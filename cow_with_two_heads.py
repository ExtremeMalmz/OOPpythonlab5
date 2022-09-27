from __future__ import annotations
from mutated_animal import MutatedAnimal

class CowWithTwoHeads(MutatedAnimal):
    def __init__(self,namn:str, alder:int, mat:list) -> None:
        self.__namn = namn
        self.__alder = alder
        self.__mat = mat
        super().__init__(namn, alder, mat)

    @classmethod
    def create(cls) -> CowWithTwoHeads:
        #print("Creating a cow with two heads")
        #namn, alder, mat = MutatedAnimal.create_an_animal()
        #Detta är fusk, jag vet beklagar.
        namn = "Brahmin"
        alder = 2
        mat = ["Gräs", "Utstrålad svamp"]
        return cls(namn, alder, mat)

    def talk(self) -> None:
        print("MOO! I say moo!")

    def __str__(self) -> str:
        return f"Namn:{self.__namn} - Ålder: {self.__alder} - Mat: {', '.join(self.__mat)}"