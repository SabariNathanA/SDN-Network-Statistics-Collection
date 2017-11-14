#!/usr/bin/evn python
from scapy.all import *
def print_summary(pkt):
    if IP in pkt:
        ip_src=pkt[IP].src
        ip_dst=pkt[IP].dst
    if TCP in pkt:
        tcp_sport=pkt[TCP].sport
        tcp_dport=pkt[TCP].dport

        print " IP src " + str(ip_src) + " TCP sport " + str(tcp_sport) 
        print " IP dst " + str(ip_dst) + " TCP dport " + str(tcp_dport)

sniff(filter="ip",prn=print_summary)
