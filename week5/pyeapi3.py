import pyeapi
from pprint import pprint

node1 = pyeapi.connect_to("switch1")
node2 = pyeapi.connect_to("switch1")

cmds = ["show ip route", "show ip ospf neighbor"]

pprint(node1.run_commands(cmds))
pprint(node2.run_commands(cmds))

