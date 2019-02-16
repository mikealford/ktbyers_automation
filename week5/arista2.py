import jsonrpclib
from pprint import pprint

ip = '192.168.122.172'
port = '80'
username = 'eapi'
password = 'cisco'

switch_url = 'http://{}:{}@{}:{}'.format(username, password, ip, port)
switch_url = switch_url + '/command-api'

remote_connect = jsonrpclib.Server(switch_url)

commands = [
            {'cmd': 'enable', 'input': 'cisco'},
            'configure terminal',
            'vlan 226',
            'name blue'
]

remote_connect.runCmds(1, commands)


