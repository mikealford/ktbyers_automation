#!/usr/bin/python

import sys
import pexpect
from getpass import getpass

def main():
    ip_addr = raw_input("Enter IP address: ")
    username = 'malford'
    password = getpass()

    #Establish connection
    ssh_conn = pexpect.spawn('ssh -l {} {}'.format(username, ip_addr))
    ssh_conn.timeout = 3
    ssh_conn.expect('ssword:')
    ssh_conn.sendline(password)
    ssh_conn.expect('#')

    ssh_conn.sendline('terminal len 0')
    ssh_conn.expect('#')

    ssh_conn.sendline('show ip int brief')
    ssh_conn.expect('#')

    print(ssh_conn.before)    

if __name__ == "__main__":
    main()
