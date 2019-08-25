import nmap

#Defining an object for Scanning Port
nm = nmap.PortScanner()

#Scanning Port as provided in arguments
nm.scan('11.11.3.200-220','1-100')

#Iterating all hosts with up status
for host in nm.all_hosts():
	state = nm[host].state()
	print("Scanned: %s \t State: %s" %(host,state))
	#Iterating protocols on a host
	for protocols in nm[host].all_protocols():
		ports_list = nm[host][protocols].keys()
		#Iterating port in a protocol on a host
		for port in ports_list:
			#Storing the State of the Port (Open/Close)
			#nm['11.11.3.205']['tcp'][22]['state']
			pstate = nm[host][protocols][port]['state']
			#Storing name of the Port Service (http,ssh..)
			#nm['11.11.3.205']['tcp'][80]['name']
			pname = nm[host][protocols][port]['name']
			print("Port:%s \t State:%s \t Service:%s" %(port,pstate,pname))
		#print port
	print("")
	


