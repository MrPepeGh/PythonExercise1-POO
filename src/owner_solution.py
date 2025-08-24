import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Bird:
    def __init__(self, name: str, age: int, species: str):
        self.name = name
        self.age = age
        self.species = species
    def __str__(self):
        return (f"{self.species}: {self.name} ({self.age} años)")
    def eat(self):
        logging.info(f"{self.name} está comiendo")
        print(f"{self.name}: Uff, mi hermano cocina bueno! ")

class Eagle(Bird):
    def __init__(self, name: str, age: int):
        super().__init__(name, age, "Águila")

class Parrot(Bird):
    def __init__(self, name: str, age: int):
        super().__init__(name, age, "Loro")

class Owner:
    def __init__(self, name: str):
        self.name = name
        self.animals = []
    def add_animal(self, animal: Bird):
        self.animals.append(animal)
        logging.info(f"{self.name} es dueño del {animal}")
    def feed_animals(self):
        if not self.animals:
            logging.warning(f"{self.name} no tiene animales para alimentar.")
            print(f"{self.name}: No tengo a quien darle comida 😢")
        else:
            logging.info(f"{self.name} está alimentando a sus animales")
            print(f"{self.name} está alimentando a sus animales:")
            for animal in self.animals:
                animal.eat()

if __name__ == "__main__":
    owner1 = Owner("JuanCa")

    eagle1 = Eagle("Pablo", 6)
    parrot1 = Parrot("Lorenzo", 3)

    owner1.add_animal(eagle1)
    owner1.add_animal(parrot1)

    owner1.feed_animals()
