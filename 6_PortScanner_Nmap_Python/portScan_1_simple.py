import nmap

#Defining an object for Scanning Port
nm = nmap.PortScanner()

#Scanning Port as provided in arguments
nm.scan('11.11.3.200-220','1-100')

print(nm.all_hosts())


