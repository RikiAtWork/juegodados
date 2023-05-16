import juego

x = juego.Juego(str(input("Introdueix el nom del primer jugador: ")),
                str(input("Introdueix el nom del segon jugador: ")),
                str(input("Introdueix el nom del tercer jugador: ")),
                int(input("Introdueix el nom de cares per al primer dau: ")),
                int(input("Introdueix el nom de cares per al segon dau: ")),
                int(input("Introdueix el nom de cares per al tercer dau: ")),
                int(input("Introdueix el nom de cares per al quart dau: ")),
                int(input("Introdueix el nom de llançaments: ")),
                input("Vols veure els resultats intermedis per pantalla? (S/N): "))

x.jugar()
x.mostrar()
