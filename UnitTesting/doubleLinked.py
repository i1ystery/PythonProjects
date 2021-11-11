class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None

    def insert_last(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.last_node = new_node
            return
        last_node = self.last_node
        self.last_node.next = new_node
        new_node.prev = last_node
        self.last_node = new_node

    def get_last_node(self):
        last_node = self.head
        while last_node.next is not None:
            last_node = last_node.next
        return last_node

    def print_next(self):
        head = self.head
        while head is not None:
            print(head.data)
            head = head.next

    def print_prev(self):
        last = self.get_last_node()
        while last is not None:
            print(last.data)
            last = last.prev

    def count_same_values(self, value):
        start_next_node = self.head
        counter = 0
        while start_next_node.next != None:
            if start_next_node.data == value:
                counter += 1
            start_next_node = start_next_node.next
        return counter

    def __iter__(self):
        return self

    def __next__(self):
        if not self.head:
            raise StopIteration
        else:
            item = self.head
            self.head = self.head.next
            return item.data
