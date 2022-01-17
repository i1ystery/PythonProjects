import socket

if __name__ == '__main__':
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 8888))
    while True:
        try:
            received_message = client.recv(2048).decode('utf-8')
            print(received_message)
            sent_text = input("")
            if len(sent_text) > 0:
                client.send(sent_text.encode('utf-8'))
        except:
            print('Lost connection to the server')
            client.close()
            break
