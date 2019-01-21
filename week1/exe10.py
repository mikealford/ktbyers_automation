from ciscoconfparse import CiscoConfParse

config_file = CiscoConfParse('cisco_ipsec.txt')

crypto = config_file.find_objects_wo_child(parentspec=r"^crypto map CRYPTO", childspec=r"AES-SHA")

no_aes = crypto[0]

print('The following crypto maps are not using AES: ')
print(no_aes.text)
for x in no_aes.children:
  print(x.text)

 
