import dado


class Juego:
    __jugador1 = ""
    __jugador2 = ""
    __jugador3 = ""
    __lanzamientos = 0

    def __init__(self, jugador1, jugador2, jugador3, caras1, caras2, caras3, caras4, lanzamientos, intermedios):
        self.set_jugador1(jugador1)
        self.set_jugador2(jugador2)
        self.set_jugador3(jugador3)
        self.set_lanzamientos(lanzamientos)
        if caras1 == caras2 or caras1 == caras3 or caras1 == caras4:
            raise Exception("No pot haver-hi dos daus iguals")
        elif caras2 == caras1 or caras2 == caras3 or caras2 == caras4:
            raise Exception("No pot haver-hi dos daus iguals")
        elif caras3 == caras1 or caras3 == caras2 or caras3 == caras4:
            raise Exception("No pot haver-hi dos daus iguals")
        elif caras4 == caras1 or caras4 == caras2 or caras4 == caras3:
            raise Exception("No pot haver-hi dos daus iguals")
        else:
            self.dado1 = dado.Dado(caras1)
            self.dado2 = dado.Dado(caras2)
            self.dado3 = dado.Dado(caras3)
            self.dado4 = dado.Dado(caras4)

        # Me guardo en un atributo booelano si necesito o no ver los datos intermedios
        self.__intermedios = (intermedios in ("S",  "s"))
        self.resultado1 = 0
        self.resultado2 = 0
        self.resultado3 = 0

    def set_jugador1(self, fjugador1):
        if len(fjugador1) > 20:
            raise Exception("La longitud del nom del jugador 1 no pot ser major de 20")
        else:
            self.__jugador1 = fjugador1

    def set_jugador2(self, fjugador2):
        if len(fjugador2) > 20:
            raise Exception("La longitud del nom del jugador 2 no pot ser major de 20")
        else:
            self.__jugador2 = fjugador2

    def set_jugador3(self, fjugador3):
        if len(fjugador3) > 20:
            raise Exception("La longitud del nom del jugador 3 no pot ser major de 20")
        else:
            self.__jugador3 = fjugador3

    def set_lanzamientos(self, flanzamientos):
        if not 2 < flanzamientos < 1000:
            raise Exception("El nombre de llançaments ha d'estar entre 2 i 100")
        else:
            self.__lanzamientos = flanzamientos

    def jugar(self):
        for x in range(self.__lanzamientos):
            # jugador1
            lanzamiento1 = self.dado1.lanzar()
            lanzamiento2 = self.dado2.lanzar()
            lanzamiento3 = self.dado3.lanzar()
            lanzamiento4 = self.dado4.lanzar()
            self.resultado1 += (lanzamiento1 + lanzamiento2 + lanzamiento3 + lanzamiento4)

            if self.__intermedios:
                print(f"Lanzamiento {x + 1}:")
                print(
                    f"{self.__jugador1}: {lanzamiento1} {lanzamiento2} {lanzamiento3} {lanzamiento4}"
                    f"({self.resultado1})")

            # jugador2
            lanzamiento1 = self.dado1.lanzar()
            lanzamiento2 = self.dado2.lanzar()
            lanzamiento3 = self.dado3.lanzar()
            lanzamiento4 = self.dado4.lanzar()
            self.resultado2 += (lanzamiento1 + lanzamiento2 + lanzamiento3 + lanzamiento4)

            if self.__intermedios:
                print(
                    f"{self.__jugador2}: {lanzamiento1} {lanzamiento2} {lanzamiento3} {lanzamiento4}"
                    f"({self.resultado2})")

            # jugador3
            lanz1 = self.dado1.lanzar()
            lanz2 = self.dado2.lanzar()
            lanz3 = self.dado3.lanzar()
            lanz4 = self.dado4.lanzar()
            self.resultado3 += (lanz1 + lanz2 + lanz3 + lanz4)

            if self.__intermedios:
                print(
                    f"{self.__jugador3}: {lanz1} {lanz2} {lanz3} {lanz4}"
                    f"({self.resultado3})")
                print("")

    def mostrar(self):
        print("Resultats:")
        print(f"Jugador 1: {self.__jugador1}")
        print(f"Jugador 2: {self.__jugador2}")
        print(f"Jugador 3: {self.__jugador3}")
        print(f"Nom de llançaments: {self.__lanzamientos}")
        print(f"Daus: {self.dado1.get_caras()}, {self.dado2.get_caras()}, {self.dado3.get_caras()} "
              f"y {self.dado4.get_caras()}")
        print(f"Punts jugador 1: {self.resultado1}")
        print(f"Punts jugador 2: {self.resultado2}")
        print(f"Punts jugador 3: {self.resultado3}")
        if self.resultado1 > self.resultado2 and self.resultado3:
            print(f"El guanyador es {self.__jugador1} con {self.resultado1} punts")
        elif self.resultado1 < self.resultado2 and self.resultado3 < self.resultado2:
            print(f"El guanyador es {self.__jugador2} con {self.resultado2} punts")
        elif self.resultado2 < self.resultado1 < self.resultado3:
            print(f"El guanyador es {self.__jugador3} con {self.resultado3} punts")
        elif self.resultado1 == self.resultado2 and self.resultado3:
            print("hi ha hagut un EMPAT")
