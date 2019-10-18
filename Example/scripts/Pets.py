"""
Descripcion del documento
"""

import random

class Pets(object):
    """
    Esta clase representa mascotas
    """

    version = '0.1'

    def __init__(self, name, owner):
        """
        Crea las variables necesarias de una instancia, el nombre y dueno de una mascota.

        :type name: string
        :param name: nombre de la mascota
        
        :type owner: string
        :param owner: dueno de la mascota
        """

        self.name = []
        self.owner = owner
        self.name.append(name)

    def add_pet(self, name):
        """
        agrega una mascota a la lista

        :type name: string
        :param name: nombre de la mascota para agregarla a la lista
        """

        self.name.append(name)

    def show_pets(self):
        """
        imprime todas las mascotas actualmente en la lista
        """

        print ("El dueno de las mascotas es: " + self.owner)
        for each in self.name:
            print (each)

    @classmethod            # constructor alternativo
    def random_pets(cls, owner):
        """
        Clase especial para generar un nombre al azar al crear una mascota.

        :type cls: Pets
        :param cls: instancia del constructor al azar se otorga a INIT.

        :type owner: string
        :param owner: nombre del dueno de la mascota
        """

        pets_random = ['Cocoa', 'Jasper', 'Elmo', 'Chester', 'Rufus']
        random_pet_name = random.choice(pets_random)
        return cls(random_pet_name, owner)

    @staticmethod           # attach a method doesn't need self
    def get_average_age(pet_type):
        """
        Imprime la edad promedio de una mascota

        :type pet_type: string
        :param pet_type: Las 3 mascotas mas populares
         """

        if pet_type is 'dog':
            print ('Dogs average life is: 13 years')
        if pet_type is 'cat':
            print ('Cats average life is: 15 years')
        if pet_type is 'fish':
           print ('Gold Fish average life is: 30 years')


if __name__ == "__main__":
    # the first class
    p1 = Pets('jabba', 'Dan Sheffner')
    print(type(p1))
    p1.show_pets()
    print ()
    p1.get_average_age('cat')

    print ()

    # the second class
    p2 = Pets.random_pets('Chris Sheffner')
    print(type(p2))
    p2.show_pets()
    print ()

   # owner gets another pet later on and names it roo
    print ('owner buys another pet later on...')
    p2.add_pet('Roo')
    p2.show_pets()
    print ()

    p2.get_average_age('dog')
    p2.get_average_age('fish')