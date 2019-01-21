from ciscoconfparse import CiscoConfParse

config_file = CiscoConfParse('cisco_ipsec.txt')

crypto = config_file.find_objects(r"^crypto map CRYPTO")

map10 = crypto[0]
map20 = crypto[1]
map30 = crypto[2]
map40 = crypto[3]
map50 = crypto[4]

print(map10.text)
for x in map10.children:
  print (x.text)

print(map20.text)
for x in map20.children:
  print (x.text)

print(map30.text)
for x in map30.children:
  print (x.text)

print(map40.text)
for x in map40.children:
  print (x.text)

print(map50.text)
for x in map50.children:
  print (x.text)

