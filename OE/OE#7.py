
class TekkenCharacter:
    def __init__(self, name, ability): 
        self.name = name
        self.ability = ability
    def introduce(self, function):
        def wrapper():
            print("Introducing.....")
            function()
            print("This Character is amazing!!!!")
        return wrapper
charac = TekkenCharacter("Asuka", "Combo Damage")
@charac.introduce
def character_intro():
    print(f"I am {charac.name} and my ability is {charac.ability}")
character_intro()
