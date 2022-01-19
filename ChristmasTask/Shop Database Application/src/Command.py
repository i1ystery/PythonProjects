from typing import Callable


class Command:
    def __init__(self, command_name: str, method_to_execute: Callable):
        self.command_name = command_name
        self.method = method_to_execute
