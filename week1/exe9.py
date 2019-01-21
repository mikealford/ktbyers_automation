from ciscoconfparse import CiscoConfParse

config_file = CiscoConfParse('cisco_ipsec.txt')

crypto = config_file.find_objects_w_child(parentspec=r"^crypto map CRYPTO", childspec=r"group2")

print('The following crypto maps contain pfs2: ')
for x in crypto:
  print(x.text)

 
