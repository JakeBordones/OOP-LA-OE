class VideoGameCharacter:
    def __init__(self, name, health, level, attack_power):
        self.name = name
        self.health = health
        self.level = level
        self.attack_power = attack_power

    def attack(self):
        print(f"{self.name} attacks with power {self.attack_power}")

    def tintin(self):
        self.attack()

class Fighter(VideoGameCharacter):
    def __init__(self, name, health, level, weapon):
        super().__init__(name, health, level, 0)
        self.weapon = weapon

    def special_move(self):
        self.attack_power = (self.level * 5) * 3

    def tintin(self):
        self.special_move()
        super().tintin()

class Mage(VideoGameCharacter):
    def __init__(self, name, health, level, spell):
        super().__init__(name, health, level, 0)
        self.spell = spell

    def cast_spell(self):
        self.attack_power = (self.level * 5) * 2

    def tintin(self):
        self.cast_spell()
        super().tintin()


mario = VideoGameCharacter("Mario", 100, 5, 25)
ryu = Fighter("Ryu", 150, 7, "Shoryuken")
gandalf = Mage("Gandalf", 80, 6, "Fireball")


print(f"Video Game Character: {mario.name}")
print(f"Health: {mario.health}")
print(f"Level: {mario.level}")
print(f"{mario.name} attacks with power {mario.attack_power}")
print()

print(f"Fighter: {ryu.name}")
print(f"Health: {ryu.health}")
print(f"Level: {ryu.level}")
print(f"Weapon: {ryu.weapon}")
ryu.special_move()
print(f"{ryu.name} uses {ryu.weapon}, attacking with power: {ryu.attack_power}")
print()

print(f"Video Game Character: {gandalf.name}")
print(f"Health: {gandalf.health}")
print(f"Level: {gandalf.level}")
print(f"Spell: {gandalf.spell}")
gandalf.cast_spell()
print(f"{gandalf.name} attacks with power {gandalf.attack_power}")
print()


for character in (mario, ryu, gandalf):
    character.tintin()