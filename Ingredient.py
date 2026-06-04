class Ingredient:
    def __init__(self, name:str, quantity:float, unit:str):
        self.name = name
        self.quantity = quantity
        self.unit = unit

    @property
    def quantity(self, val):
        pass


    def __str__(self):
        return f"{self.name}: {self.quantity} {self.unit}"

    def __repr__(self):
        return f"Ingredient('{self.name}', {self.quantity}, '{self.unit}')"

    def __eq__(self, other):
        if self.name == other.name and self.unit == other.unit:
            return True
        else:
            return False