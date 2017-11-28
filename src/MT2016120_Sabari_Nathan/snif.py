#!/usr/bin/evn python
from scapy.all import *
#list to store ip&port#match
list = []
while True:
	#a = sniff(iface=["s1-eth1","s1-eth2"], count=1)
	a = sniff(iface=["s1-eth1","s1-eth2"], prn=lambda x: x.sniffed_on+": "+x.summary())
	for pkt in a:
		if(pkt.haslayer(IP)):
			ip_src = pkt.getlayer(IP).src
			ip_dst = pkt.getlayer(IP).dst
			ip_pair = ip_src + ' ' + ip_dst
			if(ip_pair not in list):		
				list.append(ip_pair)
				#replace this with MySQL connection
				print ip_pair
		if (pkt.haslayer(TCP)):
        		tcp_sport=pkt[TCP].sport
        		tcp_dport=pkt[TCP].dport
