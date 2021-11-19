import re


class IkeaItem:
    def __init__(self, rack_number, row, name, price):
        assert 0 > rack_number < 100
        assert re.match(r'[A-K]', row) is not None
        assert type(name) == str and len(name) > 1
        assert price > 0
        self.rack_number = rack_number
        self.row = row
        self.name = name
        self.price = price


class MeasurableIkeaItem:
    def __init__(self, height, width):
        assert height > 0 and width > 0
        self.height = height
        self.width = width


class PlasticWasteIkeaItem:
    def __init__(self, plastic_mass):
        assert plastic_mass > 0
        self.plastic_mass = plastic_mass


class Lack(IkeaItem, MeasurableIkeaItem):
    def __init__(self, rack_number, row, name, price, color, height, width):
        IkeaItem.__init__(self, rack_number, row, name, price)
        MeasurableIkeaItem.__init__(self, height, width)
        assert type(color) == str and len(color) > 1
        self.color = color


class SamlaBox(IkeaItem, MeasurableIkeaItem, PlasticWasteIkeaItem):
    def __init__(self, rack_number, row, name, price, volume, height, width, plastic_mass):
        IkeaItem.__init__(self, rack_number, row, name, price)
        MeasurableIkeaItem.__init__(self, height, width)
        PlasticWasteIkeaItem.__init__(self, plastic_mass)
        assert volume > 0
        self.volume = volume


class Sjorapport(IkeaItem, PlasticWasteIkeaItem):
    def __init__(self, rack_number, row, name, price, exp_date, mass, plastic_mass):
        IkeaItem.__init__(self, rack_number, row, name, price)
        PlasticWasteIkeaItem.__init__(self, plastic_mass)
        assert type(exp_date) == str and len(exp_date) > 1
        assert mass > 0
        self.exp_date = exp_date
        self.mass = mass

