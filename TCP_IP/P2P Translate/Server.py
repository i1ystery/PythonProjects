import json
import os.path
import socket
import threading
import ipaddress
from concurrent.futures import ThreadPoolExecutor
from itertools import repeat


class NotConfigured(Exception):
    pass


def load_config() -> dict:
    """
    Loads config from json file
    :return: config as dictionary
    """
    if os.path.isfile('config.json'):
        with open("config.json", 'r') as f:
            return json.load(f)
    else:
        cfg = {
            "IP": "127.0.0.1",
            "Port": 65525,
            "IP_RANGE": "10.2.0.0/16",
            "PORT_RANGE": "65525-65535"
            }
        with open('config.json', 'w') as f:
            json.dump(cfg, f, indent=True)
            raise NotConfigured


def log(message: str):
    with open("server_log.txt", 'a') as f:
        f.write(message + '\n')


# def log_send(conn, message: str):
#     conn.send(message)
#     log()


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
    """
    Finds translation for requested word in local dictionary
    """
    if word.lower() in words.keys():
        conn.send(f'TRANSLATESUC"{words[word.lower()]}"'.encode())
    else:
        conn.send('TRANSLATEERR"Unknown word"'.encode())


def translate_rem(conn, word: str):
    """
    Finds translation for requested word in dictionaries from all available servers in defined IP range
    """
    find_available_servers()
    if available_servers:
        with ThreadPoolExecutor(max_workers=len(available_servers)) as executor:
            executor.map(find_translation, available_servers, repeat(word), repeat(conn))
    else:
        conn.send('TRANSLATEERR"No available servers found"')


def translate_any(conn, word: str):
    """
    Finds translation for requested word in local dictionary.
    If words wasn't found, finds translation for requested word in dictionaries from all available servers in defined IP range
    """
    if word.lower() in words.keys():
        conn.send(f'TRANSLATESUC"{words[word.lower()]}"'.encode())
    else:
        #conn.send('TRANSLATEERR"Unknown word"'.encode())
        translate_rem(conn, word)


commands = {
    'TRANSLATELOC': translate_loc,
    'TRANSLATEREM': translate_rem,
    'TRANSLATEANY': translate_any,
}


def find_translation(server, word: str, conn):
    """
    Used to connect to defined server and request translation for a word
    """
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(3)
    client.connect(server)
    msg = f'TRANSLATELOC"{word}"'
    client.send(msg.encode())
    log(f'{server[0]}:{server[1]} -> {msg}')
    answer = client.recv(1024)
    log(f'{server[0]}:{server[1]} <- {answer.decode()}')
    conn.send(answer)


def find_available_servers():
    """
    Finds available servers in defined IP range
    """
    all_servers = [str(ip) for ip in ipaddress.IPv4Network(config['IP_RANGE'])][1:-1]  # All possible server IP's excluding Network address and Broadcast address
    with ThreadPoolExecutor(max_workers=len(all_servers)) as executor:
        executor.map(check_ip, all_servers)


def check_ip(server):
    """
    Used for checking IP with every port from port range.
    If server responds adds it to available server list.
    :param server: IP
    """
    socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.01)
    try:
        if server == config['IP']:
            raise
        port_min, port_max = config['PORT_RANGE'].split('-')
        ports = range(int(port_min), int(port_max) + 1)
        for port in ports:
            socket_obj.connect_ex((server, port))
            socket_obj.send('TRANSLATELOC"asdasdasd"'.encode())
            msg = socket_obj.recv(1024).decode()
            if 'TRANSLATE' in msg:
                available_servers.append((server, port))
    except TimeoutError:
        pass
    except Exception as e:
        log(e.__str__())
    finally:
        socket_obj.close()


def client_thread(conn, addr):
    """
    Used for handling client inputs
    """
    try:
        message = conn.recv(1024).decode()
        log(f'{addr[0]}:{addr[1]} -> {message}')
        if message == '\r\n' or message == '\r':
            message = conn.recv(1024).decode()
        command, word = message.split('"')[:-1]
        if command.upper() in commands.keys():
            commands[command.upper()](conn, word)
        else:
            raise ValueError
    except ValueError:
        msg = 'TRASNLATEERR"Invalid Command"'
        conn.send(msg.encode())
        log(f'{addr[0]}:{addr[1]} <- {msg}')
    except Exception as e:
        log(e.__str__())
    finally:
        conn.close()


def run():
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((config['IP'], config['Port']))
        server.listen()
        while True:
            conn, addr = server.accept()
            log(addr[0] + " connected")
            t = threading.Thread(target=client_thread, args=(conn, addr))
            t.start()
    except OSError as e:
        log(e.__str__())
        log('Server stopped')
    except Exception as e:
        log(e.__str__())


if __name__ == '__main__':
    run()


