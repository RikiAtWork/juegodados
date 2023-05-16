class Dado:
    __caras = 6

    def __init__(self, fcaras):
        self.set_caras(fcaras)

    def lanzar(self):
        import random
        return random.randint(1, self.__caras)

    def get_caras(self):
        return self.__caras

    def set_caras(self, fcaras):
        caras_permitidas = [4, 6, 8, 10, 12, 20, 120, 200, 300]
        if fcaras in caras_permitidas:
            self.__caras = fcaras
        else:
            raise Exception("Numero de caras incorrecto")
