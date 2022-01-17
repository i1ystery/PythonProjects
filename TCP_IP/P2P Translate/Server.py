import socket
import threading
import ipaddress
from Client import Client

online = True
config = {
    'IP': '127.0.0.1',
    'Port': 8888,
    'IP_RANGE': '127.0.0.1/24',
    'PORT_RANGE': '65525-65535'
}
words = {
    'future': 'budoucnost',
    'memory': 'paměť',
    'speed': 'rychlost',
    'food': 'jídlo',
    'shadow': 'stín'
}
available_servers = []


def translate_loc(word: str) -> str:
    if word.lower() in words.keys():
        return f'TRANSLATESUC"{words[word.lower()]}"'
    else:
        return 'TRANSLATEERR"Unknown word"'


def translate_rem(word: str) -> str:



def translate_any(word: str) -> str:
    pass


commands = {
    'TRANSLATELOC': translate_loc,
    'TRANSLATEREM': translate_rem,
    'TRANSLATEANY': translate_any
}


def new_client():



def get_all_possible_addresses():
    ips = [str(ip) for ip in ipaddress.IPv4Network(config['IP_RANGE'])][1:-1]
    port_min, port_max = config['PORT_RANGE'].split('-')
    ports = range(int(port_min), int(port_max) + 1)
    ip_port = []
    for port in ports:
        for ip in ips:
            ip_port.append((ip, port))
    return ip_port


def find_available_servers():
    all_servers = get_all_possible_addresses()
    for server in all_servers:
        try:
            socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(3)
            result = socket_obj.connect_ex(server)
            socket_obj.close()
            available_servers.append(server)
        except:
            pass


def client_thread(conn, addr):
    conn.send(f"Welcome to this chatroom! Your ip address is: {addr}".encode())
    while True:
        try:
            global online
            if online:
                message = conn.recv(1024).decode()
                command, word = message.split('"')[:-1]
                if command.upper() in commands.keys():
                    translated = commands[command.upper()](conn, word)
                    conn.send(translated.encode())
                else:
                    conn.send('Invalid command'.encode())
            else:
                break
        except Exception as e:
            print(e)
            break


def run():
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((config['IP'], config['Port']))
        server.listen()
        while online:
            conn, addr = server.accept()
            print(addr[0] + " connected")
            t = threading.Thread(target=client_thread, args=(conn, addr))
            t.start()
    except OSError as e:
        print(e)
        print('Server stopped')
    except Exception as e:
        print(e)


if __name__ == '__main__':
    run()


