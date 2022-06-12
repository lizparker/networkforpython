# scan range of port
import socket

socket.setdefaulttimeout(.5)
# destination = ('63.116.24.66', 22)
print('\n', '#'*50, '\nStarted executing script', '\n', '#'*50)


def portrange_check(ip, sp, ep):
    ep = ep + 1
    try:
        for port in range(sp, ep):
            device_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result_of_check = device_socket.connect_ex((ip, port))
            # print(result_of_check)

            if result_of_check == 0:
                print(ip, "is listening on port:", port)
                device_socket.close()
            else:
                # print(ip, 'is not listening on port:', port)
                device_socket.close()
    except:
        print('Exception occurred')
        pass


# portrange_check('63.116.24.66', 22, 23)
portrange_check('114.255.166.82', 1, 65536)
