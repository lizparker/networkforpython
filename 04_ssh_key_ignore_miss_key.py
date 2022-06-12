import paramiko
import time
from getpass import getpass

host = "101.132.195.238"
username = "root"
password = getpass("Enter password:")

session = paramiko.SSHClient()

session.set_missing_host_key_policy(paramiko.AutoAddPolicy)

session.connect(hostname=host, port=22, username=username, password=password)
stdin, stdout, stderr = session.exec_command('hostname')
time.sleep(.5)
print(f"Hostname is: {stdout.read().decode()}")

session.close()
