"""
.. include:: ./README.md
"""


class Dado:
    """
    Esta clase es un Dado que comprueba si el numero de caras se encuentra en la lista de caras permitidas y si lo esta
    lo añade al constructor.
    :arg: caras: privado
    """
    __caras = 6

    def __init__(self, fcaras):
        """
        Constructor donde establece el numero de caras pasados como parametro
        :param fcaras: int
        """
        self.set_caras(fcaras)

    def lanzar(self):
        """
        Metodo que devuelve un numero aleatorio entre 1 y el numero de caras privado.

        :return: int: numero aleatorio
        """
        import random
        return random.randint(1, self.__caras)

    def get_caras(self):
        """
        Metodo que nos devuelve el numero de caras actuales
        :return: __caras: int
        """
        return self.__caras

    def set_caras(self, fcaras):
        """
        Metodo que establece el numero de caras si pasa la comprobacion en las caras_permitidas
        :param fcaras: int

        """
        caras_permitidas = [4, 6, 8, 10, 12, 20, 120, 200, 300]
        if fcaras in caras_permitidas:
            self.__caras = fcaras
        else:
            raise Exception("Nom de cares incorrecte")
