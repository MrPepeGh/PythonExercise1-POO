"""
Proyecto: Creación de gatos usando Programación Orientada a Objetos (POO)
Este archivo define la clase Cat y muestra cómo crear instancias, usando logging para mostrar el flujo.
"""
import logging

# Configuración básica del logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Cat:
    """
    Clase Cat representa el concepto de un gato.
    En POO, una clase es un molde para crear objetos (instancias).
    """
    def __init__(self, name: str, age: int):
        """
        El método __init__ es el constructor. Se llama automáticamente al crear una instancia.
        Los atributos son las características del objeto.
        """
        self.name = name
        self.age = age
        logging.info(f"Se ha creado un gato llamado {self.name} de {self.age} años.")

    def meow(self):
        """
        Un método define el comportamiento de los objetos.
        """
        logging.info(f"{self.name} está maullando.")
        print(f"{self.name}: ¡Miau miau!")

    def birthday(self):
        """
        Este método incrementa la edad del gato, mostrando encapsulamiento.
        """
        self.age += 1
        logging.info(f"{self.name} ahora tiene {self.age} años.")

if __name__ == "__main__":
    # Crear instancias de la clase Cat
    cat1 = Cat("Milo", 2)
    cat2 = Cat("Nina", 4)

    # Llamar métodos
    cat1.meow()
    cat2.meow()

    # Celebrar cumpleaños
    cat1.birthday()
    cat2.birthday()

    # Mostrar atributos
    print(f"{cat1.name} tiene {cat1.age} años.")
    print(f"{cat2.name} tiene {cat2.age} años.")
