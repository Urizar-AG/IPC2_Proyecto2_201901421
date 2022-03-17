
def menu():
    try:
        print(' _____________________________________________________')
        print('|                    Menú Principal                   |')
        print('|_____________________________________________________|')
        print('|1.Cargar archivo                                     |')
        print('|2.Realizar misión de rescate                         |')
        print('|3.Realizar misión de extracción                      |')
        print('|4.Salir                                              |')
        print('|_____________________________________________________|')
        option = int(input('Ingrese una opción:\n'))
        return option
    except ValueError:
        return None


if __name__== "__main__":
    opt = 0

    while opt != 4:
        opt = menu()

        if opt == 1:
            pass
        elif opt == 2:
            pass
        elif opt == 3:
            pass
        elif opt == 4:
            print('> Gracias por usar el programa')
        else:
            print('> La opción ingresada no es valida...Intenta de nuevo')

