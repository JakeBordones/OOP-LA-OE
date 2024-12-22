from  abc import ABC, abstractmethod

class Character(ABC):
    @property
    @abstractmethod
    def alias(self):
        pass

class Batman(Character):
    def __init__(self, real_name):
        self.real_name = real_name
        self.__alias = "Batman"

    @property
    def alias(self):
        return self.__alias

batman = Batman("Bruce Wayne")
print(batman.alias)