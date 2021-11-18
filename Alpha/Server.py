import socket
import threading

server_ip = '127.0.0.1'
port = 8888

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((server_ip, port))
server.listen()

clients = []            # List of currently connected clients
nicknames = []          # List of known client nicknames
cipher_keys = []        # List of keys for messages
messages = []           # List of tuples of messages and cipher keys for these messages
cipher_separator = ';'  # Used to separate message and cipher key in sent message


# Sends message to all connected clients
def send_to_all_clients(message, key):
    for cl in clients:
        cl.send(message + cipher_separator.encode('ascii') + key)


# Sends messages to client that just reconnected
def send_chat_history_after_reconnect(client):
    for message in messages:
        client.send(message[0] + cipher_separator.encode('ascii') + message[1])


# Receives messages from connected clients
def get_client_messages(client):
    while True:
        try:
            message = client.recv(1024)
            cipher_key = cipher_keys[clients.index(client)]
            messages.append((message, cipher_key.encode('ascii')))
            send_to_all_clients(message, cipher_key.encode('ascii'))
        except:
            client_nickname = nicknames[clients.index(client)]
            clients.remove(client)
            #nicknames.remove(client_nickname)
            send_to_all_clients((client_nickname + ' disconnected.').encode('ascii'), ''.encode('ascii'))
            print(f'{client_nickname} disconnected.')
            client.close()
            break


# Initializes server and constantly waiting for new connections
def server_start():
    while True:
        client, address = server.accept()
        print("New client connected. \nIP: " + str(address))
        client.send(('SET_NICKNAME' + cipher_separator).encode('ascii'))
        client_data = client.recv(1024).decode('ascii').split(';')
        print(client_data)
        client_nickname = client_data[0]
        cipher_key = client_data[1]
        client.send(('Connected' + cipher_separator).encode('ascii'))
        if client_nickname not in nicknames:
            nicknames.append(client_nickname)
            clients.append(client)
            cipher_keys.append(cipher_key)
        else:
            clients.insert(cipher_keys.index(cipher_key), client)
            send_chat_history_after_reconnect(client)
        print("Nickname: " + client_nickname)
        send_to_all_clients(f"{client_nickname} joined chat!".encode('ascii'), ''.encode('ascii'))
        new_thread = threading.Thread(target=get_client_messages, args=(client,))
        new_thread.start()


server_start()
