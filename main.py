from tkinter import filedialog, Tk
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, Comment

from lista_ciudad import ListaCiudades
from lista_robot import ListaRobots

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
            ("Archivos XML", "*.xml"),
            ("Todos los archivos", "*.*")
        )
    )
    if ruta is None or ruta == " " or ruta == " ":
        win.destroy()
        return None
    else:
        win.destroy()
        return ruta

if __name__== "__main__":
    Ciudades = ListaCiudades()
    Robots = ListaRobots()
    opt = 0

    while opt != 4:
        opt = menu()

        if opt == 1:
            ruta = abrir()
            if ruta is not None:
                try:
                    contenido = ET.parse(ruta)
                    raiz = contenido.getroot()
                    ########################################### Para el listado de ciudades ###########################################
                    
                    ciudades = raiz.find('listaCiudades')
                    #Recorre la tag "listaCiudades"
                    for child in ciudades:
                        info = child.find('nombre')#Obtiene el tag nombre
                        nombre = str(info.text)#Nombre de la ciudad
                        filas = int(info.attrib['filas'])#Número de filas de la ciudad
                        columnas = int(info.attrib['columnas'])#Número de columnas de la ciudad
                        if Ciudades.isEmpty() == True:
                            Ciudades.addEnd(nombre, filas, columnas)
                        else:
                            #Verifica si la ciudad ya existe en el listado
                            verificacion = Ciudades.searchCiudad(nombre)
                            #Si la ciudad ya existe
                            if verificacion is not None:
                                #Como se va eliminar un nodo es necesario actualizar los contadores de ciudades de la lista
                                #Actualiza el contador de ciudades que tienen unidades civiles en la lista
                                if verificacion.getContadorUnidadesCiviles() > 0:
                                    contador = Ciudades.getContadorCiudadesCiviles() - 1
                                    Ciudades.setContadorCiudadesCiviles(contador)
                                else:
                                    #No hacer nada
                                    pass
                                #Actualiza el contador de ciudades que tienen recursos en la lista
                                if verificacion.getContadorRecursos() > 0:
                                    contador = Ciudades.getContadorCiudadesRecursos() - 1
                                    Ciudades.setContadorCiudadesRecursos(contador)
                                else:
                                    #No hacer nada
                                    pass
                                #Elimina el nodo de la ciudad que ya existe en la lista
                                Ciudades.deleteCiudad(nombre)
                                
                                #Agrega el nodo con la nueva ciudad
                                Ciudades.addEnd(nombre, filas, columnas)
                            #Si la ciudad no existe    
                            else:
                                Ciudades.addEnd(nombre, filas, columnas)

                        #Recorre la tag "ciudad" para obtener las tags "fila" que hay en ella
                        ciudad_actual = Ciudades.searchCiudad(nombre)
                        #Variable para aumentar el contador de Unidades Civiles y el contador de Recursos de la lista una sola vez
                        ya_conto = False #A la primera UnidadCivil encontrada cambia a True
                        ya_conto2 = False #Al primer Recurso encontrado cambia a True
                        for row in child.iter('fila'): 
                            indice_columna = 1 #Coordenada X
                            indice_fila = int(row.attrib['numero']) #Coordenada Y
                            cadena = row.text
                            #Recorre la cadena para obtener la info de cada celda(columna) de la fila
                            for caracter in cadena:
                                if caracter == '*':
                                    ciudad_actual.mapa.insertarNodo('Intransitable', False, 0, indice_columna, indice_fila)
                                    indice_columna += 1
                                elif caracter == ' ':
                                    ciudad_actual.mapa.insertarNodo('Camino', True, 0, indice_columna, indice_fila)
                                    indice_columna += 1
                                elif caracter == 'E':
                                    ciudad_actual.mapa.insertarNodo('PuntoEntrada', True, 0, indice_columna, indice_fila)
                                    cont = ciudad_actual.getContadorPuntosDeEntrada() + 1
                                    ciudad_actual.setContadorPuntosDeEntrada(cont)#Aumenta el contador de celdas "PuntoEntrada" del nodo
                                    indice_columna += 1
                                elif caracter == 'C':
                                    ciudad_actual.mapa.insertarNodo('UnidadCivil', True, 0, indice_columna, indice_fila)
                                    cont = ciudad_actual.getContadorUnidadesCiviles() + 1
                                    ciudad_actual.setContadorUnidadesCiviles(cont)#Aumenta el contador de celdas "UnidadCivil" del nodo
                                    indice_columna += 1
                                    if ya_conto == False:
                                        contador = Ciudades.getContadorCiudadesCiviles() + 1
                                        Ciudades.setContadorCiudadesCiviles(contador)#Aumenta el contador de ciudades de la lista, que tienen unidades civiles
                                        ya_conto = True
                                    else:
                                        #No hacer nada
                                        pass
                                elif caracter == 'R':
                                    ciudad_actual.mapa.insertarNodo('Recurso', False, 0, indice_columna, indice_fila)
                                    cont = ciudad_actual.getContadorRecursos() + 1
                                    ciudad_actual.setContadorRecursos(cont)#Aumenta el contador de celdas "Recurso" del nodo
                                    indice_columna += 1
                                    if ya_conto2 == False:
                                        contador = Ciudades.getContadorCiudadesRecursos() + 1
                                        Ciudades.setContadorCiudadesRecursos(contador)
                                        ya_conto2 = True
                                    else:
                                        #No hacer nada
                                        pass
                        #Recorre la tag "ciudad" para obtener las tags "UnidadMilitar"
                        for unidad in child.iter('unidadMilitar'):
                            pos_y = int(unidad.attrib['fila'])#Coordenada X de la unidad militar
                            pos_x = int(unidad.attrib['columna'])#Coordenada Y de la unidad militar
                            capacidad = int(unidad.text)#Capacidad de combate de la unidad militar
                            nodo = ciudad_actual.mapa.searchCelda(pos_x, pos_y)#Obtiene el nodo a modificar
                            #Settea los nuevos valores
                            nodo.setTipo('UnidadMilitar')
                            nodo.setEstado(False)
                            nodo.setCapacidadCombate(capacidad)           
                
                    ########################################### Para el listado de robots #############################################
                    
                    robots = raiz.find('robots')
                    #Recorre la tag "robots"
                    for robot in robots:
                        sub_tag = robot.find('nombre')#Obtiene la tag nombre
                        nombre = str(sub_tag.text)#Nombre del robot
                        tipo = str(sub_tag.attrib['tipo'])#Tipo del robot, ChapinFighter o ChapinRescue
                        #Si el robot a agregar es ChapinFighter
                        if tipo == 'ChapinFighter':
                            capacidad = int(sub_tag.attrib['capacidad'])#Capacidad de combate del robot
                            if Robots.isEmpty() == True:
                                Robots.addEnd(nombre, tipo)#Agrega el robot a la lista
                                robot_actual = Robots.searchRobot(nombre, tipo)#Obtiene el robot que se va a agregar
                                robot_actual.setCapacidadCombate(capacidad)#Asigna la capacidad de combate al robot
                            else:
                                #Verifica si el robot ya existe en la lista
                                robot_actual = Robots.searchRobot(nombre, tipo)
                                #Si ya existe
                                if robot_actual is not None:
                                    #Solo reasigna la capacidad de combate, los demás atributos no necesitan cambiar
                                    robot_actual.setCapacidadCombate(capacidad)
                                #Si la ciudad no existe
                                else:
                                    Robots.addEnd(nombre, tipo)
                                    robot_actual = Robots.searchRobot(nombre, tipo)
                                    robot_actual.setCapacidadCombate(capacidad)
                        #Si el robot a agregar es ChapinRescue
                        else:
                            if Robots.isEmpty() == True:
                                Robots.addEnd(nombre, tipo)
                            else:
                                robot_actual = Robots.searchRobot(nombre, tipo)
                                #Si ya existe el robot en la lista
                                if robot_actual is not None:
                                    #No hacer nada
                                    pass
                                #Si el robot no existe en la lista
                                else:
                                    Robots.addEnd(nombre, tipo)
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

