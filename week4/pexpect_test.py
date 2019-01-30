#!/usr/bin/python

import sys
import pexpect
from getpass import getpass

def main():
    ip_addr = raw_input("Enter IP address: ")
    username = 'malford'
    port = 22
    password = getpass()

    #ssh -l malford 192.168.122.172 -p 22
    ssh_conn = pexpect.spawn('ssh -l {} {} {}'.format(username, ip_addr, port))
    
    ssh_conn.logfile = sys.stdout
    ssh_conn.timeout = 3
    ssh_conn.expect('ssword:')
    ssh_conn.sendline(password)
    
    ssh_conn.expect('#')

    ssh_conn.sendline('show ip int brief')
    print(ssh_conn.before)    
    print(ssh_conn.after)

    #router_name = ssh_conn.before
    #router_name = router_name.strip()
    #prompt = router_name + ssh_conn.after
    #prompt = prompt.strip()
   

   

if __name__ == "__main__":
    main()
