class Hero:
    def __init__(self, name, role, damage_type):
        self.name = name
        self.role = role
        self.damage_type = damage_type
    
    def __string__(self):
        return f"{self.name} is a hero {self.role} and {self.damage_type} damage type"
    
mm1 = Hero("Khufra", "Tank", "Physical")
mm2 = Hero("Claude", "Marksman", "Physical")
mm3 = Hero("Phoveus", "Fighter", "Physical")
mm4 = Hero("Aurora", "Mage", "Magic")
mm5 = Hero("Ling", "Assasin", "Physical")
print("Hero#1")
print("Hero name: " + mm1.name)
print("Hero role: " + mm1.role)
print("Hero damage type: " + mm1.damage_type)
print("")
print("Hero#2")
print("Hero name: " + mm2.name)
print("Hero role: " + mm2.role)
print("Hero damage type: " + mm2.damage_type)
print("")
print("Hero#3")
print("Hero name: " + mm3.name)
print("Hero role: " + mm3.role)
print("Hero damage type: " + mm3.damage_type)
print("")
print("Hero#4")
print("Hero name: " + mm4.name)
print("Hero role: " + mm4.role)
print("Hero damage type: " + mm4.damage_type)
print("")
print("Hero#5")
print("Hero name: " + mm5.name)
print("Hero role: " + mm5.role)
print("Hero damage type: " + mm5.damage_type)
print("")