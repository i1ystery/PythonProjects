import socket
import threading
from string import ascii_uppercase, ascii_lowercase
from tika import parser
from zipfile import ZipFile
from requests import get as requests_get
from io import BytesIO
from os import remove, rmdir


def generate_key():
    """
    Generates cipher key from pdf file.
    :return: cipher key as string
    """
    url = "https://docs.python.org/3/archives/python-3.10.0-docs-pdf-a4.zip"
    r = requests_get(url)
    with ZipFile(BytesIO(r.content), 'r') as zip:
        zip.extract('docs-pdf/c-api.pdf')
    raw = parser.from_file('docs-pdf/c-api.pdf')
    cipher_key = ''.join(filter(str.isalpha, raw['content']))
    remove("docs-pdf/c-api.pdf")
    rmdir("docs-pdf")
    return cipher_key


class ClientVariables:
    """
    Class used to store unsent message and cipher key
    """
    unsent_message = None
    key = generate_key()


def decrypt(message: str):
    """
    Decrypts encrypted message from other clients using Vigenere cipher.
    :param message: str encrypted message from server
    :return: decrypted message as str
    """
    decrypted_message = []
    index = 0
    for letter in message:
        if letter in ascii_uppercase:
            x = (ord(letter) - ord(ClientVariables.key[index].upper()) + 26) % 26
            x += ord('A')
            decrypted_message.append(chr(x))
            index += 1
        elif letter in ascii_lowercase:
            x = (ord(letter) - ord(ClientVariables.key[index].lower()) + 26) % 26
            x += ord('a')
            decrypted_message.append(chr(x))
            index += 1
        else:
            decrypted_message.append(letter)
    return "".join(decrypted_message)


def encrypt(message: str):
    """
    Encrypts user's message using Vigenere cipher.
    :param message: str user input message
    :return: encrypted user message as str
    """
    encrypted_text = []
    index = 0
    for letter in message:
        if letter in ascii_uppercase:
            x = (ord(letter) - 65 + ord(ClientVariables.key[index].upper()) - 65) % 26
            x += ord('A')
            encrypted_text.append(chr(x))
            index += 1
        elif letter in ascii_lowercase:
            x = (ord(letter) - 97 + ord(ClientVariables.key[index].lower()) - 97) % 26
            x += ord('a')
            encrypted_text.append(chr(x))
            index += 1
        else:
            encrypted_text.append(letter)
    return "".join(encrypted_text)


def get_messages_from_server():
    """
    Receives messages from the server.
    """
    online = True
    while online:
        try:
            received_message = client.recv(1024).decode('ascii')
            # Server messages are not encrypted/Client messages
            if received_message == 'SET_NICKNAME':
                client.send((nickname.encode('ascii')))
            elif 'SERVER_MESSAGE >' in received_message:
                print(received_message)
            else:
                message = decrypt(received_message)
                print(message)

        except Exception as e:
            print(e)
            client.close()
            online = False


def send_message():
    """
    Sends message to the server.
    """
    online = True
    while online:
        message = None
        try:
            if ClientVariables.unsent_message is not None:
                message = ClientVariables.unsent_message
                client.send(message.encode('ascii'))
                ClientVariables.unsent_message = None
            else:
                sent_text = input("")
                message = f'{nickname} > {sent_text}'
                message = encrypt(message)
                # Testing if
                if sent_text == 'reconnect':
                    client.close()
                # Testing if end
                if len(sent_text) > 0:
                    client.send(message.encode('ascii'))
        except Exception as e:
            print(e)
            ClientVariables.unsent_message = message
            online = False


if __name__ == '__main__':
    nickname = input("Enter your nickname: ")
    assert len(nickname) > 2
    reconnect = True
    while True:
        if reconnect:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect(('127.0.0.1', 8888))
            receive_message_thread = threading.Thread(target=get_messages_from_server)
            send_message_thread = threading.Thread(target=send_message)
            receive_message_thread.start()
            send_message_thread.start()
            reconnect = False
        threads_running = receive_message_thread.is_alive() or send_message_thread.is_alive()
        if not threads_running:
            print('Connection lost. Reconnecting..')
            reconnect = True
