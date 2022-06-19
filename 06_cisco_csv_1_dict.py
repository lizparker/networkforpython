# handling config in a dict
conf_dict = {'63.116.24.66': ['terminal len 0',
                              'config t',
                              'interface loopback 100',
                              'ip add 100.1.1.1 255.255.255.0',
                              'no shut',
                              'exit',
                              'exit',
                              'show ip int brief'],
             '152.193.10.179': ['terminal len 0',
                                'config t',
                                'interface loopback 101',
                                'ip add 101.1.1.1 255.255.255.0',
                                'no shut',
                                'exit',
                                'exit',
                                'show ip int brief'],
             }

for ip in conf_dict.keys():
    print(f"IP address is: {ip}")
    # print(conf_dict[ip])
    for conf in conf_dict[ip]:
        print(conf)
