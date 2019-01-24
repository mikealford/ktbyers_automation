from __future__ import print_function, unicode_literals
import snmp_helper
import getpass

SYS_DESCR = '1.3.6.1.2.1.1.1.0'
SYS_NAME = '1.3.6.1.2.1.1.5.0'

def main():
   ip_addr = raw_input("ip address: ")
   community_string = getpass.getpass(prompt="Community String: ")

   switch = [ip_addr, community_string, 161]

   for a_device in switch:
       print("\n**********")
       for the_oid in (SYS_DESCR, SYS_NAME):
           snmp_data = snmp_helper.snmp_get_oid(a_device, oid=the_oid)
           output = snmp_helper.snmp_extract(snmp_data)

           print(output)
       print("**************")

if __name__ == "__main__":
    main()

