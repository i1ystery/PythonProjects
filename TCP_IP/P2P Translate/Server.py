import socket
import threading

online = True
config = {
    'IP': '10.2.3.98',
    'Port': 65525,
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


def translate_loc(conn, word: str) -> str:
    if word.lower() in words.keys():
        return f'TRANSLATESUC"{words[word.lower()]}"'
    else:
        return 'TRANSLATEERR"Unknown word"'


commands = {
    'TRANSLATELOC': translate_loc,
    #'TRANSLATEREM': translaterem,
    #'TRANSLATEANY': translateany
}


def client_thread(conn, addr):
    conn.send(f"Welcome to this chatroom! Your ip address is: {addr}".encode('utf-8'))
    while True:
        try:
            global online
            if online:
                message = conn.recv(1024).decode('utf-8')
                conn.recv(1024)
                command, word = message.split('"')[:-1]
                if command.upper() in commands.keys():
                    translated = commands[command.upper()](conn, word)
                    conn.send(translated.encode('utf-8'))
                else:
                    conn.send('Invalid command'.encode('utf-8'))
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


