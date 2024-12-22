class Favorite_food:
    def __init__(self, dish, ingredient1, ingredient2, ingredient3):
        self.__dish = dish
        self.__ingredient1 = ingredient1
        self.__ingredient2 = ingredient2
        self.__ingredient3 = ingredient3
    def __str__(self):
        return f"My favorite food is {self.__dish}. Ingredients: {self.__ingredient1}, {self.__ingredient2}, {self.__ingredient3}"
fave1 = Favorite_food("Adobo","Pork","Patatas","Toyo")
fave2 = Favorite_food("Ampalaya","Egg","Onion","Garlic")
fave3 = Favorite_food("Dinuguan","Pork","Vinegar","Spices")
for x in (fave1,fave2,fave3):
print(x)
