from death_claw import Deathclaw
from cow_with_two_heads import CowWithTwoHeads
from radscorpion import Radscorpion

class Zoo:
    ANIMALS = [Deathclaw,CowWithTwoHeads,Radscorpion]

    def __init__(self) -> None:
        self.animalList = []

    def start(self) -> None:
        #this is where we run stuff from

        print("Welcome to the zoo")
        
        self.create_animals()
        print("\nDin deathclaw har ett bra namn!")
        print("Här är alla djurparkens djur")
        self.print_animals()

        #adding food to deathclaw
        print("\nDin deathclaw vill ha mer matalternativ!")
        self.animalList[0].add_mat()
        print("Matalternativ:")
        print(self.animalList[0].get_mat())

        print("\nDin deathclaw vill ha färre matalternativ! Ta bort en")
        self.animalList[0].remove_mat()
        print("Uppdaterade matalternativ")
        print(self.animalList[0].get_mat())

        print("\n\nNu säger alla djuren vad de kan!")
        for i in self.animalList:
            print(str(i.get_name()) + ": ", end="")
            i.talk()

        print("\nTACK FÖR ATT DU BESÖKTE PARKEN - VÄLKOMMEN ÅTER")



    def add_animals_to_list(self,animal) -> None:
        self.animalList.append(animal)

    
    def create_animals(self) -> None:
        #create the animals here
        print("Creating the animals...")

        #Adding deathclaw
        print("Du får skapa djurparkens första \"Deathclaw\"")
        animal = self.ANIMALS[0].create()
        self.add_animals_to_list(animal)

        #all the other animals are created automatically
        #the cow with two heads is created
        animal = self.ANIMALS[1].create()
        self.add_animals_to_list(animal)

        #rad scorpions created
        animal = self.ANIMALS[2].create()
        self.add_animals_to_list(animal)


    def print_animals(self) -> None:
        for animals in self.animalList:
            print(animals)