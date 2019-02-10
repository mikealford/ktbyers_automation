from netmiko import ConnectHandler
from getpass import getpass

password = getpass()

switch1 = {
     'device_type': 'cisco_ios',
     'ip': '192.168.122.172',
     'username': 'malford',
     'password': password,
}

switch2 = {
     'device_type': 'cisco_ios',
     'ip': '192.168.122.173',
     'username': 'malford',
     'password': password,
}

switch3 = {
     'device_type': 'cisco_ios',
     'ip': '192.168.122.174',
     'username': 'malford',
     'password': password,
}

ssh_switch1 = ConnectHandler(**switch1)
ssh_switch2 = ConnectHandler(**switch2)
ssh_switch3 = ConnectHandler(**switch3)

output1 = ssh_switch1.send_command("show ip arp")
output2 = ssh_switch2.send_command("show ip arp")
output3 = ssh_switch3.send_command("show ip arp")

print('Switch 1 arp:\n {}'.format(output1))
print('\n')
print('Switch 2 arp:\n {}'.format(output2))
print('\n')
print('Switch 3 arp:\n {}'.format(output3))
