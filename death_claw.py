from __future__ import annotations
from mutated_animal import MutatedAnimal

class Deathclaw(MutatedAnimal):
    def __init__(self,namn:str, alder:int, mat:list) -> None:
        self.__namn = namn
        self.__alder = alder
        self.__mat = mat
        super().__init__(namn, alder, mat)

    @classmethod
    def create(cls) -> Deathclaw:
        namn, alder, mat = MutatedAnimal.create_an_animal()
        return cls(namn, alder, mat)

    def talk(self):
        print("I'm the one who put the 'law' in the deathclaw!")

    def __str__(self):
        return f"Namn:{self.__namn} - Ålder: {self.__alder} - Mat: {', '.join(self.__mat)}"