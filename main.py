from tkinter import filedialog, Tk
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, Comment
from os import system, startfile

from lista_ciudad import ListaCiudades
from lista_robot import ListaRobots
from lista_ruta import ListaRutas

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

def preguntarCoordenadas(ciudad, tipo_de_busqueda):
    if tipo_de_busqueda == 'UnidadCivil':
        x = int(input('Ingresa la coordenda X de la unidad civil a rescatar: \n'))
        y = int(input('Ingresa la coordenda Y de la unidad civil a rescatar: \n'))
        celda = ciudad.mapa.searchCelda(x, y)
        return celda
    elif tipo_de_busqueda == 'PuntoEntrada':
        x = int(input('Ingresa la coordenada X del punto de entrada a usar: \n'))
        y = int(input('Ingresa la coordenada Y del punto de entrada a usar: \n'))
        celda = ciudad.mapa.searchCelda(x, y)
        return celda
    elif tipo_de_busqueda == 'Recurso':
        x = int(input('Ingresa la coordenada X del recurso a extraer: \n'))
        y = int(input('Ingresa la coordenada Y del recurso a extraer: \n'))
        celda = ciudad.mapa.searchCelda(x, y)
        return celda

#Encuentra el camino de rescate
def buscarCaminoRescate(origen, destino, plano):
    camino_completado = ListaRutas() #Guarda el camino a graficar
    camino = ListaRutas()
    camino.addEnd(origen.getCoordenadaX(), origen.getCoordenadaY()) #Añade el nodo de partida(punto de entrada)

    vecino_right = origen.right #El nodo que está a la derecha del punto de entrada
    vecino_up = origen.up#El nodo que está arriba del punto de entrada
    vecino_left = origen.left# El nodo que está a la izquierda del punto de entrada
    vecino_down = origen.down#El nodo que está debajo del punto de entrada

    #Si se puede avanzar hacia el vecino de la derecha
    if vecino_right is not None:
        #Verifica que al vecino al que se avanza no es una cabecera de la matriz
        if vecino_right.getTipo() != 'Cabecera':
            #Verifica que se pueda transitar por el vecino hacia el que se quiere avanzar
            if vecino_right.getEstado() == True:
                coordenada_x_actual = vecino_right.getCoordenadaX() 
                coordenada_y_actual = vecino_right.getCoordenadaY() 
                #Crea una copia del camino que se lleva recorrido
                longitud_camino = camino.getSize()
                copia = ListaRutas()
                aux = camino.getFirst()
                for i in range(longitud_camino):
                    copia.addEnd(aux.getCoordenadaX(), aux.getCoordenadaY())
                    aux = aux.next
                #Añade el vecino a la copia
                copia.addEnd(coordenada_x_actual, coordenada_y_actual)
                #Llama a la función caminosRescate
                caminosRescate(coordenada_x_actual, coordenada_y_actual, destino, copia, camino_completado, plano)
    #Si se puede avanzar hacia el vecino de arriba
    if vecino_up is not None:
        if vecino_up.getTipo() != 'Cabecera':
            if vecino_up.getEstado() == True:
                coordenada_x_actual = vecino_up.getCoordenadaX() 
                coordenada_y_actual = vecino_up.getCoordenadaY() 
                #Crea una copia del camino que se lleva recorrido
                longitud_camino = camino.getSize()
                copia = ListaRutas()
                aux = camino.getFirst()
                for i in range(longitud_camino):
                    copia.addEnd(aux.getCoordenadaX(), aux.getCoordenadaY())
                    aux = aux.next
                #Añade el vecino a la copia
                copia.addEnd(coordenada_x_actual, coordenada_y_actual)
                caminosRescate(coordenada_x_actual, coordenada_y_actual, destino, copia, camino_completado, plano)
    #Si se puede avanzar hacia el vecino de la izquierda
    if vecino_left is not None:
        if vecino_left.getTipo() != 'Cabecera':
            if vecino_left.getEstado() == True:
                coordenada_x_actual = vecino_left.getCoordenadaX() 
                coordenada_y_actual = vecino_left.getCoordenadaY() 
                #Crea una copia del camino que se lleva recorrido
                longitud_camino = camino.getSize()
                copia = ListaRutas()
                aux = camino.getFirst()
                for i in range(longitud_camino):
                    copia.addEnd(aux.getCoordenadaX(), aux.getCoordenadaY())
                    aux = aux.next
                #Añade el vecino a la copia
                copia.addEnd(coordenada_x_actual, coordenada_y_actual)
                caminosRescate(coordenada_x_actual, coordenada_y_actual, destino, copia, camino_completado, plano)
    #Si se puede avanzar hacia el vecino de la derecha
    if vecino_down is not None:
        if vecino_down.getTipo() != 'Cabecera':
            if vecino_down.getEstado() == True:
                coordenada_x_actual = vecino_down.getCoordenadaX() 
                coordenada_y_actual = vecino_down.getCoordenadaY() 
                #Crea una copia del camino que se lleva recorrido
                longitud_camino = camino.getSize()
                copia = ListaRutas()
                aux = camino.getFirst()
                for i in range(longitud_camino):
                    copia.addEnd(aux.getCoordenadaX(), aux.getCoordenadaY())
                    aux = aux.next
                #Añade el vecino a la copia
                copia.addEnd(coordenada_x_actual, coordenada_y_actual)
                caminosRescate(coordenada_x_actual, coordenada_y_actual, destino, copia, camino_completado, plano)
    
    #Retorna None si no encontro una ruta para completar la misión
    if camino_completado.getSize() == 0:
        return None
    #Retorna la lista del camino seguro para el rescate
    else:
        return camino_completado           

def caminosRescate(x_actual, y_actual, destino, camino, camino_completado, plano):
    #Si llegó al punto de destino
    if x_actual == destino.getCoordenadaX() and y_actual == destino.getCoordenadaY():
        #Si la lista está vacía
        if camino_completado.getSize() == 0:
            #Añade el camino encontrado a la lista que guarda el camino a graficar 
            longitud_camino = camino.getSize()
            aux = camino.getFirst()
            for i in range(longitud_camino):
                camino_completado.addEnd(aux.getCoordenadaX(), aux.getCoordenadaY())
                aux = aux.next
        #Si encontró otro camino y es más corto que el que ya está guardado
        elif camino.getSize() < camino_completado.getSize():
            #Elimina el que ya está guardado
            camino_completado.clearLista()
            #Guarda el nuevo camino
            longitud_camino = camino.getSize()
            aux = camino.getFirst()
            for i in range(longitud_camino):
                camino_completado.addEnd(aux.getCoordenadaX(), aux.getCoordenadaY())
                aux = aux.next
    else:
        nodo = plano.searchCelda(x_actual, y_actual)#Obtiene el nodo que se está evaluando actualmente
        vecino_right = nodo.right #El nodo que está a la derecha del nodo actual
        vecino_up = nodo.up#El nodo que está arriba del nodo actual
        vecino_left = nodo.left# El nodo que está a la izquierda del nodo actual
        vecino_down = nodo.down#El nodo que está debajo del nodo actual
        
        if vecino_right is not None:
            if vecino_right.getTipo() != 'Cabecera':
                if vecino_right.getEstado() == True:#Si el nodo es transitable
                    coordenada_x_actual = vecino_right.getCoordenadaX()#Coordenada x del vecino al que se está avanzando
                    coordenada_y_actual = vecino_right.getCoordenadaY()#Coordenada y del vecino al que se está avanzando
                    #Crea una copia del camino
                    longitud_camino = camino.getSize()
                    copia = ListaRutas()
                    aux = camino.getFirst()
                    for i in range(longitud_camino):
                        copia.addEnd(aux.getCoordenadaX(), aux.getCoordenadaY())
                        aux = aux.next
                    try:
                        #Si el nodo no ha sido visitado, no existe en la lista
                        if camino.search(coordenada_x_actual, coordenada_y_actual) == False:
                            copia.addEnd(coordenada_x_actual, coordenada_y_actual)
                            #Recursividad
                            caminosRescate(coordenada_x_actual, coordenada_y_actual, destino, copia, camino_completado, plano)
                        else:
                            #Ya fue visitado no se agrega el nodo a la lista
                            pass    
                    except:
                        #print(e)
                        pass
        if vecino_up is not None:
            if vecino_up.getTipo() != 'Cabecera':
                if vecino_up.getEstado() == True:#Si el nodo es transitable
                    coordenada_x_actual = vecino_up.getCoordenadaX()#Coordenada x del vecino al que se está avanzando
                    coordenada_y_actual = vecino_up.getCoordenadaY()#Coordenada y del vecino al que se está avanzando
                    #Crea una copia del camino
                    longitud_camino = camino.getSize()
                    copia = ListaRutas()
                    aux = camino.getFirst()
                    for i in range(longitud_camino):
                        copia.addEnd(aux.getCoordenadaX(), aux.getCoordenadaY())
                        aux = aux.next
                    try:
                        #Si el nodo no ha sido visitado, no existe en la lista
                        if camino.search(coordenada_x_actual, coordenada_y_actual) == False:
                            copia.addEnd(coordenada_x_actual, coordenada_y_actual)
                            caminosRescate(coordenada_x_actual, coordenada_y_actual, destino, copia, camino_completado, plano)
                        else:
                            #Ya fue visitado no se agrega el nodo a la lista
                            pass    
                    except:
                        #print(e)
                        pass      
        if vecino_left is not None:
            if vecino_left.getTipo() != 'Cabecera':
                if vecino_left.getEstado() == True:#Si el nodo es transitable
                    coordenada_x_actual = vecino_left.getCoordenadaX()#Coordenada x del vecino al que se está avanzando
                    coordenada_y_actual = vecino_left.getCoordenadaY()#Coordenada y del vecino al que se está avanzando
                    #Crea una copia del camino
                    longitud_camino = camino.getSize()
                    copia = ListaRutas()
                    aux = camino.getFirst()
                    for i in range(longitud_camino):
                        copia.addEnd(aux.getCoordenadaX(), aux.getCoordenadaY())
                        aux = aux.next
                    try:
                        #Si el nodo no ha sido visitado, no existe en la lista
                        if camino.search(coordenada_x_actual, coordenada_y_actual) == False:
                            copia.addEnd(coordenada_x_actual, coordenada_y_actual)
                            caminosRescate(coordenada_x_actual, coordenada_y_actual, destino, copia, camino_completado, plano)
                        else:
                            #Ya fue visitado no se agrega el nodo a la lista
                            pass    
                    except:
                        #print(e)
                        pass         
        if vecino_down is not None:
            if vecino_down.getTipo() != 'Cabecera':
                if vecino_down.getEstado() == True:#Si el nodo es transitable
                    coordenada_x_actual = vecino_down.getCoordenadaX()#Coordenada x del vecino al que se está avanzando
                    coordenada_y_actual = vecino_down.getCoordenadaY()#Coordenada y del vecino al que se está avanzando
                    #Crea una copia del camino
                    longitud_camino = camino.getSize()
                    copia = ListaRutas()
                    aux = camino.getFirst()
                    for i in range(longitud_camino):
                        copia.addEnd(aux.getCoordenadaX(), aux.getCoordenadaY())
                        aux = aux.next
                    try:
                        #Si el nodo no ha sido visitado, no existe en la lista
                        if camino.search(coordenada_x_actual, coordenada_y_actual) == False:
                            copia.addEnd(coordenada_x_actual, coordenada_y_actual)
                            caminosRescate(coordenada_x_actual, coordenada_y_actual, destino, copia, camino_completado, plano)
                        else:
                            #Ya fue visitado no se agrega el nodo a la lista
                            pass    
                    except:
                        #print(e)
                        pass   

#Actualiza la lista de ciudades, sus contadores y los contadores de los nodos de la lista.
def actualizarListaCiudades(listaCiudad, nodoCiudad, tipo_actualizacion):
    if tipo_actualizacion == 'Rescate':
        nuevo_contador_unidades_civiles = nodoCiudad.getContadorUnidadesCiviles() - 1 #Resta uno al contador de unidades civiles de la ciudad
        contador_unidades_recursos = nodoCiudad.getContadorRecursos() #La cantidad de celdas Recursos que hay en la ciudad
        nodoCiudad.setContadorUnidadesCiviles(nuevo_contador_unidades_civiles)#Actualiza el contador de unidades civiles de la ciudad
        actualizado_contador_unidades_civiles = nodoCiudad.getContadorUnidadesCiviles()#El valor del contador de unidades civiles actualizado
        if actualizado_contador_unidades_civiles == 0:#Si ya no hay unidades civiles en la ciudad
            print('> No hay más unidades civiles por rescatar en la ciudad')
            nuevo_contador_ciudades_civiles = listaCiudad.getContadorCiudadesCiviles() - 1 #Resta uno al contador de ciudades que tiene unidades civiles de la lista de ciudades
            listaCiudad.setContadorCiudadesCiviles(nuevo_contador_ciudades_civiles)#Actualiza el contador
            actualizado_contador_ciudades_civiles = listaCiudad.getContadorCiudadesCiviles()# Obtiene el contador actualizado
            if actualizado_contador_ciudades_civiles == 0 and contador_unidades_recursos == 0: #Si la ciuad ya no tenia unidades recursos
                #Ya no se puede realizar ningún tipo de misión en la ciudad
                #se elimina de la lista
                print('> La ciudad está limpia')
                listaCiudad.deleteCiudad(nodoCiudad.getNombre())
            else:
                print('> Pero aún hay recursos por extraer de la ciudad')
                #Ya no tiene celdas de unidades civiles, pero tiene celdas de Recursos
                pass
        else:
            print('> Todavía hay uniades civiles por rescatar en la ciudad')
            #Aún existen más unidades civiles en la ciudad.
            pass     


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
                    print('> Carga de datos exitosa')
                except:
                    print('> Algo salió mal y no es posible completar la lectura del archivo')
            else:
                print('> No se cargó ningún archivo')       
        elif opt == 2:
            robot = None #Robot con el que se va a realizar la misión
            ciudad = None #Ciudad donde se va a realizar la misión
            punto_de_entrada = None #Punto de entrada a utilizar, en la ciudad seleccionada
            unidad_civil = None #Unidad Civil a rescatar en la ciudad seleccionada
            if Robots.getContadorRescue() > 0:
                if Robots.getContadorRescue() == 1:#Solo hay un chapinRescue en la lista
                    robot = Robots.getPrimero('ChapinRescue')
                    if Ciudades.getContadorCiudadesCiviles() > 0:
                        if Ciudades.getContadorCiudadesCiviles() == 1:
                            ciudad = Ciudades.getPrimero('UnidadCivil')
                            res = Ciudades.showMapa(ciudad.getNombre(), ciudad.getColumnas(), 'Rescate') #Hace la gráfica
                            if res == True:#Si retorna True -> todo salió bien
                                #Convierte la grafica de .dot a .svg y la abre automáticamente
                                archivo_nombre_dot = 'Ciudad_'+ciudad.getNombre()+'_Rescate.dot'
                                archivo_nombre_svg = 'Ciudad_'+ciudad.getNombre()+'_Rescate.svg'
                                system('dot -Tsvg {} -o {}'.format(archivo_nombre_dot, archivo_nombre_svg))
                                startfile(archivo_nombre_svg)
                            else:#Si hubo error al graficar
                                print('> No es posible mostrar gráficamente esta ciudad')

                            if ciudad.getContadorPuntosDeEntrada() == 1:#Solo hay un punto de entrada en la ciudad
                                punto_de_entrada = ciudad.mapa.getPrimero('PuntoEntrada')#Se obtiene directamente de la matriz sin preguntar al usuario
                                if ciudad.getContadorUnidadesCiviles() == 1:#Solo hay una unidad civil en la ciudad
                                    unidad_civil = ciudad.mapa.getPrimero('UnidadCivil')#Se obtiene directamente de la matriz sin preguntar al usuario
                                    
                                    ########################################## Ejecutar misión
                                    resultado = buscarCaminoRescate(punto_de_entrada, unidad_civil, ciudad.mapa)
                                    if resultado is not None: #Si encontro un camino para completar la misión
                                        coordenada_x = unidad_civil.getCoordenadaX()#Coordenada X de la unidad civil que se está rescatando
                                        coordenada_y = unidad_civil.getCoordenadaY()#Coordenada Y de la unidad civil que se está rescatando
                                        coordenadas_unidad_civil = str(coordenada_x) + ',' + str(coordenada_y)#Para enviar por parámetro
                                        capacidad_final = 0 #Capacidad de combate del robot, para ChapinRescue siempre es cero, al igual que la inicial.
                                        #Genera la gráfica
                                        res = Ciudades.showMisionRescate(ciudad.getNombre(), 'Rescate', coordenadas_unidad_civil, robot.getNombre(), robot.getCapacidadCombate(), capacidad_final, ciudad.getColumnas(), resultado)
                                        if res == True:#Todo salio bien
                                            #Convierte el archivo '.dot' a '.svg' y lo abre automáticamente
                                            print('> Misión Completada')
                                            archivo_nombre_dot = 'Ciudad_'+ciudad.getNombre()+'_Rescate.dot'
                                            archivo_nombre_svg = 'Ciudad_'+ciudad.getNombre()+'_Rescate.svg'
                                            system('dot -Tsvg {} -o {}'.format(archivo_nombre_dot, archivo_nombre_svg))
                                            startfile(archivo_nombre_svg)
                                            #La celda donde estaba la unidad civil pasa a ser una celda de tipo 'Camino'
                                            unidad_civil.setTipo('Camino')
                                            unidad_civil.setEstado(True)
                                            #Actualiza la info de la lista de ciudades y de la ciudad
                                            actualizarListaCiudades(Ciudades, ciudad, 'Rescate')
                                        else:
                                            print('> No es posible mostrar gráficamente esta ciudad')
                                    else:
                                        print('> Misión Imposible')

                                else:
                                    ciudad.mapa.showUnidadesCiviles()
                                    print()
                                    #Pregunta al usuario las coordenadas de la unidad civil que quiere rescatar
                                    unidad_civil = preguntarCoordenadas(ciudad, 'UnidadCivil')
                                    
                                    ########################################## Ejecutar misión
                                    resultado = buscarCaminoRescate(punto_de_entrada, unidad_civil, ciudad.mapa)
                                    if resultado is not None:
                                        coordenada_x = unidad_civil.getCoordenadaX()
                                        coordenada_y = unidad_civil.getCoordenadaY()
                                        coordenadas_unidad_civil = str(coordenada_x) + ',' + str(coordenada_y)
                                        capacidad_final = 0
                                        #Genera la gráfica
                                        res = Ciudades.showMisionRescate(ciudad.getNombre(), 'Rescate', coordenadas_unidad_civil, robot.getNombre(), robot.getCapacidadCombate(), capacidad_final, ciudad.getColumnas(), resultado)
                                        if res == True:#Todo salio bien
                                            #Convierte el archivo '.dot' a '.svg' y lo abre automáticamente
                                            print('> Misión Completada')
                                            archivo_nombre_dot = 'Ciudad_'+ciudad.getNombre()+'_Rescate.dot'
                                            archivo_nombre_svg = 'Ciudad_'+ciudad.getNombre()+'_Rescate.svg'
                                            system('dot -Tsvg {} -o {}'.format(archivo_nombre_dot, archivo_nombre_svg))
                                            startfile(archivo_nombre_svg)
                                            #La celda donde estaba la unidad civil pasa a ser una celda de tipo 'Camino'
                                            unidad_civil.setTipo('Camino')
                                            unidad_civil.setEstado(True)
                                            #Actualiza la info de la lista de ciudades y de la ciudad
                                            actualizarListaCiudades(Ciudades, ciudad, 'Rescate')
                                        else:
                                            print('> No es posible mostrar gráficamente esta ciudad')
                                    else:
                                        print('> Misión Imposible')

                            else:
                                ciudad.mapa.showPuntosDeEntrada()
                                print()
                                punto_de_entrada = preguntarCoordenadas(ciudad, 'PuntoEntrada')
                                if ciudad.getContadorUnidadesCiviles() == 1:
                                    unidad_civil = ciudad.mapa.getPrimero('UnidadCivil')

                                    ########################################## Ejecutar misión
                                    #funcion_uno(punto_de_entrada, unidad_civil, ciudad.mapa)
                                    resultado = buscarCaminoRescate(punto_de_entrada, unidad_civil, ciudad.mapa)
                                    if resultado is not None: #Si encontro un camino para completar la misión
                                        coordenada_x = unidad_civil.getCoordenadaX()#Coordenada X de la unidad civil que se está rescatando
                                        coordenada_y = unidad_civil.getCoordenadaY()#Coordenada Y de la unidad civil que se está rescatando
                                        coordenadas_unidad_civil = str(coordenada_x) + ',' + str(coordenada_y)#Para enviar por parámetro
                                        capacidad_final = 0 #Capacidad de combate del robot, para ChapinRescue siempre es cero, al igual que la inicial.
                                        #Genera la gráfica
                                        res = Ciudades.showMisionRescate(ciudad.getNombre(), 'Rescate', coordenadas_unidad_civil, robot.getNombre(), robot.getCapacidadCombate(), capacidad_final, ciudad.getColumnas(), resultado)
                                        if res == True:#Todo salio bien
                                            #Convierte el archivo '.dot' a '.svg' y lo abre automáticamente
                                            print('> Misión Completada')
                                            archivo_nombre_dot = 'Ciudad_'+ciudad.getNombre()+'_Rescate.dot'
                                            archivo_nombre_svg = 'Ciudad_'+ciudad.getNombre()+'_Rescate.svg'
                                            system('dot -Tsvg {} -o {}'.format(archivo_nombre_dot, archivo_nombre_svg))
                                            startfile(archivo_nombre_svg)
                                            #La celda donde estaba la unidad civil pasa a ser una celda de tipo 'Camino'
                                            unidad_civil.setTipo('Camino')
                                            unidad_civil.setEstado(True)
                                            #Actualiza la info de la lista de ciudades y de la ciudad
                                            actualizarListaCiudades(Ciudades, ciudad, 'Rescate')
                                        else:
                                            print('> No es posible mostrar gráficamente esta ciudad')
                                    else:
                                        print('> Misión Imposible')
                               
                                else:
                                    ciudad.mapa.showUnidadesCiviles()
                                    print()
                                    unidad_civil = preguntarCoordenadas(ciudad, 'UnidadCivil')

                                    ########################################## Ejecutar misión                                
                                    resultado = buscarCaminoRescate(punto_de_entrada, unidad_civil, ciudad.mapa)
                                    if resultado is not None: #Si encontro un camino para completar la misión
                                        coordenada_x = unidad_civil.getCoordenadaX()
                                        coordenada_y = unidad_civil.getCoordenadaY()
                                        coordenadas_unidad_civil = str(coordenada_x) + ',' + str(coordenada_y)
                                        capacidad_final = 0
                                        #Genera la gráfica
                                        res = Ciudades.showMisionRescate(ciudad.getNombre(), 'Rescate', coordenadas_unidad_civil, robot.getNombre(), robot.getCapacidadCombate(), capacidad_final, ciudad.getColumnas(), resultado)
                                        if res == True:#Todo salio bien
                                            #Convierte el archivo '.dot' a '.svg' y lo abre automáticamente
                                            print('> Misión Completada')
                                            archivo_nombre_dot = 'Ciudad_'+ciudad.getNombre()+'_Rescate.dot'
                                            archivo_nombre_svg = 'Ciudad_'+ciudad.getNombre()+'_Rescate.svg'
                                            system('dot -Tsvg {} -o {}'.format(archivo_nombre_dot, archivo_nombre_svg))
                                            startfile(archivo_nombre_svg)
                                            #La celda donde estaba la unidad civil pasa a ser una celda de tipo 'Camino'
                                            unidad_civil.setTipo('Camino')
                                            unidad_civil.setEstado(True)
                                            #Actualiza la info de la lista de ciudades y de la ciudad
                                            actualizarListaCiudades(Ciudades, ciudad, 'Rescate')
                                        else:
                                            print('> No es posible mostrar gráficamente esta ciudad')
                                    else:
                                        print('> Misión Imposible')                        

                        else:
                            Ciudades.showCiudadesCiviles()
                            print()
                            nombre = str(input('> Ingresa el nombre de la ciudad: \n'))#Pregunta el nombre de la ciudad donde se va a realizar la misión
                            ciudad = Ciudades.searchCiudad(nombre)#Obtiene la ciudad
                            res = Ciudades.showMapa(ciudad.getNombre(), ciudad.getColumnas(), 'Rescate')
                            if res == True:
                                #Convierte la grafica de .dot a .svg y la abre automáticamente
                                archivo_nombre_dot = 'Ciudad_'+ciudad.getNombre()+'_Rescate.dot'
                                archivo_nombre_svg = 'Ciudad_'+ciudad.getNombre()+'_Rescate.svg'
                                system('dot -Tsvg {} -o {}'.format(archivo_nombre_dot, archivo_nombre_svg))
                                startfile(archivo_nombre_svg)
                            else:
                                print('> No es posible mostrar gráficamente esta ciudad')                                
                            
                            if ciudad.getContadorPuntosDeEntrada() == 1:#Solo hay un punto de entrada en la ciudad
                                punto_de_entrada = ciudad.mapa.getPrimero('PuntoEntrada')#Se obtiene directamente de la matriz sin preguntar al usuario
                                if ciudad.getContadorUnidadesCiviles() == 1:#Solo hay una unidad civil en la ciudad
                                    unidad_civil = ciudad.mapa.getPrimero('UnidadCivil')#Se obtiene directamente de la matriz sin preguntar al usuario
                                    
                                    ########################################## Ejecutar misión                                
                                    resultado = buscarCaminoRescate(punto_de_entrada, unidad_civil, ciudad.mapa)
                                    if resultado is not None: #Si encontro un camino para completar la misión
                                        coordenada_x = unidad_civil.getCoordenadaX()
                                        coordenada_y = unidad_civil.getCoordenadaY()
                                        coordenadas_unidad_civil = str(coordenada_x) + ',' + str(coordenada_y)
                                        capacidad_final = 0
                                        #Genera la gráfica
                                        res = Ciudades.showMisionRescate(ciudad.getNombre(), 'Rescate', coordenadas_unidad_civil, robot.getNombre(), robot.getCapacidadCombate(), capacidad_final, ciudad.getColumnas(), resultado)
                                        if res == True:#Todo salio bien
                                            #Convierte el archivo '.dot' a '.svg' y lo abre automáticamente
                                            print('> Misión Completada')
                                            archivo_nombre_dot = 'Ciudad_'+ciudad.getNombre()+'_Rescate.dot'
                                            archivo_nombre_svg = 'Ciudad_'+ciudad.getNombre()+'_Rescate.svg'
                                            system('dot -Tsvg {} -o {}'.format(archivo_nombre_dot, archivo_nombre_svg))
                                            startfile(archivo_nombre_svg)
                                            #La celda donde estaba la unidad civil pasa a ser una celda de tipo 'Camino'
                                            unidad_civil.setTipo('Camino')
                                            unidad_civil.setEstado(True)
                                            #Actualiza la info de la lista de ciudades y de la ciudad
                                            actualizarListaCiudades(Ciudades, ciudad, 'Rescate')
                                        else:
                                            print('> No es posible mostrar gráficamente esta ciudad')
                                    else:
                                        print('> Misión Imposible')                        

                                else:
                                    ciudad.mapa.showUnidadesCiviles()
                                    print()
                                    unidad_civil = preguntarCoordenadas(ciudad, 'UnidadCivil')
                                    
                                    ########################################## Ejecutar misión                                
                                    resultado = buscarCaminoRescate(punto_de_entrada, unidad_civil, ciudad.mapa)
                                    if resultado is not None: #Si encontro un camino para completar la misión
                                        coordenada_x = unidad_civil.getCoordenadaX()
                                        coordenada_y = unidad_civil.getCoordenadaY()
                                        coordenadas_unidad_civil = str(coordenada_x) + ',' + str(coordenada_y)
                                        capacidad_final = 0
                                        #Genera la gráfica
                                        res = Ciudades.showMisionRescate(ciudad.getNombre(), 'Rescate', coordenadas_unidad_civil, robot.getNombre(), robot.getCapacidadCombate(), capacidad_final, ciudad.getColumnas(), resultado)
                                        if res == True:#Todo salio bien
                                            #Convierte el archivo '.dot' a '.svg' y lo abre automáticamente
                                            print('> Misión Completada')
                                            archivo_nombre_dot = 'Ciudad_'+ciudad.getNombre()+'_Rescate.dot'
                                            archivo_nombre_svg = 'Ciudad_'+ciudad.getNombre()+'_Rescate.svg'
                                            system('dot -Tsvg {} -o {}'.format(archivo_nombre_dot, archivo_nombre_svg))
                                            startfile(archivo_nombre_svg)
                                            #La celda donde estaba la unidad civil pasa a ser una celda de tipo 'Camino'
                                            unidad_civil.setTipo('Camino')
                                            unidad_civil.setEstado(True)
                                            #Actualiza la info de la lista de ciudades y de la ciudad
                                            actualizarListaCiudades(Ciudades, ciudad, 'Rescate')
                                        else:
                                            print('> No es posible mostrar gráficamente esta ciudad')
                                    else:
                                        print('> Misión Imposible')                        
                            
                            else:                          
                                ciudad.mapa.showPuntosDeEntrada()
                                print()
                                punto_de_entrada = preguntarCoordenadas(ciudad, 'PuntoEntrada')
                                if ciudad.getContadorUnidadesCiviles() == 1:
                                    unidad_civil = ciudad.mapa.getPrimero('UnidadCivil')
                                   
                                    ########################################## Ejecutar misión                                
                                    resultado = buscarCaminoRescate(punto_de_entrada, unidad_civil, ciudad.mapa)
                                    if resultado is not None: #Si encontro un camino para completar la misión
                                        coordenada_x = unidad_civil.getCoordenadaX()
                                        coordenada_y = unidad_civil.getCoordenadaY()
                                        coordenadas_unidad_civil = str(coordenada_x) + ',' + str(coordenada_y)
                                        capacidad_final = 0
                                        #Genera la gráfica
                                        res = Ciudades.showMisionRescate(ciudad.getNombre(), 'Rescate', coordenadas_unidad_civil, robot.getNombre(), robot.getCapacidadCombate(), capacidad_final, ciudad.getColumnas(), resultado)
                                        if res == True:#Todo salio bien
                                            #Convierte el archivo '.dot' a '.svg' y lo abre automáticamente
                                            print('> Misión Completada')
                                            archivo_nombre_dot = 'Ciudad_'+ciudad.getNombre()+'_Rescate.dot'
                                            archivo_nombre_svg = 'Ciudad_'+ciudad.getNombre()+'_Rescate.svg'
                                            system('dot -Tsvg {} -o {}'.format(archivo_nombre_dot, archivo_nombre_svg))
                                            startfile(archivo_nombre_svg)
                                            #La celda donde estaba la unidad civil pasa a ser una celda de tipo 'Camino'
                                            unidad_civil.setTipo('Camino')
                                            unidad_civil.setEstado(True)
                                            #Actualiza la info de la lista de ciudades y de la ciudad
                                            actualizarListaCiudades(Ciudades, ciudad, 'Rescate')
                                        else:
                                            print('> No es posible mostrar gráficamente esta ciudad')
                                    else:
                                        print('> Misión Imposible')                        

                                else:
                                    ciudad.mapa.showUnidadesCiviles()
                                    print()
                                    unidad_civil = preguntarCoordenadas(ciudad, 'UnidadCivil')
                                    ########################################## Ejecutar misión                                
                                    resultado = buscarCaminoRescate(punto_de_entrada, unidad_civil, ciudad.mapa)
                                    if resultado is not None: #Si encontro un camino para completar la misión
                                        coordenada_x = unidad_civil.getCoordenadaX()
                                        coordenada_y = unidad_civil.getCoordenadaY()
                                        coordenadas_unidad_civil = str(coordenada_x) + ',' + str(coordenada_y)
                                        capacidad_final = 0
                                        #Genera la gráfica
                                        res = Ciudades.showMisionRescate(ciudad.getNombre(), 'Rescate', coordenadas_unidad_civil, robot.getNombre(), robot.getCapacidadCombate(), capacidad_final, ciudad.getColumnas(), resultado)
                                        if res == True:#Todo salio bien
                                            #Convierte el archivo '.dot' a '.svg' y lo abre automáticamente
                                            print('> Misión Completada')
                                            archivo_nombre_dot = 'Ciudad_'+ciudad.getNombre()+'_Rescate.dot'
                                            archivo_nombre_svg = 'Ciudad_'+ciudad.getNombre()+'_Rescate.svg'
                                            system('dot -Tsvg {} -o {}'.format(archivo_nombre_dot, archivo_nombre_svg))
                                            startfile(archivo_nombre_svg)
                                            #La celda donde estaba la unidad civil pasa a ser una celda de tipo 'Camino'
                                            unidad_civil.setTipo('Camino')
                                            unidad_civil.setEstado(True)
                                            #Actualiza la info de la lista de ciudades y de la ciudad
                                            actualizarListaCiudades(Ciudades, ciudad, 'Rescate')
                                        else:
                                            print('> No es posible mostrar gráficamente esta ciudad')
                                    else:
                                        print('> Misión Imposible')                        

                    else:
                        print('> La misión de rescate no es posible, no hay ciudades con unidades civiles')
                else:
                    Robots.showChapinRescue()
                    print()
                    nombre = str(input('Ingresa el nombre del robot a utilizar: \n'))
                    robot = Robots.searchRobot(nombre, 'ChapinRescue')#Obtiene el robot a utilizar
                    if Ciudades.getContadorCiudadesCiviles() > 0:
                        if Ciudades.getContadorCiudadesCiviles() == 1:
                            ciudad = Ciudades.getPrimero('UnidadCivil')
                            res = Ciudades.showMapa(ciudad.getNombre(), ciudad.getColumnas(), 'Rescate')
                            if res == True:
                                #Convierte la grafica de .dot a .svg y la abre automáticamente
                                archivo_nombre_dot = 'Ciudad_'+ciudad.getNombre()+'_Rescate.dot'
                                archivo_nombre_svg = 'Ciudad_'+ciudad.getNombre()+'_Rescate.svg'
                                system('dot -Tsvg {} -o {}'.format(archivo_nombre_dot, archivo_nombre_svg))
                                startfile(archivo_nombre_svg)
                            else:
                                print('> No es posible mostrar gráficamente esta ciudad')
                            
                            if ciudad.getContadorPuntosDeEntrada() == 1:#Solo hay un punto de entrada en la ciudad
                                punto_de_entrada = ciudad.mapa.getPrimero('PuntoEntrada')#Se obtiene directamente de la matriz sin preguntar al usuario
                                if ciudad.getContadorUnidadesCiviles() == 1:#Solo hay una unidad civil en la ciudad
                                    unidad_civil = ciudad.mapa.getPrimero('UnidadCivil')#Se obtiene directamente de la matriz sin preguntar al usuario

                                    ########################################## Ejecutar misión                                
                                    resultado = buscarCaminoRescate(punto_de_entrada, unidad_civil, ciudad.mapa)
                                    if resultado is not None: #Si encontro un camino para completar la misión
                                        coordenada_x = unidad_civil.getCoordenadaX()
                                        coordenada_y = unidad_civil.getCoordenadaY()
                                        coordenadas_unidad_civil = str(coordenada_x) + ',' + str(coordenada_y)
                                        capacidad_final = 0
                                        #Genera la gráfica
                                        res = Ciudades.showMisionRescate(ciudad.getNombre(), 'Rescate', coordenadas_unidad_civil, robot.getNombre(), robot.getCapacidadCombate(), capacidad_final, ciudad.getColumnas(), resultado)
                                        if res == True:#Todo salio bien
                                            #Convierte el archivo '.dot' a '.svg' y lo abre automáticamente
                                            print('> Misión Completada')
                                            archivo_nombre_dot = 'Ciudad_'+ciudad.getNombre()+'_Rescate.dot'
                                            archivo_nombre_svg = 'Ciudad_'+ciudad.getNombre()+'_Rescate.svg'
                                            system('dot -Tsvg {} -o {}'.format(archivo_nombre_dot, archivo_nombre_svg))
                                            startfile(archivo_nombre_svg)
                                            #La celda donde estaba la unidad civil pasa a ser una celda de tipo 'Camino'
                                            unidad_civil.setTipo('Camino')
                                            unidad_civil.setEstado(True)
                                            #Actualiza la info de la lista de ciudades y de la ciudad
                                            actualizarListaCiudades(Ciudades, ciudad, 'Rescate')
                                        else:
                                            print('> No es posible mostrar gráficamente esta ciudad')
                                    else:
                                        print('> Misión Imposible')                        

                                else:
                                    ciudad.mapa.showUnidadesCiviles()
                                    print()
                                    #Pregunta al usuario las coordenadas de la unidad civil que quiere rescatar
                                    unidad_civil = preguntarCoordenadas(ciudad, 'UnidadCivil')
                                   
                                    ########################################## Ejecutar misión                                
                                    resultado = buscarCaminoRescate(punto_de_entrada, unidad_civil, ciudad.mapa)
                                    if resultado is not None: #Si encontro un camino para completar la misión
                                        coordenada_x = unidad_civil.getCoordenadaX()
                                        coordenada_y = unidad_civil.getCoordenadaY()
                                        coordenadas_unidad_civil = str(coordenada_x) + ',' + str(coordenada_y)
                                        capacidad_final = 0
                                        #Genera la gráfica
                                        res = Ciudades.showMisionRescate(ciudad.getNombre(), 'Rescate', coordenadas_unidad_civil, robot.getNombre(), robot.getCapacidadCombate(), capacidad_final, ciudad.getColumnas(), resultado)
                                        if res == True:#Todo salio bien
                                            #Convierte el archivo '.dot' a '.svg' y lo abre automáticamente
                                            print('> Misión Completada')
                                            archivo_nombre_dot = 'Ciudad_'+ciudad.getNombre()+'_Rescate.dot'
                                            archivo_nombre_svg = 'Ciudad_'+ciudad.getNombre()+'_Rescate.svg'
                                            system('dot -Tsvg {} -o {}'.format(archivo_nombre_dot, archivo_nombre_svg))
                                            startfile(archivo_nombre_svg)
                                            #La celda donde estaba la unidad civil pasa a ser una celda de tipo 'Camino'
                                            unidad_civil.setTipo('Camino')
                                            unidad_civil.setEstado(True)
                                            #Actualiza la info de la lista de ciudades y de la ciudad
                                            actualizarListaCiudades(Ciudades, ciudad, 'Rescate')
                                        else:
                                            print('> No es posible mostrar gráficamente esta ciudad')
                                    else:
                                        print('> Misión Imposible')                        
                            
                            else:
                                ciudad.mapa.showPuntosDeEntrada()
                                print()
                                punto_de_entrada = preguntarCoordenadas(ciudad, 'PuntoEntrada')
                                if ciudad.getContadorUnidadesCiviles() == 1:
                                    unidad_civil = ciudad.mapa.getPrimero('UnidadCivil')
                                    ########################################## Ejecutar misión                                
                                    resultado = buscarCaminoRescate(punto_de_entrada, unidad_civil, ciudad.mapa)
                                    if resultado is not None: #Si encontro un camino para completar la misión
                                        coordenada_x = unidad_civil.getCoordenadaX()
                                        coordenada_y = unidad_civil.getCoordenadaY()
                                        coordenadas_unidad_civil = str(coordenada_x) + ',' + str(coordenada_y)
                                        capacidad_final = 0
                                        #Genera la gráfica
                                        res = Ciudades.showMisionRescate(ciudad.getNombre(), 'Rescate', coordenadas_unidad_civil, robot.getNombre(), robot.getCapacidadCombate(), capacidad_final, ciudad.getColumnas(), resultado)
                                        if res == True:#Todo salio bien
                                            #Convierte el archivo '.dot' a '.svg' y lo abre automáticamente
                                            print('> Misión Completada')
                                            archivo_nombre_dot = 'Ciudad_'+ciudad.getNombre()+'_Rescate.dot'
                                            archivo_nombre_svg = 'Ciudad_'+ciudad.getNombre()+'_Rescate.svg'
                                            system('dot -Tsvg {} -o {}'.format(archivo_nombre_dot, archivo_nombre_svg))
                                            startfile(archivo_nombre_svg)
                                            #La celda donde estaba la unidad civil pasa a ser una celda de tipo 'Camino'
                                            unidad_civil.setTipo('Camino')
                                            unidad_civil.setEstado(True)
                                            #Actualiza la info de la lista de ciudades y de la ciudad
                                            actualizarListaCiudades(Ciudades, ciudad, 'Rescate')
                                        else:
                                            print('> No es posible mostrar gráficamente esta ciudad')
                                    else:
                                        print('> Misión Imposible')                        
                                
                                else:
                                    ciudad.mapa.showUnidadesCiviles()
                                    print()
                                    unidad_civil = preguntarCoordenadas(ciudad, 'UnidadCivil')
                                    ########################################## Ejecutar misión                                
                                    resultado = buscarCaminoRescate(punto_de_entrada, unidad_civil, ciudad.mapa)
                                    if resultado is not None: #Si encontro un camino para completar la misión
                                        coordenada_x = unidad_civil.getCoordenadaX()
                                        coordenada_y = unidad_civil.getCoordenadaY()
                                        coordenadas_unidad_civil = str(coordenada_x) + ',' + str(coordenada_y)
                                        capacidad_final = 0
                                        #Genera la gráfica
                                        res = Ciudades.showMisionRescate(ciudad.getNombre(), 'Rescate', coordenadas_unidad_civil, robot.getNombre(), robot.getCapacidadCombate(), capacidad_final, ciudad.getColumnas(), resultado)
                                        if res == True:#Todo salio bien
                                            #Convierte el archivo '.dot' a '.svg' y lo abre automáticamente
                                            print('> Misión Completada')
                                            archivo_nombre_dot = 'Ciudad_'+ciudad.getNombre()+'_Rescate.dot'
                                            archivo_nombre_svg = 'Ciudad_'+ciudad.getNombre()+'_Rescate.svg'
                                            system('dot -Tsvg {} -o {}'.format(archivo_nombre_dot, archivo_nombre_svg))
                                            startfile(archivo_nombre_svg)
                                            #La celda donde estaba la unidad civil pasa a ser una celda de tipo 'Camino'
                                            unidad_civil.setTipo('Camino')
                                            unidad_civil.setEstado(True)
                                            #Actualiza la info de la lista de ciudades y de la ciudad
                                            actualizarListaCiudades(Ciudades, ciudad, 'Rescate')
                                        else:
                                            print('> No es posible mostrar gráficamente esta ciudad')
                                    else:
                                        print('> Misión Imposible')                        
                               
                        else:
                            Ciudades.showCiudadesCiviles()
                            print()
                            nombre = str(input('Ingresa el nombre de la ciudad: \n'))#Pregunta el nombre de la ciudad donde se va a realizar la misión
                            ciudad = Ciudades.searchCiudad(nombre)#Obtiene la ciudad
                            res = Ciudades.showMapa(ciudad.getNombre(), ciudad.getColumnas(), 'Rescate')
                            if res == True:
                                #Convierte la grafica de .dot a .svg y la abre automáticamente
                                archivo_nombre_dot = 'Ciudad_'+ciudad.getNombre()+'_Rescate.dot'
                                archivo_nombre_svg = 'Ciudad_'+ciudad.getNombre()+'_Rescate.svg'
                                system('dot -Tsvg {} -o {}'.format(archivo_nombre_dot, archivo_nombre_svg))
                                startfile(archivo_nombre_svg)
                            else:
                                print('> No es posible mostrar gráficamente esta ciudad')
                           
                            if ciudad.getContadorPuntosDeEntrada() == 1:#Solo hay un punto de entrada en la ciudad
                                punto_de_entrada = ciudad.mapa.getPrimero('PuntoEntrada')#Se obtiene directamente de la matriz sin preguntar al usuario
                                if ciudad.getContadorUnidadesCiviles() == 1:#Solo hay una unidad civil en la ciudad
                                    unidad_civil = ciudad.mapa.getPrimero('UnidadCivil')#Se obtiene directamente de la matriz sin preguntar al usuario
                                    ########################################## Ejecutar misión                                
                                    resultado = buscarCaminoRescate(punto_de_entrada, unidad_civil, ciudad.mapa)
                                    if resultado is not None: #Si encontro un camino para completar la misión
                                        coordenada_x = unidad_civil.getCoordenadaX()
                                        coordenada_y = unidad_civil.getCoordenadaY()
                                        coordenadas_unidad_civil = str(coordenada_x) + ',' + str(coordenada_y)
                                        capacidad_final = 0
                                        #Genera la gráfica
                                        res = Ciudades.showMisionRescate(ciudad.getNombre(), 'Rescate', coordenadas_unidad_civil, robot.getNombre(), robot.getCapacidadCombate(), capacidad_final, ciudad.getColumnas(), resultado)
                                        if res == True:#Todo salio bien
                                            #Convierte el archivo '.dot' a '.svg' y lo abre automáticamente
                                            print('> Misión Completada')
                                            archivo_nombre_dot = 'Ciudad_'+ciudad.getNombre()+'_Rescate.dot'
                                            archivo_nombre_svg = 'Ciudad_'+ciudad.getNombre()+'_Rescate.svg'
                                            system('dot -Tsvg {} -o {}'.format(archivo_nombre_dot, archivo_nombre_svg))
                                            startfile(archivo_nombre_svg)
                                            #La celda donde estaba la unidad civil pasa a ser una celda de tipo 'Camino'
                                            unidad_civil.setTipo('Camino')
                                            unidad_civil.setEstado(True)
                                            #Actualiza la info de la lista de ciudades y de la ciudad
                                            actualizarListaCiudades(Ciudades, ciudad, 'Rescate')
                                        else:
                                            print('> No es posible mostrar gráficamente esta ciudad')
                                    else:
                                        print('> Misión Imposible')                        
                               
                                else:
                                    ciudad.mapa.showUnidadesCiviles()
                                    print()
                                    unidad_civil = preguntarCoordenadas(ciudad, 'UnidadCivil')
                                    ########################################## Ejecutar misión                                
                                    resultado = buscarCaminoRescate(punto_de_entrada, unidad_civil, ciudad.mapa)
                                    if resultado is not None: #Si encontro un camino para completar la misión
                                        coordenada_x = unidad_civil.getCoordenadaX()
                                        coordenada_y = unidad_civil.getCoordenadaY()
                                        coordenadas_unidad_civil = str(coordenada_x) + ',' + str(coordenada_y)
                                        capacidad_final = 0
                                        #Genera la gráfica
                                        res = Ciudades.showMisionRescate(ciudad.getNombre(), 'Rescate', coordenadas_unidad_civil, robot.getNombre(), robot.getCapacidadCombate(), capacidad_final, ciudad.getColumnas(), resultado)
                                        if res == True:#Todo salio bien
                                            #Convierte el archivo '.dot' a '.svg' y lo abre automáticamente
                                            print('> Misión Completada')
                                            archivo_nombre_dot = 'Ciudad_'+ciudad.getNombre()+'_Rescate.dot'
                                            archivo_nombre_svg = 'Ciudad_'+ciudad.getNombre()+'_Rescate.svg'
                                            system('dot -Tsvg {} -o {}'.format(archivo_nombre_dot, archivo_nombre_svg))
                                            startfile(archivo_nombre_svg)
                                            #La celda donde estaba la unidad civil pasa a ser una celda de tipo 'Camino'
                                            unidad_civil.setTipo('Camino')
                                            unidad_civil.setEstado(True)
                                            #Actualiza la info de la lista de ciudades y de la ciudad
                                            actualizarListaCiudades(Ciudades, ciudad, 'Rescate')
                                        else:
                                            print('> No es posible mostrar gráficamente esta ciudad')
                                    else:
                                        print('> Misión Imposible')                        

                            else:                          
                                ciudad.mapa.showPuntosDeEntrada()
                                print()
                                punto_de_entrada = preguntarCoordenadas(ciudad, 'PuntoEntrada')
                                if ciudad.getContadorUnidadesCiviles() == 1:
                                    unidad_civil = ciudad.mapa.getPrimero('UnidadCivil')
                                    ########################################## Ejecutar misión                                
                                    resultado = buscarCaminoRescate(punto_de_entrada, unidad_civil, ciudad.mapa)
                                    if resultado is not None: #Si encontro un camino para completar la misión
                                        coordenada_x = unidad_civil.getCoordenadaX()
                                        coordenada_y = unidad_civil.getCoordenadaY()
                                        coordenadas_unidad_civil = str(coordenada_x) + ',' + str(coordenada_y)
                                        capacidad_final = 0
                                        #Genera la gráfica
                                        res = Ciudades.showMisionRescate(ciudad.getNombre(), 'Rescate', coordenadas_unidad_civil, robot.getNombre(), robot.getCapacidadCombate(), capacidad_final, ciudad.getColumnas(), resultado)
                                        if res == True:#Todo salio bien
                                            #Convierte el archivo '.dot' a '.svg' y lo abre automáticamente
                                            print('> Misión Completada')
                                            archivo_nombre_dot = 'Ciudad_'+ciudad.getNombre()+'_Rescate.dot'
                                            archivo_nombre_svg = 'Ciudad_'+ciudad.getNombre()+'_Rescate.svg'
                                            system('dot -Tsvg {} -o {}'.format(archivo_nombre_dot, archivo_nombre_svg))
                                            startfile(archivo_nombre_svg)
                                            #La celda donde estaba la unidad civil pasa a ser una celda de tipo 'Camino'
                                            unidad_civil.setTipo('Camino')
                                            unidad_civil.setEstado(True)
                                            #Actualiza la info de la lista de ciudades y de la ciudad
                                            actualizarListaCiudades(Ciudades, ciudad, 'Rescate')
                                        else:
                                            print('> No es posible mostrar gráficamente esta ciudad')
                                    else:
                                        print('> Misión Imposible')                        
                                
                                else:
                                    ciudad.mapa.showUnidadesCiviles()
                                    print()
                                    unidad_civil = preguntarCoordenadas(ciudad, 'UnidadCivil')
                                    ########################################## Ejecutar misión                                
                                    resultado = buscarCaminoRescate(punto_de_entrada, unidad_civil, ciudad.mapa)
                                    if resultado is not None: #Si encontro un camino para completar la misión
                                        coordenada_x = unidad_civil.getCoordenadaX()
                                        coordenada_y = unidad_civil.getCoordenadaY()
                                        coordenadas_unidad_civil = str(coordenada_x) + ',' + str(coordenada_y)
                                        capacidad_final = 0
                                        #Genera la gráfica
                                        res = Ciudades.showMisionRescate(ciudad.getNombre(), 'Rescate', coordenadas_unidad_civil, robot.getNombre(), robot.getCapacidadCombate(), capacidad_final, ciudad.getColumnas(), resultado)
                                        if res == True:#Todo salio bien
                                            #Convierte el archivo '.dot' a '.svg' y lo abre automáticamente
                                            print('> Misión Completada')
                                            archivo_nombre_dot = 'Ciudad_'+ciudad.getNombre()+'_Rescate.dot'
                                            archivo_nombre_svg = 'Ciudad_'+ciudad.getNombre()+'_Rescate.svg'
                                            system('dot -Tsvg {} -o {}'.format(archivo_nombre_dot, archivo_nombre_svg))
                                            startfile(archivo_nombre_svg)
                                            #La celda donde estaba la unidad civil pasa a ser una celda de tipo 'Camino'
                                            unidad_civil.setTipo('Camino')
                                            unidad_civil.setEstado(True)
                                            #Actualiza la info de la lista de ciudades y de la ciudad
                                            actualizarListaCiudades(Ciudades, ciudad, 'Rescate')
                                        else:
                                            print('> No es posible mostrar gráficamente esta ciudad')
                                    else:
                                        print('> Misión Imposible')                        
    
                    else:
                        print('> La misión de rescate no es posible, no hay ciudades con unidades civiles')           
            else:
                print('> No es posible realizar esta misión, no hay robots ChapinRescue en el sistema')
        elif opt == 3:
            #Su funcionamiento es similar al de la función 2 del menú
            robot = None
            ciudad = None
            punto_de_entrada = None
            recurso = None
            if Robots.getContadorFighter() > 0:
                if Robots.getContadorFighter() == 1:
                    robot = Robots.getPrimero('ChapinFighter')
                    if Ciudades.getContadorCiudadesRecursos() > 0:
                        if Ciudades.getContadorCiudadesRecursos() == 1:
                            ciudad = Ciudades.getPrimero('Recurso')
                            res = Ciudades.showMapa(ciudad.getNombre(), ciudad.getColumnas(), 'Extraccion')
                            if res == True:#Si retorna True -> todo salió bien
                                #Convierte la grafica de .dot a .svg y la abre automáticamente
                                archivo_nombre_dot = 'Ciudad_'+ciudad.getNombre()+'_Extraccion.dot'
                                archivo_nombre_svg = 'Ciudad_'+ciudad.getNombre()+'_Extraccion.svg'
                                system('dot -Tsvg {} -o {}'.format(archivo_nombre_dot, archivo_nombre_svg))
                                startfile(archivo_nombre_svg)  
                            else:
                                print('> No es posible mostrar gráficamente esta ciudad')                              
                            if ciudad.getContadorPuntosDeEntrada() == 1:
                                punto_de_entrada = ciudad.mapa.getPrimero('PuntoEntrada')
                                if ciudad.getContadorRecursos() == 1:
                                    recurso = ciudad.mapa.getPrimero('Recurso')
                                    #Ejecutar misión
                                else:
                                    ciudad.mapa.showRecursos()
                                    print()
                                    #Pregunta al usuario las coordenadas del recurso a extraer
                                    recurso = preguntarCoordenadas(ciudad, 'Recurso')
                                    #Ejecutar misión
                            else:
                                #ciudad.mapa.showRecursos()
                                ciudad.mapa.showPuntosDeEntrada()
                                print()
                                punto_de_entrada = preguntarCoordenadas(ciudad, 'PuntoEntrada')
                                if ciudad.getContadorRecursos() == 1:
                                    recurso = ciudad.mapa.getPrimero('Recurso')
                                    #Ejecutar misión
                                else:
                                    ciudad.mapa.showRecursos()
                                    print()
                                    #Pregunta al usuario las coordenadas del recurso a extraer
                                    recurso = preguntarCoordenadas(ciudad, 'Recurso')
                                    #Ejecutar misión                                
                        else:
                            Ciudades.showCiudadesRecursos()
                            print()
                            nombre = str(input('> Ingresa el nombre de la ciudad: \n'))
                            ciudad = Ciudades.searchCiudad(nombre)
                            res = Ciudades.showMapa(ciudad.getNombre(), ciudad.getColumnas(), 'Extraccion')
                            if res == True:
                                #Convierte la grafica de .dot a .svg y la abre automáticamente
                                archivo_nombre_dot = 'Ciudad_'+ciudad.getNombre()+'_Extraccion.dot'
                                archivo_nombre_svg = 'Ciudad_'+ciudad.getNombre()+'_Extraccion.svg'
                                system('dot -Tsvg {} -o {}'.format(archivo_nombre_dot, archivo_nombre_svg))
                                startfile(archivo_nombre_svg)
                            else:
                                print('> No es posible mostrar gráficamente esta ciudad')
                            if ciudad.getContadorPuntosDeEntrada() == 1:
                                punto_de_entrada = ciudad.mapa.getPrimero('PuntoEntrada')
                                if ciudad.getContadorRecursos() == 1:
                                    recurso = ciudad.mapa.getPrimero('Recurso')
                                    #Ejecutar misión
                                else:
                                    ciudad.mapa.showRecursos()
                                    print()
                                    #Pregunta al usuario las coordenadas del recurso a extraer
                                    recurso = preguntarCoordenadas(ciudad, 'Recurso')
                                    #Ejecutar misión
                            else:
                                #ciudad.mapa.showRecursos()
                                ciudad.mapa.showPuntosDeEntrada()
                                print()
                                punto_de_entrada = preguntarCoordenadas(ciudad, 'PuntoEntrada')
                                if ciudad.getContadorRecursos() == 1:
                                    recurso = ciudad.mapa.getPrimero('Recurso')
                                    #Ejecutar misión
                                else:
                                    ciudad.mapa.showRecursos()
                                    print()
                                    #Pregunta al usuario las coordenadas del recurso a extraer
                                    recurso = preguntarCoordenadas(ciudad, 'Recurso')
                                    #Ejecutar misión                                
                    else:
                        print('> La misión de rescate no es posible, no hay ciudades con recursos por extraer')
                else:
                    Robots.showChapinFighter()
                    print()
                    nombre = str(input('> Ingresa el nombre del robot a utilizar: \n'))
                    robot = Robots.searchRobot(nombre, 'ChapinFighter')
                    if Ciudades.getContadorCiudadesRecursos() > 0:
                        if Ciudades.getContadorCiudadesRecursos() == 1:
                            ciudad = Ciudades.getPrimero('Recurso')
                            res = Ciudades.showMapa(ciudad.getNombre(), ciudad.getColumnas(), 'Extraccion')
                            if res == True:
                                #Convierte la grafica de .dot a .svg y la abre automáticamente
                                archivo_nombre_dot = 'Ciudad_'+ciudad.getNombre()+'_Extraccion.dot'
                                archivo_nombre_svg = 'Ciudad_'+ciudad.getNombre()+'_Extraccion.svg'
                                system('dot -Tsvg {} -o {}'.format(archivo_nombre_dot, archivo_nombre_svg))
                                startfile(archivo_nombre_svg)
                            else:
                                print('> No es posible mostrar gráficamente esta ciudad')
                            if ciudad.getContadorPuntosDeEntrada() == 1:
                                punto_de_entrada = ciudad.mapa.getPrimero('PuntoEntrada')
                                if ciudad.getContadorRecursos() == 1:
                                    recurso = ciudad.mapa.getPrimero('Recurso')
                                    #Ejecutar misión
                                else:
                                    ciudad.mapa.showRecursos()
                                    print()
                                    #Pregunta al usuario las coordenadas del recurso a extraer
                                    recurso = preguntarCoordenadas(ciudad, 'Recurso')
                                    #Ejecutar misión
                            else:
                                #ciudad.mapa.showRecursos()
                                ciudad.mapa.showPuntosDeEntrada()
                                print()
                                punto_de_entrada = preguntarCoordenadas(ciudad, 'PuntoEntrada')
                                if ciudad.getContadorRecursos() == 1:
                                    recurso = ciudad.mapa.getPrimero('Recurso')
                                    #Ejecutar misión
                                else:
                                    ciudad.mapa.showRecursos()
                                    print()
                                    #Pregunta al usuario las coordenadas del recurso a extraer
                                    recurso = preguntarCoordenadas(ciudad, 'Recurso')
                                    #Ejecutar misión                                
                        else:
                            Ciudades.showCiudadesRecursos()
                            print()
                            nombre = str(input('Ingresa el nombre de la ciudad: \n'))
                            ciudad = Ciudades.searchCiudad(nombre)
                            res = Ciudades.showMapa(ciudad.getNombre(), ciudad.getColumnas(), 'Extraccion')
                            if res == True:
                                #Convierte la grafica de .dot a .svg y la abre automáticamente
                                archivo_nombre_dot = 'Ciudad_'+ciudad.getNombre()+'_Extraccion.dot'
                                archivo_nombre_svg = 'Ciudad_'+ciudad.getNombre()+'_Extraccion.svg'
                                system('dot -Tsvg {} -o {}'.format(archivo_nombre_dot, archivo_nombre_svg))
                                startfile(archivo_nombre_svg)
                            else:
                                print('> No es posible mostrar gráficamente esta ciudad')                                
                            if ciudad.getContadorPuntosDeEntrada() == 1:
                                punto_de_entrada = ciudad.mapa.getPrimero('PuntoEntrada')
                                if ciudad.getContadorRecursos() == 1:
                                    recurso = ciudad.mapa.getPrimero('Recurso')
                                    #Ejecutar misión
                                else:
                                    ciudad.mapa.showRecursos()
                                    print()
                                    #Pregunta al usuario las coordenadas del recurso a extraer
                                    recurso = preguntarCoordenadas(ciudad, 'Recurso')
                                    #Ejecutar misión
                            else:
                                #ciudad.mapa.showRecursos()
                                ciudad.mapa.showPuntosDeEntrada()
                                print()
                                punto_de_entrada = preguntarCoordenadas(ciudad, 'PuntoEntrada')
                                if ciudad.getContadorRecursos() == 1:
                                    recurso = ciudad.mapa.getPrimero('Recurso')
                                    #Ejecutar misión
                                else:
                                    ciudad.mapa.showRecursos()
                                    print()
                                    #Pregunta al usuario las coordenadas del recurso a extraer
                                    recurso = preguntarCoordenadas(ciudad, 'Recurso')
                                    #Ejecutar misión                                
                    else:
                        print('> La misión de rescate no es posible, no hay ciudades con recursos por extraer')
            else:
                print('> No es posible realizar esta misión, no hay robots ChapinFighter en el sistema')
        elif opt == 4:
            print('> Gracias por usar el programa')
        else:
            print('> La opción ingresada no es valida...Intenta de nuevo')

