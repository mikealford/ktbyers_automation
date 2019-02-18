import pyeapi
from pprint import pprint

#Connect to switch1
node1 = pyeapi.connect_to('switch1')

#Show interfaces
interfaces = node1.enable("show interfaces")

#Remove parent list so only dictionary remains (unpack)
interfaces = interfaces[0]

#Further unpack to display just dictionary of interfaces
interfaces = interfaces['result']
interfaces = interfaces['interfaces']

for port in interfaces.items():
    pprint(port)
