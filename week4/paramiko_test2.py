import time
import paramiko
from getpass import getpass

ip_addr = '192.168.122.172'
username = 'malford'
password = getpass()
port = 22

remote_conn_pre = paramiko.SSHClient()
remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
remote_conn_pre.connect(ip_addr, username=username, password=password, look_for_keys=False, allow_agent=False, port=port)

remote_conn = remote_conn_pre.invoke_shell()

remote_conn.send("show ip int br\n")
time.sleep(1)
outp = remote_conn.recv(5000)
print(outp)

remote_conn.close
