import datetime
import random
import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IP_address = '127.0.0.1'
Port = 8888
server.bind((IP_address, Port))
server.listen()
list_of_clients = []
client_chat_history = {

}
online = True
quotes = ['"People, who can’t throw something important away, can never hope to change anything." – Armin Arlert',
          '“If you don’t take risks, you can’t create a future!” – Monkey D. Luffy',
          '“Why should I apologize for being a monster? Has anyone ever apologized for turning me into one?” – Juuzou Suzuya',
          '“Life and death are like light and shadow. They’re both always there. But people don’t like thinking about death, so subconsciously, they always look away from it." – Yato'
          ]


def quote(client):
    client.send(random.choice(quotes).encode('utf-8'))


def date(client):
    client.send(datetime.datetime.now().strftime('%Y-%m-%d').encode('utf-8'))


def help_command(client):
    help_cmds = ", ".join(list(commands.keys()))
    client.send(help_cmds.encode('utf-8'))


def ohm(client):
    client.send('Enter I,U or R in SI base units'.encode('utf-8'))
    values = {
        'I': None,
        'U': None,
        'R': None
    }
    data = 0
    while data < 2:
        try:
            msg = receive_message(client)
            name, value = msg.split('=')
            name = name.upper().strip()
            if name in values.keys():
                if values[name]:
                    client.send('This value is already set.'.encode('utf-8'))
                else:
                    values[name] = float(value)
                    data += 1
                    client.send('OK'.encode('utf-8'))
            else:
                client.send('Invalid Data'.encode('utf-8'))
        except:
            client.send('Invalid Data'.encode('utf-8'))
            continue

    while True:
        action = receive_message(client)
        if action.lower() == 'calculate i' and values['U'] is not None and values['R'] is not None:
            result = values['U'] / values['R']
            client.send(str(result).encode('utf-8'))
            break
        elif action.lower() == 'calculate u' and values['I'] is not None and values['R'] is not None:
            result = values['I'] * values['R']
            client.send(str(result).encode('utf-8'))
            break
        elif action.lower() == 'calculate r' and values['I'] is not None and values['U'] is not None:
            result = values['U'] / values['I']
            client.send(str(result).encode('utf-8'))
            break
        else:
            client.send('Invalid command'.encode('utf-8'))


def stop(client):
    broadcast('Stopping server...', None)
    global online
    online = False
    server.close()


def broadcast(msg, connection):
    for clients in list_of_clients:
        if clients != connection:
            try:
                clients.send(msg.encode('utf-8'))
            except:
                clients.close()
                remove(clients)


def history(client):
    history = '\n'.join(client_chat_history[client])
    client.send(history.encode('utf-8'))


commands = {
    'QUOTE': quote,
    'DATE': date,
    'HELP': help_command,
    'OHM': ohm,
    'STOP': stop,
    'HISTORY': history
}


def client_thread(conn, addr):
    conn.send("Welcome to this chatroom!".encode('utf-8'))
    client_chat_history[conn] = []
    while True:
        try:
            global online
            if online:
                message = receive_message(conn)
                if message.upper() in commands.keys():
                    commands[message.upper()](conn)
                else:
                    conn.send('Invalid command'.encode('utf-8'))
            else:
                break
        except Exception as e:
            print(e)
            remove(conn)
            break


def receive_message(client):
    m = client.recv(2048).decode('utf-8')
    client_chat_history[client].append(m)
    return m


def remove(connection):
    if connection in list_of_clients:
        list_of_clients.remove(connection)


def run():
    try:
        while online:
            conn, addr = server.accept()
            list_of_clients.append(conn)
            print(addr[0] + " connected")
            t = threading.Thread(target=client_thread, args=(conn, addr))
            t.daemon = True
            t.start()
    except OSError:
        print('Server stopped')
    except Exception as e:
        print(e)


if __name__ == '__main__':
    run()


