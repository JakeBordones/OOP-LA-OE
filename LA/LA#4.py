class ML_Heroes():
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def __str__(self):
        return f"{self.name} is a {self.role} hero"

mm1 = ML_Heroes("Thamuz", "Fighter") 
print(mm1)