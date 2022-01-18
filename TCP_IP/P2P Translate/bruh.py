import socket

if __name__ == '__main__':
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('192.168.43.21', 65525))
    while True:
        try:
            received_message = client.recv(1024).decode('utf-8')
            print(received_message)
            sent_text = input("")
            client.send(sent_text.encode('utf-8'))
        except:
            print('Lost connection to the server')
            client.close()
            break
