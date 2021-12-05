import socket
import threading
from time import sleep

server_ip = '127.0.0.1'
port = 8888

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((server_ip, port))
server.listen()

clients = []    # List of currently connected clients
nicknames = []  # List of known client nicknames
messages = []   # List of tuples of messages


def send_to_all_clients(message):
    """
    Sends message to all connected clients
    :param message: byte
    """
    for cl in clients:
        cl.send(message)


def send_chat_history_after_reconnect(client):
    """
    Sends messages to client that just reconnected
    :param client: client that should receive message history
    """
    for message in messages:
        client.send(message)
        sleep(0.2)


def get_client_messages(client):
    """
    Used in thread to constantly receive messages from defined client
    :param client: client that the server getting messages from
    """
    while True:
        try:
            message = client.recv(1024)
            messages.append(message)
            send_to_all_clients(message)
        except:
            client_nickname = nicknames[clients.index(client)]
            clients.remove(client)
            send_to_all_clients(('SERVER_MESSAGE > ' + client_nickname + ' disconnected.').encode('ascii'))
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
        send_to_all_clients(f"SERVER_MESSAGE > {client_nickname} joined chat!".encode('ascii'))
        new_thread = threading.Thread(target=get_client_messages, args=(client,))
        new_thread.start()


if __name__ == '__main__':
    server_start()
