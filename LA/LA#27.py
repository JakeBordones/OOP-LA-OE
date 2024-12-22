from abc import ABC, abstractmethod


class Leonardo(ABC):
    def __init__(self, real_name):
        self.real_name = real_name
        self.__alias = "Nardo"
       
    @property
    def alias(self):
        return self.__alias 

class Michaelangelo(ABC):
    def __init__(self, real_name):
        self.real_name = real_name
        self.__alias = "Mike"
     
    @property
    def alias(self):
        return self.__alias

class Donatello(ABC):
    def __init__(self, real_name):
        self.real_name = real_name
        self.__alias = "Dona"
     
    @property
    def alias(self):
        return self.__alias

class Raphael(ABC):
    def __init__(self, real_name):
        self.real_name = real_name
        self.__alias = "Ralph"

    @property
    def alias(self):
        return self.__alias
    

if __name__== "__main__":
    turtle = Michaelangelo("Michael")
    print(turtle.real_name)