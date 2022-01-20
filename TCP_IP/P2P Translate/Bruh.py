import socket

if __name__ == '__main__':
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('10.2.5.186', 65525))
    while True:
        try:
            received_message = client.recv(1024).decode()
            print(received_message)
            sent_text = input("")
            if len(sent_text) > 0:
                client.send(sent_text.encode())
        except:
            print('Lost connection to the server')
            client.close()
            break
