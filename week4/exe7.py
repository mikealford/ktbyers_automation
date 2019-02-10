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

config_commands = ['logging buffered 30000']

ssh_switch1.send_config_set(config_commands)
ssh_switch2.send_config_set(config_commands)
ssh_switch3.send_config_set(config_commands)
