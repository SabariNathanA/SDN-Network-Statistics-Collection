import subprocess
import mysql.connector
import signal
import time

def foo(interface):
	command = 'ovs-vsctl get Interface '+interface+' statistics'
	complete = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout.read()
	complete = complete[1:(len(complete)-2)]
	list = complete.split(',')
	coll = list[0].split('=')[1]
	rb = list[1].split('=')[1]
	rcrc = list[2].split('=')[1]
	rd = list[3].split('=')[1]
	rfe = list[4].split('=')[1]
	roe = list[5].split('=')[1]
	rp = list[6].split('=')[1]
	tb = list[7].split('=')[1]
	td = list[8].split('=')[1]
	te = list[9].split('=')[1]
	tp = list[10].split('=')[1]
	
	switch_index = interface.split("-")[0]
	switch_start = switch_index.find('s')+1
	switch_end = len(switch_index)
	switch_index = switch_index[switch_start:switch_end]
	
	port_index = interface.split("-")[1]
	port_start = port_index.find('eth')+3
	port_end = len(port_index)
	port_index = port_index[port_start:port_end]
	
	sw='openflow:'+str(switch_index)
	s_p =  'openflow:'+str(switch_index)+':'+str(port_index)
	data_ipsoc = {'s_p':s_p,'coll': coll, 'rb': rb, 'rcrc': rcrc,'rd':rd,'rfe':rfe,'roe':roe,'rp':rp,'tb':tb,'td':td,'te':te,'tp':tp,'sw':sw}
	cursor.execute(add_ipsoc,data_ipsoc)
	mysql_cnx.commit()

#MySQL connection setup
mysql_cnx = mysql.connector.connect(user='root', password='password',host='192.168.56.1',database='UG_DB')

run = True

#Signal handling for graceful exit of program
def signal_handler(signal, frame):
    global run
    print "...Stopped sending statistics..."
    run = False
signal.signal(signal.SIGINT, signal_handler)

# MySQL cursor -> aids insert
cursor = mysql_cnx.cursor()
add_ipsoc = ("INSERT INTO stats (Switch_port, Collisions,  RX_Bytes, RX_CRC_Errors, RX_Dropped, RX_Frame_Error, RX_Over_Error, RX_Packets, TX_Bytes, TX_Dropped, TX_Error, TX_Packets,Switch) VALUES (%(s_p)s,%(coll)s,%(rb)s,%(rcrc)s,%(rd)s,%(rfe)s,%(roe)s,%(rp)s,%(tb)s,%(td)s,%(te)s,%(tp)s,%(sw)s)")

print "Sending statistics"
while run:
	interface = 's1-eth1'
	foo(interface)
	interface = 's1-eth2'
	foo(interface)
	interface = 's1-eth3'
	foo(interface)
	interface = 's2-eth1'
	foo(interface)
	interface = 's2-eth2'
	foo(interface)
	interface = 's2-eth3'
	foo(interface)
	interface = 's2-eth4'
	foo(interface)
	interface = 's3-eth1'
	foo(interface)
	interface = 's3-eth2'
	foo(interface)
	interface = 's4-eth1'
	foo(interface)
	interface = 's4-eth2'
	foo(interface)
	time.sleep(5)
cursor.close()
mysql_cnx.close()
