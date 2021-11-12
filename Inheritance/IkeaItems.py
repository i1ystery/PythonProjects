class IkeaItem:
    def __init__(self, rack_number, row, name, price):
        self.rack_number = rack_number
        self.row = row
        self.name = name
        self.price = price


class MeasurableIkeaItem:
    def __init__(self, height, width):
        self.height = height
        self.width = width


class PlasticWasteIkeaItem:
    def __init__(self, plastic_mass):
        self.plastic_mass = plastic_mass


class Lack(IkeaItem, MeasurableIkeaItem):
    def __init__(self, rack_number, row, name, price, color, height, width):
        IkeaItem.__init__(self, rack_number, row, name, price)
        MeasurableIkeaItem.__init__(self, height, width)
        self.color = color


class SamlaBox(IkeaItem, MeasurableIkeaItem, PlasticWasteIkeaItem):
    def __init__(self, rack_number, row, name, price, volume, height, width, plastic_mass):
        IkeaItem.__init__(self, rack_number, row, name, price)
        MeasurableIkeaItem.__init__(self, height, width)
        PlasticWasteIkeaItem.__init__(self, plastic_mass)
        self.volume = volume


class Sjorapport(IkeaItem, PlasticWasteIkeaItem):
    def __init__(self, rack_number, row, name, price, exp_date, mass, plastic_mass):
        IkeaItem.__init__(self, rack_number, row, name, price)
        PlasticWasteIkeaItem.__init__(self, plastic_mass)
        self.exp_date = exp_date
        self.mass = mass

