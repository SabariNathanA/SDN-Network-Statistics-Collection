import csv, sys
TOPOLOGY_NAME = "h3s4"
PORT = "Switch_numberofport.csv"
OUTPUT_TOPO = "topo_consolidated.py"
OUTPUT_SNIFFER = "sniffer_consolidated.py"
OUTPUT_STAT = "stat_consolidated.py"
INPUT = "topo.csv"

interface_list = {}
mac_host=10
mac_switch=10
no_of_switch = 0

########################## Topology generation ################################## 

# FUnction to add hosts and switches
def addHost(src,typ):
	global mac_host, mac_switch
	entry=""
	if(typ == 'h'):
		now_mac='00:00:00:00:00:'+str(mac_host)
		entry = ""+str(src)+' = net.addHost("'+str(src)+'",mac="'+now_mac+'")\n'
		mac_host += 1
#		print entry
	elif(typ == 's'):
		now_mac='00:00:00:00:10:'+str(mac_switch)
		entry = ""+str(src)+' = net.addSwitch("'+str(src)+'",listenPort=6634,mac="'+now_mac+'")\n'
		mac_switch += 1
#		print entry
	opPy_file.write(entry)

# Function for adding links
def addLink(src,dst,styp,dtyp):
	entry = ""
	if(styp == dtyp): # Lnk between 2 switches
		entry = ""+"net.addLink( "+str(src)+", "+str(dst)+", bw=100, delay='7.5ms',use_htb=True)"+"\n"
	else:
		entry = ""+"net.addLink( "+str(src)+", "+str(dst)+", bw=5, delay='5ms',use_htb=True)"+"\n"
	opPy_file.write(entry)
#	print entry

opPy_file = open(OUTPUT_TOPO,'w')

# Header
opPy_file.write('from mininet.net import Mininet\n\
from mininet.node import Controller, RemoteController\n\
from mininet.topo import Topo\n\
from mininet.link import TCLink  # So we can rate limit links\n\
from mininet.cli import CLI  # So we can bring up the Mininet CLI\n\n\
net = Mininet(topo=None, link=TCLink, build=False)\n')


# read the csv file
try:
	matrixFile = open(INPUT, 'rb')
except:
	print INPUT,"<< Can't find the connection MATRIX file"
	sys.exit()
matrixFile = csv.reader(matrixFile, delimiter=',')
matrix=[]
for row in matrixFile:
	matrix.append(row)
# matrix is now an array of rows of the CSV file.

# Adding hosts and switches
opPy_file.write('print "**** Adding hosts and switches ****"\n')
for i in range(1,len(matrix)):
	row = matrix[i]
	if (row[0] != ''):
		src = row[0]
		typ = src[0]
		addHost(src,typ)
		interface_list[src] = 0

# Adding links
opPy_file.write('print "**** Adding Traffic conditioned links ****"\n')
opPy_file.write('\n# Add links\n')
for i in range(1,len(matrix)):
	row = matrix[i]
	if (row[0] != ''):
		src = row[0]
		styp = src[0]
		for j in range(1,len(row),1):
			if ((row[j]=="") or (row[j]=="0")):
				print 
			else:
				dst = row[j]
				dtyp = dst[0]
				interface_list[src] += 1
				interface_list[dst] += 1
				addLink(src, dst,styp,dtyp)

opPy_file.write('print "**** Adding Remote controller from 192.168.56.1:6653****"\n')
opPy_file.write("\n# Add controller\nodl_c = net.addController('c0',controller=RemoteController,ip='192.168.56.1', port=6653)\nnet.build()\n\n")

# Helper for sniffer script
opCsv_file = open(PORT,'w')
for i in interface_list:
	if(i[0] == 's'):
		# Starting switch with corresponding controllers
		opPy_file.write(str(i)+".start([odl_c])\n")
		no_of_switch += 1
	entry=""
	entry = i+','+str(interface_list[i])+'\n'
	opCsv_file.write(entry)
#	print i+' - '+str(interface_list[i])
print "Writing switch to port mapping file....done!"
opCsv_file.close()

opPy_file.write("# Bring up the mininet CLI\n\
CLI(net) \n\
net.stop()\n")
print "Writing topology file....done!"
opPy_file.close()

########################## Next Sniffer generation ##################################

opPy_file = open(OUTPUT_SNIFFER,'w')
# Headers 
opPy_file.write("#!/usr/bin/evn python\n\
from scapy.all import *\n\
import signal\n\
import mysql.connector\n\n\
#MySQL connection setup\n\
mysql_cnx = mysql.connector.connect(user='root', password='password',host='192.168.56.1',database='UG_DB')\n\n\
#list to store ip&port#match\n\
list_ipsoc = []\n\
run = True\n\n\
#Signal handling for graceful exit of program\n\
def signal_handler(signal, frame):\n\
\tglobal run\n\
\tprint \"...Safely Exiting sniff mode...\"\n\
\trun = False\n\
signal.signal(signal.SIGINT, signal_handler)\n\n\
# MySQL cursor -> aids insert\n\
cursor = mysql_cnx.cursor()\n\
add_ipsoc = (\"INSERT INTO routeinfo (Sender_IP, Dest_IP, Sender_port, Dest_port, Switch_port, Switch) VALUES (%(sip)s,%(dip)s,%(sp)s,%(dp)s,%(s_p)s,%(sw)s)\")\n\n\
print \"Started sniffing on all interfaces...\"\n\
while run:\n\
\ta = sniff(iface=[")

entry = ""
for i in interface_list:
	if(i[0] == 's'):
		number = interface_list[i]
		for j in range(1,number+1):
			entry += '"'+str(i)+'-eth'+str(j)+'",'

entry = entry[0:(len(entry)-1)] # Removing the last comma
opPy_file.write(entry)

# Rest of the file
opPy_file.write("],count =1)\n\
\tfor pkt in a:\n\
\t\tif(pkt.haslayer(IP)):\n\
\t\t\tip_src = pkt.getlayer(IP).src\n\
\t\t\tip_dst = pkt.getlayer(IP).dst\n\
\t\t\tip_pair = ip_src + ' ' + ip_dst\n\n\
\t\t\t# Interface extractor\n\
\t\t\tinterface = pkt.sniffed_on\n\n\
\t\t\t# String parsing to converst s1-eth1 to openflow:1:1\n\
\t\t\tswitch_index = interface.split(\"-\")[0]\n\
\t\t\tswitch_start = switch_index.find('s')+1\n\
\t\t\tswitch_end = len(switch_index)\n\
\t\t\tswitch_index = switch_index[switch_start:switch_end]\n\n\
\t\t\tport_index = interface.split(\"-\")[1]\n\
\t\t\tport_start = port_index.find('eth')+3\n\
\t\t\tport_end = len(port_index)\n\
\t\t\tport_index = port_index[port_start:port_end]\n\n\
\t\tif (pkt.haslayer(TCP)):\n\
\t\t\ttcp_sport=pkt[TCP].sport\n\
\t\t\ttcp_dport=pkt[TCP].dport\n\n\
\t\t\tsw='openflow:'+str(switch_index)\n\
\t\t\tswitch_port = 'openflow:'+str(switch_index)+':'+str(port_index)\n\
\t\t\tip_sock_pair = ip_pair +' '+ str(tcp_sport) +' '+ str(tcp_dport) + ' ' + str(switch_port)\n\
\t\t\tif(ip_sock_pair not in list_ipsoc):\n\
\t\t\t\tlist_ipsoc.append(ip_sock_pair)\n\
\t\t\t\tdata_ipsoc = {'sip': ip_src, 'dip': ip_dst, 'sp': tcp_sport,'dp': tcp_dport,'s_p':switch_port,'sw':sw}\n\
\t\t\t\tcursor.execute(add_ipsoc,data_ipsoc)\n\
\t\t\t\tmysql_cnx.commit()\n\
\t\t\t\tprint ip_sock_pair\n\
cursor.close()\n\
mysql_cnx.close()")

print "Writing Sniffer python file....done!"
opPy_file.close()

########################## Stat_Collector file ##################################
opPy_file = open(OUTPUT_STAT,'w')
# Headers 



opPy_file.write("import subprocess\n\
import mysql.connector\n\
import signal\n\
import time\n\n")

opPy_file.write("def foo(interface):\n")
opPy_file.write("\tcommand = 'ovs-vsctl get Interface '+interface+' statistics'\n")
opPy_file.write("\tcomplete = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout.read()\n")
opPy_file.write("\tcomplete = complete[1:(len(complete)-2)]\n\tlist = complete.split(',')\n\tcoll = list[0].split('=')[1]\n\trb = list[1].split('=')[1]\n\trcrc = list[2].split('=')[1]\n\trd = list[3].split('=')[1]\n\trfe = list[4].split('=')[1]\n\troe = list[5].split('=')[1]\n\trp = list[6].split('=')[1]\n\ttb = list[7].split('=')[1]\n\ttd = list[8].split('=')[1]\n\tte = list[9].split('=')[1]\n\ttp = list[10].split('=')[1]\n\t\n\t")
opPy_file.write('switch_index = interface.split("-")[0]\n\tswitch_start = switch_index.find(\'s\')+1\n\tswitch_end = len(switch_index)\n\tswitch_index = switch_index[switch_start:switch_end]\n\t\n\tport_index = interface.split("-")[1]\n\tport_start = port_index.find(\'eth\')+3\n\tport_end = len(port_index)\n\tport_index = port_index[port_start:port_end]\n\t\n\t')
opPy_file.write("sw='openflow:'+str(switch_index)\n\ts_p =  'openflow:'+str(switch_index)+':'+str(port_index)\n\tdata_ipsoc = {'s_p':s_p,'coll': coll, 'rb': rb, 'rcrc': rcrc,'rd':rd,'rfe':rfe,'roe':roe,'rp':rp,'tb':tb,'td':td,'te':te,'tp':tp,'sw':sw}\n\tcursor.execute(add_ipsoc,data_ipsoc)\n\tmysql_cnx.commit()\n\n")


opPy_file.write("#MySQL connection setup\n\
mysql_cnx = mysql.connector.connect(user='root', password='password',host='192.168.56.1',database='UG_DB')\n\n\
run = True\n\n\
#Signal handling for graceful exit of program\n\
def signal_handler(signal, frame):\n\
    global run\n\
    print \"...Stopped sending statistics...\"\n\
    run = False\n\
signal.signal(signal.SIGINT, signal_handler)\n\n\
# MySQL cursor -> aids insert\n\
cursor = mysql_cnx.cursor()\n\
add_ipsoc = (\"INSERT INTO stats (Switch_port, Collisions,  RX_Bytes, RX_CRC_Errors, RX_Dropped, RX_Frame_Error, RX_Over_Error, RX_Packets, TX_Bytes, TX_Dropped, TX_Error, TX_Packets,Switch) VALUES (%(s_p)s,%(coll)s,%(rb)s,%(rcrc)s,%(rd)s,%(rfe)s,%(roe)s,%(rp)s,%(tb)s,%(td)s,%(te)s,%(tp)s,%(sw)s)\")\n\n\
print \"Sending statistics\"\n\
while run:\n")

for k in range(1,no_of_switch+1):
	no_of_ports = interface_list['s'+str(k)]
	for l in range(1,no_of_ports+1):
		interface = 's'+str(k)+'-eth'+str(l)
		opPy_file.write("\tinterface = '"+interface+"'\n")
		opPy_file.write("\tfoo(interface)\n")

opPy_file.write("\ttime.sleep(5)\ncursor.close()\nmysql_cnx.close()\n")

print "Writing statistics generator file....done!"
opPy_file.close()

