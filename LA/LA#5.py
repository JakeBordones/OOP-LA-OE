class Hero:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def description(self):
        return f"{self.name} is a {self.role} hero."

hero = Hero("Moskov", "Marksman")
print(hero.description())
