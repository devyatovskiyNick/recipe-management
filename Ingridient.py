class Ingredient:
    def __init__(self, name:str, quantity:float, unit:str):
        self.name = name
        self.quantity = quantity
        self.unit = unit

    @property
    def quantity(self, val):
        pass


    def __str__(self):
        pass

    def __repr__(self):
        pass

    def __eq__(self, other):
        pass