import socket


class Client:
    def __init__(self, ip, port):
        self.cl = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = (ip, port)

    def execute_command(self, command):
        self.cl.connect(self.server)
        self.cl.send(command.encode())
        answer = self.cl.recv(1024)
        return answer

