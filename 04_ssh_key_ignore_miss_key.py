import paramiko
import time
from getpass import getpass

host = "101.132.195.238"
username = "root"
password = getpass("Enter password:")

session = paramiko.SSHClient()

session.set_missing_host_key_policy(paramiko.AutoAddPolicy)
# session.load_host_keys()
session.connect(hostname=host, port=22, username=username, password=password)

commands = ['hostname', 'ls /', 'echo $USER', 'aabb']

for command in commands:
    print(f"Executing the command: {command}")
    stdin, stdout, stderr = session.exec_command(command)
    time.sleep(.5)
    print(stdout.read().decode())
    err = stderr.read().decode()
    if err:
        print(err)

session.close()
