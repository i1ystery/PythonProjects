import socket
import threading


def get_messages_from_server():
    while True:
        try:
            received_message = client.recv(2048).decode('utf-8')
            print(received_message)
        except:
            print('Lost connection to the server')
            client.close()
            break


def send_message():
    while True:

        try:
            sent_text = input("")
            if len(sent_text) > 0:
                client.send(sent_text.encode('utf-8'))
        except:
            print('Lost connection to the server')
            client.close()
            break


if __name__ == '__main__':
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 8888))
    receive_message_thread = threading.Thread(target=get_messages_from_server)
    send_message_thread = threading.Thread(target=send_message)
    receive_message_thread.start()
    send_message_thread.start()
