import json
import socket
import threading
import ipaddress
from concurrent.futures import ThreadPoolExecutor
from itertools import repeat


def load_config():
    with open("config.json", 'r') as f:
        return json.load(f)


words = {
    'future': 'budoucnost',
    'memory': 'paměť',
    'speed': 'rychlost',
    'food': 'jídlo',
    'shadow': 'stín'
}
available_servers = []
config = load_config()


def translate_loc(conn, word: str):
    if word.lower() in words.keys():
        conn.send(f'TRANSLATESUC"{words[word.lower()]}"'.encode())
    else:
        conn.send('TRANSLATEERR"Unknown word"'.encode())


def translate_rem(conn, word: str):
    find_available_servers()
    if available_servers:
        with ThreadPoolExecutor(max_workers=len(available_servers)) as executor:
            executor.map(find_translation, available_servers, repeat(word), repeat(conn))


def translate_any(conn, word: str):
    if word.lower() in words.keys():
        conn.send(f'TRANSLATESUC"{words[word.lower()]}"'.encode())
    else:
        conn.send('TRANSLATEERR"Unknown word"'.encode())
        translate_rem(conn, word)


commands = {
    'TRANSLATELOC': translate_loc,
    'TRANSLATEREM': translate_rem,
    'TRANSLATEANY': translate_any,
}


def find_translation(server, word: str, conn):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(server)
    client.recv(1024)
    client.send(f'TRANSLATELOC"{word}"'.encode())
    answer = client.recv(1024)
    print(answer)
    conn.send(answer)


def find_available_servers():
    all_servers = [str(ip) for ip in ipaddress.IPv4Network(config['IP_RANGE'])][1:-1]
    with ThreadPoolExecutor(max_workers=len(all_servers)) as executor:
        executor.map(check_ip, all_servers)


def check_ip(server):
    try:
        if server == config['IP']:
            raise
        port_min, port_max = config['PORT_RANGE'].split('-')
        ports = range(int(port_min), int(port_max) + 1)
        for port in ports:
            print(f'Checking {server}, {port}')
            socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(3)
            socket_obj.connect_ex((server, port))
            socket_obj.recv(1024)
            socket_obj.send('TRANSLATELOC"asdasdasd"'.encode())
            msg = socket_obj.recv(1024).decode()
            print(msg)
            socket_obj.close()
            if 'TRANSLATE' in msg:
                print(f'Found {server} + {port}')
                available_servers.append((server, port))
    except:
        pass


def client_thread(conn, addr):
    conn.send(f"Welcome to this chatroom! Your ip address is: {addr}".encode())
    while True:
        try:
            message = conn.recv(1024).decode()
            if message == '\r\n' or message == '\r':
                message = conn.recv(1024).decode()
            command, word = message.split('"')[:-1]
            if command.upper() in commands.keys():
                commands[command.upper()](conn, word)
            else:
                raise ValueError
        except ValueError:
            conn.send('TRASNLATEERR"Invalid Command"'.encode())
            conn.close()
        except:
            conn.close()


def run():
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((config['IP'], config['Port']))
        server.listen()
        print('Server Started')
        print(available_servers)
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

