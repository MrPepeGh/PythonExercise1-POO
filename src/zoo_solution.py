import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Zoo:

    def __init__(self):
        self.animaleszoo = []

    def nuevoanimal(self, animal):
        self.animaleszoo.append(animal)
        logging.info(f"Ahora hay un {animal} en el zoo!")

    def mostraranimaleszoo(self):
        if not self.animaleszoo:
            logging.warning("No hay ningun animal en el zoo :(")
        else:
            logging.info("En el zoo hay: ")
            for animal in self.animaleszoo:
                print(f"- {animal}")

if __name__ == "__main__":
    zoo = Zoo()
    zoo.nuevoanimal("Wolf: Tony")
    zoo.nuevoanimal("Lion: Mufasa")
    zoo.nuevoanimal("Eagle: Blue")
    zoo.mostraranimaleszoo()