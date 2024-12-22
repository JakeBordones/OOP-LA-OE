class AnimeCharacter:
    def __init__(self, name, ability):
        self.name = name
        self.ability = ability

    def introduce(self, func):
        def wrapper_method():
            print("Introducing...")
            func()
            print("This character is amazing!")
        return wrapper_method
    
anime = AnimeCharacter("Meliodas","Full Counter")

@anime.introduce
def character_intro():
    print(f"I am {anime.name} and I can use {anime.ability}")

character_intro()