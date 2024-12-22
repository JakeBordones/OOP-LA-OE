class Animal:
    def __init__(self, name, type):
        pass

class Fish(Animal):
    def __init__(self, name, type):
        super().__init__(name, type)
        self.name = name
        self.type = type
        self.can_swim = True

    def describeFish(self):
        print (f"The fish name is {self.name}, he's type of {self.type} and he can swim {self.can_swim}")

fish = Fish("Nemo", "Clownfish")
fish.describeFish()