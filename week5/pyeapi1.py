import pyeapi
from pprint import pprint

switch1 = pyeapi.connect_to('switch1')
switch2 = pyeapi.connect_to('switch2')

cmds = ['vlan 225', 'name red', 'vlan 226', 'name black']

switch2.config(cmds)

#pprint(switch1.run_commands("show version"))
