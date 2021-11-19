import socket
import threading
import time

server_ip = '127.0.0.1'
port = 8888

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((server_ip, port))
server.listen()

clients = []                               # List of currently connected clients
nicknames = []                             # List of known client nicknames
cipher_keys = []                           # List of keys for messages
messages = []                              # List of tuples of messages and cipher keys for these messages
cipher_separator = chr(1).encode('ascii')  # Used to separate message and cipher key in sent message


def send_to_all_clients(message, key):
    """
    Sends message to all connected clients
    :param message: byte
    :param key: byte decryption key for message
    """
    for cl in clients:
        cl.send(message + cipher_separator + key)


def send_chat_history_after_reconnect(client):
    """
    Sends messages to client that just reconnected
    :param client: client that should receive message history
    """
    for message in messages:
        client.send(message[0] + cipher_separator + message[1])
        time.sleep(0.2)



def get_client_messages(client):
    """
    Used in thread to constantly receive messages from defined client
    :param client: client
    """
    while True:
        try:
            message = client.recv(1024)
            cipher_key = cipher_keys[clients.index(client)]
            message_with_key = (message, cipher_key.encode('ascii'))
            messages.append(message_with_key)
            send_to_all_clients(message, cipher_key.encode('ascii'))
        except:
            client_nickname = nicknames[clients.index(client)]
            clients.remove(client)
            send_to_all_clients((client_nickname + ' disconnected.').encode('ascii'), ''.encode('ascii'))
            print(f'{client_nickname} disconnected.')
            client.close()
            break


def server_start():
    # Initializes server and constantly waiting for new connections
    while True:
        client, address = server.accept()
        print("New client connected. \nIP: " + str(address))
        client.send(('SET_NICKNAME'.encode('ascii')))
        client_data = client.recv(1024).decode('ascii')
        client_nickname = client_data
        if client_nickname not in nicknames:
            nicknames.append(client_nickname)
            clients.append(client)
        else:
            clients.insert(nicknames.index(client_nickname), client)
            send_chat_history_after_reconnect(client)
        print("Nickname: " + client_nickname)
        send_to_all_clients(f"{client_nickname} joined chat!".encode('ascii'))
        new_thread = threading.Thread(target=get_client_messages, args=(client,))
        new_thread.start()


if __name__ == '__main__':
    server_start()
