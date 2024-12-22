class Party:
    def __init__(self, theme, food1, food2):
        self.theme = theme
        self.food1 = food1
        self.food2 = food2

    def food_list(self):
        print(f"List of foods:\n1. {self.food1}\n2.{self.food2}")

    def __secret_dish(self):
        print("Sinigang na hotdog")

    def show_special(self):
        self.__secret_dish()

holloween = Party("Holloween","Candy","Chocolate")
christmas = Party("Christmas","Graham", "Fried Chicken")
birthday = Party("Birthday", "Shanghai", "Ice Cream")

for x in (holloween,christmas,birthday):
    x.food_list()