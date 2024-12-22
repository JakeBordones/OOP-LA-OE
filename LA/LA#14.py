class Spiderman:
    def __init__(self, name, age):
        self.name = name.lower()
        self.age = age
    def describeSpiderman(self):
        print(f"Name: {self.name} Age: {self.age} ")

class Gwen(Spiderman):
    def __init__(self, name, age, movietitle):
        super().__init__(name, age)
        self.movietitle = movietitle

class Venom(Spiderman):
    def __init__(self, name, age, movietitle):
        super().__init__(name, age)
        self.movietitle = movietitle

class Tom(Spiderman):
    def __init__(self, name, age, movietitle):
        super().__init__(name, age)
        self.movietitle = movietitle

gwens = Gwen("Gwen", 26, "Spider-Man")
venoms = Venom("Eddie", 41, "The Amazing Spider-Man")
stom = Tom("Tom", 28, "Homecoming")

print(gwens.describeSpiderman(), gwens.movietitle.upper())
print(venoms.describeSpiderman(), venoms.movietitle.upper())
print(stom.describeSpiderman(), stom.movietitle.upper())
