from netmiko import ConnectHandler
from getpass import getpass

password = getpass()

switch2 = {
     'device_type': 'cisco_ios',
     'ip': '192.168.122.173',
     'username': 'malford',
     'password': password,
}

ssh_switch2 = ConnectHandler(**switch2)

ssh_switch2.config_mode()
prompt = ssh_switch2.check_config_mode()

print("Device is in config mode: {}".format(prompt))
