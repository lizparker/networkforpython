# scan fqdn of host
import socket

socket.setdefaulttimeout(.5)
# destination = ('63.116.24.66', 22)
print('\n', '#'*50, '\nStarted executing script from',
      socket.gethostname(), '\n', '#'*50)


def port_check(ip, port):
    print('~'*20)
    print('fqdn is', socket.getfqdn(ip))
    print('IP is', socket.gethostbyname(ip))
    print('PTR record is', socket.gethostbyaddr(ip))  # get the PTR record
    device_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result_of_check = device_socket.connect_ex((ip, port))
    # print(result_of_check)

    if result_of_check == 0:
        print(ip, "is listening on port:", port)
        device_socket.close()
    else:
        print(ip, 'is not listening on port:', port)
        device_socket.close()


port_check('mail02.morganstanleyhuaxin.com', 25)
