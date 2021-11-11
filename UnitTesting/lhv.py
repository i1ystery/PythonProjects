class CapacityException(Exception):
    pass
class BottleClosedException(Exception):
    pass
class FillException(Exception):
    pass

class Lahev:
    def __init__(self):
        self.capacity = None
        self.amount = None
        self.is_closed = False

    def set_capacity(self, capacity):
        if capacity > 0:
            self.capacity = capacity
            return 'Capacity is now ' + str(capacity) + ' l'
        else:
            raise CapacityException("Capacity can't be 0 or lower than 0")

    def set_amount(self, amount):
        if amount <= self.capacity and not self.is_closed and amount >= 0:
            self.amount = amount
            return 'Liquid amount in bottle is ' + str(amount) + ' l'
        elif self.is_closed:
            raise BottleClosedException("You can't fill bottle when it's closed")
        elif amount >= self.capacity or amount < 0:
            raise FillException("You can't put more liquid than bottle can hold")

    def clr_amount(self):
        if not self.is_closed:
            self.amount = 0
            return'Bottle is now empty'
        else:
            raise BottleClosedException("You can't empty bottle when it's closed")

    def set_amount_ml(self, amount):
        if not self.is_closed and amount / 1000 <= self.capacity and amount >= 0:
            self.amount = amount / 1000
            return 'Bottle was filled with ' + str(amount) + ' ml'
        elif self.is_closed:
            raise BottleClosedException("You can't fill bottle when it's closed")
        elif self.capacity <= amount or amount < 0:
            raise FillException("You can't put more liquid than bottle can hold")

    def get_amount_ml(self):
        return self.amount * 1000

    def close(self):
        self.is_closed = True
        return 'Bottle is now closed'

    def open(self):
        self.is_closed = False
        return 'Bottle is now open'

    def bottleToString(self):
        return f"Bottle capacity is {self.capacity} l, liquid amount in bottle: {self.amount} l."
