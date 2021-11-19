import socket
import threading
import sys
from string import ascii_uppercase, ascii_lowercase


class Messages:
    unsent_message = None


def generate_key(message, keyword):
    """
    Generates cipher key with the same length as message using original cipher key
    :param message: str message that we want generate key for
    :param keyword: str original cipher key
    :return: str cipher key with the same length as message
    """
    if len(keyword) == len(message):
        return keyword
    elif len(keyword) > len(message):
        return keyword[0:len(message)]
    else:
        while len(keyword) < len(message):
            keyword = keyword * 2
        return keyword[0:len(message)]


def decrypt(message, keyword):
    """
    Decrypts encrypted message from other clients using Vigenere cipher
    :param message: str encrypted message from server
    :param keyword: str decrypt key from server
    :return: str decrypted message
    """
    decrypted_message = []
    index = 0
    key = generate_key(message, keyword)
    for letter in message:
        if letter in ascii_uppercase:
            x = (ord(letter) -
                 ord(key[index].upper()) + 26) % 26
            x += ord('A')
            decrypted_message.append(chr(x))
            index += 1
        elif letter in ascii_lowercase:
            x = (ord(letter) -
                 ord(key[index]) + 26) % 26
            x += ord('a')
            decrypted_message.append(chr(x))
            index += 1
        else:
            decrypted_message.append(letter)
    return "".join(decrypted_message)


def encrypt(message, keyword):
    """
    Encrypts user's message using Vigenere cipher
    :param message: str user input message
    :param keyword: str user input encryption key
    :return: str encrypted user message
    """
    cipher_text = []
    index = 0
    key = generate_key(message, keyword)
    for letter in message:
        if letter in ascii_uppercase:
            x = (ord(letter) - 65 +
                 ord(key[index].upper()) - 65) % 26
            x += ord('A')
            cipher_text.append(chr(x))
            index += 1
        elif letter in ascii_lowercase:
            x = (ord(letter) - 97 +
                 ord(key[index]) - 97) % 26
            x += ord('a')
            cipher_text.append(chr(x))
            index += 1
        else:
            cipher_text.append(letter)
    return "".join(cipher_text)


def get_messages_from_server():
    # Used to receive messages from other clients
    # cipher_separator used to split received message from server to message and decrypt key
    cipher_separator = chr(1)
    online = True
    while online:
        try:
            encrypted_message = client.recv(1024).decode('ascii')
            received_message = encrypted_message.split(cipher_separator)
            message = received_message[0]
            decrypt_key = received_message[1]
            # Decrypts message from other client
            if decrypt_key != '':
                message = decrypt(message, decrypt_key)
            # Server messages are not encrypted
            elif decrypt_key == '':
                message = message
            else:
                message = ''

            if message == 'SET_NICKNAME':
                client.send((nickname + cipher_separator + cipher_key).encode('ascii'))
            else:
                print(message)

        except Exception as e:
            print(e)
            client.close()
            online = False


def send_message():
    # Method used for sending messages
    online = True
    while online:
        message = None
        try:
            if Messages.unsent_message is not None:
                message = Messages.unsent_message
                client.send(message.encode('ascii'))
                Messages.unsent_message = None
            else:
                sent_text = input("")
                message = f'{nickname} > {sent_text}'
                message = encrypt(message, cipher_key)
                if sent_text == 'stop':
                    client.close()
                if len(sent_text) > 0:
                    client.send(message.encode('ascii'))
                #
        except Exception as e:
            print(e)
            Messages.unsent_message = message
            online = False


if __name__ == '__main__':
    nickname = input("Enter your nickname: ")
    cipher_key = input("Enter key for cipher(min. 3 characters long): ")
    assert len(cipher_key) > 2
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
