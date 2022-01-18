import socket
import threading
import ipaddress
from concurrent.futures import ThreadPoolExecutor
from itertools import repeat
from Client import Client


config = {
    'IP': '10.2.5.186',
    'Port': 65525,
    'IP_RANGE': '10.2.5.0/24',
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


def translate_loc(conn, word: str):
    if word.lower() in words.keys():
        conn.send(f'TRANSLATESUC"{words[word.lower()]}"'.encode())
    else:
        conn.send('TRANSLATEERR"Unknown word"'.encode())


def translate_rem(conn, word: str):
    command = 'TRANSLATEREM'
    with ThreadPoolExecutor(max_workers=len(available_servers)) as executor:
        executor.map(find_translation, available_servers, repeat(word), repeat(command), repeat(conn))


def translate_any(word: str) -> str:
    pass


commands = {
    'TRANSLATELOC': translate_loc,
    'TRANSLATEREM': translate_rem,
    'TRANSLATEANY': translate_any
}


def find_translation(server, word: str, command: str, conn):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(server)
    client.send(f'{command}"{word}"'.encode())
    answer = client.recv(1024)
    conn.send(answer)


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
    # all_servers = get_all_possible_addresses()
    all_servers = [str(ip) for ip in ipaddress.IPv4Network(config['IP_RANGE'])][1:-1]
    with ThreadPoolExecutor(max_workers=len(all_servers)) as executor:
        executor.map(check_ip, all_servers)
    # for server in all_servers:
    #     try:
    #         socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #         socket.setdefaulttimeout(3)
    #         result = socket_obj.connect_ex(server)
    #         print(f'Found {server[0]} + {server[1]}')
    #         # socket_obj.send('TRANSLATELOC"asdasdasd"'.encode())
    #         # if 'TRANSLATE' in socket_obj.recv(1024).decode():
    #         #     available_servers.append(server)
    #         socket_obj.close()
    #     except:
    #         continue


def check_ip(server):
    try:
        port_min, port_max = config['PORT_RANGE'].split('-')
        ports = range(int(port_min), int(port_max) + 1)
        for port in ports:
            socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(3)
            result = socket_obj.connect_ex((server, port))
            socket_obj.send('TRANSLATELOC"asdasdasd"'.encode())
            #if 'TRANSLATE' in socket_obj.recv(1024).decode():
            available_servers.append(server)
            print(f'Found {server} + {port}')
            socket_obj.close()
    except:
        pass


def client_thread(conn, addr):
    conn.send(f"Welcome to this chatroom! Your ip address is: {addr}".encode())
    while True:
        try:
            if True:
                message = conn.recv(1024).decode()
                command, word = message.split('"')[:-1]
                if command.upper() in commands.keys():
                    commands[command.upper()](conn, word)
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
        print('Server Started')
        find_available_servers()
        while True:
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


