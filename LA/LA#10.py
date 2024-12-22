class Vehicle:
    def __init__(self, brand, model, fuel_type):
        self.brand = brand
        self.model = model
        self.fuel_type = fuel_type
    def describeVehicle(self):
         print (f"This Vehicle is a {self.brand} brand, {self.model} model and {self.fuel_type} fuel type")
class Car(Vehicle):
    pass
class Motor(Vehicle):
    pass
car = Car("Hellcats", "Dodge Charger SRT", "Gasoline")
motor = Motor("Honda", "Click125i", "Gasoline")
car.describeVehicle()
motor.describeVehicle()