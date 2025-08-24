"""
Proyecto: Ejemplo de herencia en POO con aves.
Este archivo define la clase Bird y la clase Eagle que hereda de Bird.
Incluye logging y comentarios explicativos sobre herencia.
"""
import logging

# Configuración básica del logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class Bird:
    """
    Clase base Bird representa el concepto general de un ave.
    En POO, una clase base puede ser heredada por otras clases más específicas.
    """
    def __init__(self, name: str, age: int, species: str):
        self.name = name
        self.age = age
        self.species = species
        logging.info(f"Se ha creado un ave de especie {self.species} llamada {self.name} de {self.age} años.")

    def sing(self):
        """
        Método que representa el canto del ave.
        """
        logging.info(f"{self.name} está cantando.")
        print(f"{self.name}: ¡Pío pío!")


    def birthday(self):
        self.age += 1
        logging.info(f"{self.name} ahora tiene {self.age} años.")

    def migrate(self, destino:str):
        logging.info(f"{self.name} está migrando hacia {destino}")
        print(f"{self.name}: Como dijo mi padre! nos vamos de paseo para {destino}!")

# Ejemplo de herencia: Eagle hereda de Bird
class Eagle(Bird):
    """
    Clase Eagle hereda de Bird.
    En POO, la herencia permite que una clase hija obtenga atributos y métodos de la clase padre.
    """
    def __init__(self, name: str, age: int):
        # Llama al constructor de Bird con especie fija "Águila"
        super().__init__(name, age, "Águila")
        self.altitude=40
        logging.info(f"Se ha creado un águila llamada {self.name}.")

    def fly(self):
        """
        Método propio de Eagle, además de los heredados de Bird.
        """
        logging.info(f"{self.name} está volando alto.")
        print(f"{self.name}: ¡Estoy volando alto!")

    def show_altitude(self):
        logging.info(f"{self.name} está a {self.altitude} metros de altura")
        print(f"{self.name}: Mirame mamá estoy volando 😭")

class parrot(Bird):
        def __init__(self, name: str, age: int):
            super().__init__(name, age, "loro")
            logging.info(f"Ha aparecido un loro llamado {self.name}")

        def talk(self,frase: str):
            logging.info(f"{self.name} Saludalos! ")
            print(f"{self.name}: {frase}")

if __name__ == "__main__":
    Eagle1 = Eagle("Pablo",6)
    Eagle1.fly()
    Eagle1.show_altitude()
    Eagle1.birthday()
    Eagle1.migrate("Piscilago")

    parrot1 = parrot("Lorenzo",3)
    parrot1.talk("Holas, que onda!")
    parrot1.migrate("Miami")
