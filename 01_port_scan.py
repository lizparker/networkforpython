import socket

socket.setdefaulttimeout(.5)
# destination = ('63.116.24.66', 22)
print('\n', '#'*50, '\nStarted executing script', '\n', '#'*50)


def port_check(ip, port):
    device_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result_of_check = device_socket.connect_ex((ip, port))
    # print(result_of_check)

    if result_of_check == 0:
        print(ip, "is listening on port:", port)
        device_socket.close()
    else:
        print(ip, 'is not listening on port:', port)
        device_socket.close()


port_check('63.116.24.66', 22)
