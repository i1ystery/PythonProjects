import ipaddress
a = [str(ip) for ip in ipaddress.IPv4Network('192.168.1.0/24')]
print(len(a))

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