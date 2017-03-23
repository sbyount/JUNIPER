#!/usr/bin/env python
'''
Connect to Juniper device using PyEZ. Display device facts.

There is a Juniper SRX100 in the lab environment. Here is its login information:

IP Address: 184.105.247.76
SSH Port: 22
NETCONF Port (API): 830


Username: pyclass
Password: 88newclass

From the lab environment, you can SSH into the SRX as follows:
$ ssh -l pyclass 184.105.247.76

'''

from jnpr.junos import Device
from getpass import getpass
from pprint import pprint

def main():
    '''
    Connect to Juniper device using PyEZ. Display device facts.
    '''
    pwd = getpass()
    ip_addr = raw_input("Enter Juniper SRX IP: ")
    ip_addr = ip_addr.strip()

    juniper_srx = {
        "host": ip_addr,
        "user": 'pyclass',
        "password": pwd
    }

    print "\n\nConnecting to Juniper SRX...\n"
    # create device object with all the arguments in the dictionary
    a_device = Device(**juniper_srx)
    a_device.open()
    pprint(a_device.facts)
    print

if __name__ == '__main__':
    main()
