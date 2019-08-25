#Import Scapy Library
'''
Author: Qaidjohar Jawadwala
'''

from scapy.all import *
#No useless data on the screen
conf.verb = 0

#looping through the IP
for i in range(1,20):
	ip = "11.11.1."+str(i)
	#Sending ICMP request to the destination IP
	request = IP(dst=ip,ttl=10)/ICMP()
	
	#Sending data on the network and receiving the reply into reply variable
	reply = sr1(request,timeout=2)

	#If host is down, then reply variable is None
	if (reply is None):
		print(ip + " is Down")
	else:
		print(ip + " is Up")
