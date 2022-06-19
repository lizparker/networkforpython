# how to ssh cisco router with ssh key instead of username and password
import paramiko
# from getpass import getpass
import time
'''
1.generate ssh key in your jumpbox: ssh-keygen
    by default with no passphase
2.find id_rsa.pub in /var/root/.ssh
3.wrap pub key with 64 bits since the maximum line lengh at cisco CLI is 254
    characters: fold -b -w 64 id_rsa.pub
4.copy the key-string to cisco CLI
    conf t:
    ip ssh pubkey-chain
    username admin
    key-string XXX
    exit
5.ssh cisco from your jumpbox:
    ssh -oKexAlgorithms=+diffie-hellman-group1-sha1 -l <username> <ip_address>
6.bug about 5 in paramiko, you may use the 'disabled_algorithms' SSHClient/
    Transport init kwarg to disable that or other algorithms if your server
    does not support them
    disabled_algorithms=dict(
        pubkeys=["rsa-sha2-512", "rsa-sha2-256"])
'''
paramiko.util.log_to_file("log.txt", level="DEBUG")
# paramiko.transport._preferred_kex = ('diffie-hellman-group-exchange-sha1',
#                                     'diffie-hellman-group1-sha1',
#                                     'diffie-hellman-group14-sha1',
#                                     )

host = "63.116.24.66"
username = "cicny"
password = "cic123$%^"

session = paramiko.SSHClient()

session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# session.load_system_host_keys()

key_file = paramiko.RSAKey.from_private_key_file("/var/root/.ssh/id_rsa")
# key_pass = getpass("Enter priviate key password:")

session.connect(hostname=host,
                username=username,
                disabled_algorithms=dict(
                    pubkeys=["rsa-sha2-512", "rsa-sha2-256"]),
                # password=password
                pkey=key_file
                )

device_access = session.invoke_shell()
time.sleep(1)
device_access.send('term length 0\n')
# time.sleep(1)
device_access.send('show ip int brief\n')
time.sleep(5)
output = device_access.recv(65000)
print(">>>>>", type(output))
print(output.decode('ascii'))

session.close()
