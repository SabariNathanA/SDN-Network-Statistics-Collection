#!/usr/bin/evn python
from scapy.all import *
import signal
import mysql.connector

#MySQL connection setup
mysql_cnx = mysql.connector.connect(user='root', password='password',host='192.168.56.1',database='UG_DB')

#list to store ip&port#match
list_ipsoc = []
run = True

#Signal handling for graceful exit of program
def signal_handler(signal, frame):
	global run
	print "...Safely Exiting sniff mode..."
	run = False
signal.signal(signal.SIGINT, signal_handler)

# MySQL cursor -> aids insert
cursor = mysql_cnx.cursor()
add_ipsoc = ("INSERT INTO routeinfo (Sender_IP, Dest_IP, Sender_port, Dest_port, Switch_port, Switch) VALUES (%(sip)s,%(dip)s,%(sp)s,%(dp)s,%(s_p)s,%(sw)s)")

print "Started sniffing on all interfaces..."
while run:
	a = sniff(iface=["s1-eth1","s1-eth2","s1-eth3","s4-eth1","s4-eth2","s3-eth1","s3-eth2","s2-eth1","s2-eth2","s2-eth3","s2-eth4"],count =1)
	for pkt in a:
		if(pkt.haslayer(IP)):
			ip_src = pkt.getlayer(IP).src
			ip_dst = pkt.getlayer(IP).dst
			ip_pair = ip_src + ' ' + ip_dst

			# Interface extractor
			interface = pkt.sniffed_on

			# String parsing to converst s1-eth1 to openflow:1:1
			switch_index = interface.split("-")[0]
			switch_start = switch_index.find('s')+1
			switch_end = len(switch_index)
			switch_index = switch_index[switch_start:switch_end]

			port_index = interface.split("-")[1]
			port_start = port_index.find('eth')+3
			port_end = len(port_index)
			port_index = port_index[port_start:port_end]

		if (pkt.haslayer(TCP)):
			tcp_sport=pkt[TCP].sport
			tcp_dport=pkt[TCP].dport

			sw='openflow:'+str(switch_index)
			switch_port = 'openflow:'+str(switch_index)+':'+str(port_index)
			ip_sock_pair = ip_pair +' '+ str(tcp_sport) +' '+ str(tcp_dport) + ' ' + str(switch_port)
			if(ip_sock_pair not in list_ipsoc):
				list_ipsoc.append(ip_sock_pair)
				data_ipsoc = {'sip': ip_src, 'dip': ip_dst, 'sp': tcp_sport,'dp': tcp_dport,'s_p':switch_port,'sw':sw}
				cursor.execute(add_ipsoc,data_ipsoc)
				mysql_cnx.commit()
				print ip_sock_pair
cursor.close()
mysql_cnx.close()