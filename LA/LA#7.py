class Car:
    def __init__(self, brand):
        self.brand = brand

Hellcats = Car("Model: Hellcats")
print(Hellcats.brand)
Hellcats.color = "Color: Black"
print(Hellcats.color)
Hellcats.color = "Updated Color: Gray"
print(Hellcats.color)