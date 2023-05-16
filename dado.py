class Dado:
    __caras = 6

    def __init__(self, fcaras):
        self.setCaras(fcaras)

    def lanzar(self):
        import random
        return random.randint(1, self.__caras)

    def getCaras(self):
        return self.__caras

    def setCaras(self, fcaras):
        caras_permitidas = [4, 6, 8, 10, 12, 20, 120]
        if fcaras in caras_permitidas:
            self.__caras = fcaras
        else:
            raise Exception("Numero de caras incorrecto")
