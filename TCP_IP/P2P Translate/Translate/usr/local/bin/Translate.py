import json
import os.path
import socket
import threading
import ipaddress
from concurrent.futures import ThreadPoolExecutor
from itertools import repeat
from serverLogging import *


class NotConfigured(Exception):
    pass


def load_config() -> dict:
    """
    Loads config from json file
    :return: config as dictionary
    """
    if os.path.isfile('/usr/local/etc/cfg.json'):
        with open("/usr/local/etc/cfg.json", 'r') as f:
            return json.load(f)
    else:
        cfg = {
            "IP": "127.0.0.1",
            "Port": 65525,
            "IP_RANGE": "127.0.0.0/24",
            "PORT_RANGE": "65525-65535"
            }
        with open('/usr/local/etc/cfg.json', 'w') as f:
            json.dump(cfg, f, indent=True)
            raise NotConfigured


def get_ports():
    """
    Returns list with all ports that are in range defined in config
    """
    port_min, port_max = config['PORT_RANGE'].split('-')
    ports = list(range(int(port_min), int(port_max) + 1))
    return ports


words = {
    'range': 'rozsah',
    'car': 'auto',
    'hideout': 'úkryt',
    'loadout': 'výbava',
    'stash': 'skrýš'
}


available_servers = []
config = load_config()
ports = get_ports()


def translate_loc(conn, addr, word: str):
    """
    Finds translation for requested word in local dictionary
    """
    if word.lower() in words.keys():
        log_send(f'TRANSLATESUC"{words[word.lower()]}"', conn, addr)
    else:
        log_send('TRANSLATEERR"Unknown word"', conn, addr)


def translate_rem(conn, addr, word: str):
    """
    Finds translation for requested word in dictionaries from all available servers in defined IP range
    """
    available_servers.clear()
    find_available_servers()
    if available_servers:
        answer = None
        with ThreadPoolExecutor(max_workers=len(available_servers)) as executor:
            for result in executor.map(find_translation, available_servers, repeat(word), repeat(conn)):
                if result:
                    answer = result
            if answer:
                log_send(answer.decode(), conn, addr)
            else:
                log_send('TRANSLATEERR"Unknown word"', conn, addr)
    else:
        log_send('TRANSLATEERR"No available servers found"', conn, addr)


def translate_any(conn, addr, word: str):
    """
    Finds translation for requested word in local dictionary.
    If words wasn't found, finds translation for requested word in dictionaries from all available servers in defined IP range
    """
    if word.lower() in words.keys():
        log_send(f'TRANSLATESUC"{words[word.lower()]}"', conn, addr)
    else:
        translate_rem(conn, addr, word)


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
    client.settimeout(3)
    client.connect(server)
    msg = f'TRANSLATELOC"{word}"'
    client.send(msg.encode())
    answer = client.recv(1024)
    if 'TRANSLATESUC'.encode() in answer:
        return answer


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
    for port in ports:
        if port == config['Port'] and server == config['IP']:
            continue
        try:
            socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket_obj.settimeout(1)
            socket_obj.connect_ex((server, port))
            socket_obj.send('TRANSLATELOC"test"'.encode())
            msg = socket_obj.recv(1024).decode()
            if 'TRANSLATE' in msg:
                available_servers.append((server, port))
            socket_obj.close()
        except TimeoutError:
            pass
        except IOError:
       	    pass
        except Exception as e:
            log('Check ip ' + e.__str__())


def client_thread(conn, addr):
    """
    Used for handling client inputs
    """
    try:
        while True:
            try:
                message = conn.recv(1024).decode()
                if message == '\r\n' or message == '\r':
                    message = conn.recv(1024).decode()
                log(f'{addr[0]}:{addr[1]} -> {message}')
                command, word = message.split('"')[:-1]
                if command.upper() in commands.keys():
                    commands[command.upper()](conn, addr, word)
                else:
                    raise ValueError
            except ValueError:
                msg = 'TRASNLATEERR"Invalid Command"'
                conn.send(msg.encode())
                log(f'{addr[0]}:{addr[1]} <- {msg}')
    except OSError:
        pass
    except Exception as e:
        log('Client thread ' + e.__str__())
    finally:
        conn.close()


def run():
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((config['IP'], config['Port']))
        server.listen()
        while True:
            conn, addr = server.accept()
            log(f'{addr[0]}:{addr[1]} connected')
            t = threading.Thread(target=client_thread, args=(conn, addr))
            t.start()
    except OSError as e:
        log(e.__str__())
        log('Server stopped')
    except Exception as e:
        log('Server run ' + e.__str__())


if __name__ == '__main__':
    run()


