class Command:
    def __init__(self, command_name: str, function):
        self.name = command_name
        self.func = function

    def execute(self, client):
        self.func(client)