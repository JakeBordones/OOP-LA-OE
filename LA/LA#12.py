class Toy:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def describeToy(self):
        print (f"The {self.name} toy cost {self.price} pesos")

class Car(Toy):
    def __init__(self, name, price):
        super().__init__(self, name, price)

Car = Toy("Meliodas", 750)
Car.describeToy()