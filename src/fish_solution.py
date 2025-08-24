class fish:
    def __init__(self, name: str, age: int, species: str):
        self.name = name
        self.age = age
        self.species = species
    def swim (self):
        print (f"{self.name}: Qué se dice mi pez! glu glu glu")

if __name__ =="__main__":
    globo = fish("Srta. Puf", 14,"Globo")
    globo.swim()