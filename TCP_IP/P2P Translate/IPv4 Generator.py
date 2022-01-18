import ipaddress
net = ipaddress.ip_network('10.2.5.184/29', strict=False)
a = [str(ip) for ip in ipaddress.IPv4Network(net)]
print(a)

#
# config = {
#     'IP': '127.0.0.0',
#     'Port': 8888,
#     'IP_RANGE': '127.0.1.0/24',
#     'PORT_RANGE': '65525-65535'
# }
#
# def get_all_possible_addresses():
#     ips = [str(ip) for ip in ipaddress.IPv4Network(config['IP_RANGE'])][1:-1]
#     port_min, port_max = config['PORT_RANGE'].split('-')
#     ports = range(int(port_min), int(port_max) + 1)
#     ip_port = []
#     for port in ports:
#         for ip in ips:
#             ip_port.append((ip, port))
#     return ip_port
#
#
# print(get_all_possible_addresses())


# # importing socket module
# import socket
#
# # creates a new socket using the given address family.
# socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# # setting up the default timeout in seconds for new socket object
# socket.setdefaulttimeout(1)
#
# # returns 0 if connection succeeds else raises error
# result = socket_obj.connect_ex((addr, port))  # address and port in the tuple format
#
# # closes te object
# socket_obj.close()