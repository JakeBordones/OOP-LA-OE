class Phone:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def descibePhone(self):
        print (f"The {self.brand} phone brand has a {self.model} phone model")

class Android(Phone):
    def __init__(self, brand, model):
         Phone.__init__(self, brand, model)
         
phone = Android("Realme", "Realme7")
phone.descibePhone()