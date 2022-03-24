from tkinter import filedialog, Tk

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

def abrir():
    win = Tk()
    win.withdraw()
    win.attributes('-topmost', True)#Posiciona el filedialog sobre las demás ventanas
    ruta = filedialog.askopenfilename(
        title = 'Seleccionar archivo',
        initialdir = '../',
        filetypes = (
            ('Archivos XML', "*.xml")
            ('Todos los archivos', '*.*')
        )
    )
    if ruta is None or ruta == " " or ruta == " ":
        win.destroy()
        return None
    else:
        win.destroy()
        return ruta

if __name__== "__main__":
    opt = 0

    while opt != 4:
        opt = menu()

        if opt == 1:
            ruta = abrir()
            if ruta is not None:
                try:
                    pass
                except:
                    print('> Algo salió mal y no es posible completar la lectura del archivo')
            else:
                print('> No se cargó ningún archivo')       
        elif opt == 2:
            pass
        elif opt == 3:
            pass
        elif opt == 4:
            print('> Gracias por usar el programa')
        else:
            print('> La opción ingresada no es valida...Intenta de nuevo')

