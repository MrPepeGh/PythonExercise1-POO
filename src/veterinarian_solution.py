import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Veterinarian:
    def __init__(self, name: str):
        self.name = name
        logging.info(f"El Dr. {self.name} está listo ")

    def checkup(self, animal):
        logging.info(f"El Dr. {self.name} está revisando a {animal.name}")

class Dog:
    def __init__(self, name: str):
        self.name = name
        logging.info(f"Ha venido un perro llamado {self.name}")

if __name__ == "__main__":
    dog1 = Dog("Rex")
    vet = Veterinarian("Jorge el curioso")

    vet.checkup(dog1)