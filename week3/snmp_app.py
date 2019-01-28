import snmp_helper

IP = '192.168.122.172'
COMMUNITY_STRING = 'galileo1'
SNMP_PORT = 161


pynet_rtr1 = (IP, COMMUNITY_STRING, SNMP_PORT)

snmp_data = snmp_helper.snmp_get_oid(pynet_rtr1, oid='1.3.6.1.2.1.1.5.0')

output = snmp_helper.snmp_extract(snmp_data)

print(output)
