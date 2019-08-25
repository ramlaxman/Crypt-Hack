'''
Author: Qaidjohar Jawadwala
'''

#Import Scapy
from scapy.all import *

#Creating a Custom Packet with IP and TCP Header
packet = IP(dst="11.11.3.208")/TCP(sport=45000,dport=80)

#Sending the packet created on the network
send(packet)
