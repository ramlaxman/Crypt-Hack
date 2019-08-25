'''
Author: Qaidjohar Jawadwala
'''


#Import Scapy
from scapy.all import *

#Creating a Custom Packet with IP and TCP Header
packet = IP(dst="11.11.3.119")/TCP(sport=4000,dport=80)

#Looping through the ports
for port in range(1000,10000):
	#Changing Source Port address in every iteration
	packet[TCP].sport = port
	print port
	#Sending packet on network
	send(packet)

