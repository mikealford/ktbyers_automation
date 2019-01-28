import snmp_helper

IP = '192.168.122.172'
COMMUNITY_STRING = 'galileo1'
SNMP_PORT = 161

pynet_rtr1 = (IP, COMMUNITY_STRING, SNMP_PORT)

snmp_oids = (
    ('sysName', '1.3.6.1.2.1.1.5.0', None),
    ('sysUptime', '1.3.6.1.2.1.1.3.0', None),
    ('ifDescr_gi0', '1.3.6.1.2.1.2.2.1.2.5', None),
    ('ifInOctets_gi0', '1.3.6.1.2.1.2.2.1.10.5', True),
    ('ifInUcastPkts_gi0', '1.3.6.1.2.1.2.2.1.11.5', True),
    ('ifOutOctets_gi0', '1.3.6.1.2.1.2.2.1.16.5', True),
    ('ifOutUcastPkts_gi0', '1.3.6.1.2.1.2.2.1.17.5', True),
)

snmp_data = snmp_helper.snmp_get_oid(pynet_rtr1, oid=snmp_oids[0])
output = snmp_helper.snmp_extract(snmp_data)
print(output)
