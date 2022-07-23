#!/usr/bin/env python3

import optparse
import nmap

class NmapScanner:
     
    def __init__(self): 
        self.port_scan = nmap.PortScanner()
    
    def nmapScan(self, host, port): 
        self.port_scan.scan(host, port) 
        self.state = self.port_scan[host]['tcp'][int(port)]['state']
        print(" [+] Executing command: ", self.port_scan.command_line()) 
        print(" [+] "+ host + " tcp/" + port + " " + self.state)

def main():
    parser = optparse.OptionParser("usage:  " + "-host <target host> -port <target port>") 
    parser.add_option('--host', dest = 'host', type = 'string', help = 'specify the target ip address.')
    parser.add_option('--port', dest = 'ports', type = 'string', help = 'specify the target port(s)')
    (options, args) = parser.parse_args()
    if (options.host == None) | (options.ports == None): 
        print('[-] You must specify a target host and a target port(s).')
        exit(0)
    host = options.host
    ports = options.ports.split(',')

    for port in ports: 
        NmapScanner().nmapScan(host, port)

if __name__ == "__main__": 
    main()
