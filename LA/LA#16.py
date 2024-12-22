class Appliance:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def operate(self):
        print("Operating!!!!!")
    def info(self):
        print(f"Brand: {self.brand}, Model: {self.model}")

class WashingMachine(Appliance):
    def operate(self):
        print(f"Washing clothes!")

class Refrigerator(Appliance):
    def operate(self):
        print(f"Keeping Food cold!")

class Microwave(Appliance):
    def operate(self):
        print(f"Heating food!")

samsung = WashingMachine("SAMSUNG", "wa50r5200aw")
lg = Refrigerator("LG", "lrflc2706s")
panasonic = Microwave("Panasonic", "nn-cf778s")

for char in [samsung, lg, panasonic]:
    char.operate()
    char.info()
