class ML_Heroes():
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def story(self):
        return f"{self.name} is a {self.role} hero"

mm1 = ML_Heroes("Thamuz", "Fighter") 
print("Heroe name: " + mm1.name)
print("Heroe role: " + mm1.role)
print(mm1.story())