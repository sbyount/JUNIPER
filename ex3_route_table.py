#!/usr/bin/env python
'''
Connect to Juniper device using PyEZ. Display the routing table.

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
from jnpr.junos.op.routes import RouteTable
from getpass import getpass

def main():
    '''
    Connect to Juniper device using PyEZ. Display the routing table.
    '''
    pwd = getpass('88newclass: ')
    ip_addr = raw_input("184.105.247.76\nEnter Juniper SRX IP: ")
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
    # get routing table
    routes = RouteTable(a_device)
    routes.get()

    print "\nJuniper SRX Routing Table: "
    for a_route, route_attr in routes.items():
        print "\n" + a_route
        for attr_desc, attr_value in route_attr:
            print " {} {}".format(attr_desc, attr_value)
    print

if __name__ == '__main__':
    main()
