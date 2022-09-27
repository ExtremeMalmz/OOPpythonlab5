class MutatedAnimal:
    def __init__(self, namn:str, alder:int, mat:list) -> None:
        self.namn = namn
        self.alder = alder
        self.mat = mat

    def get_name(self) -> None:
        return self.namn

    def set_namn(self,namn)-> None:
        self.namn = namn

    def get_alder(self) -> int:
        return self.alder

    def set_alder(self,alder) -> None:
        self.alder = alder
        
    def get_mat(self) -> list:
        return ',och '.join(self.mat)

    def add_mat(self) -> None:
        newMat = input("Mat du ska lägga in: ")
        self.mat.append(newMat)

    def remove_mat(self) -> None:
        userInputMat = input("Vilken mat vill du ta bort?: ")

        if userInputMat in self.mat:
            self.mat.remove(userInputMat)
        else:
            print("Fanns ingen mat med det angivna namnet")

    @classmethod
    def create_an_animal(cls):
        name = input("Name: ")
        alder = input("Ålder: ")
        matLista = []
        while True:
            mat = input("Mat (lämna blankt när färdig): ")
            #Uppgradering av Antons där det bara var break
            if mat == "":
                break
            else:
                matLista.append(mat)
        return name, alder, matLista

    @classmethod
    def create(cls) -> any:
        pass