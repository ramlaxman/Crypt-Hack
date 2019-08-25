'''
Author: Qaidjohar Jawadwala
'''

#Import Scapy
from scapy.all import *

#Creating a Custom Packet with IP(custom source IP) and TCP Header
packet = IP(src="192.168.2.100",dst="11.11.3.119")/TCP(sport=4000,dport=80)

#Looping through the ports
for port in range(1000,10000):
	#Updating Port Address
	packet[TCP].sport = port
	print port
	
	#Sending data on the Network
	send(packet)

