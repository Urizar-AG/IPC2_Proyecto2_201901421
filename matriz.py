from nodo_celda import Celda

class MatrizOrtogonal():

    def __init__(self):
        #Cabecera 0,0 
        #Nodo raíz de la matriz
        self.root = Celda()
        self.root.setTipo('Cabecera')
        self.root.setEstado(False)
        self.root.setCoordenadaX(0)
        self.root.setCoordenadaY(0)
    
    def crearCabeceraVertical(self, indice):
        #Recorre las cabeceras verticales

        tmp = self.root

        while tmp is not None:
            #No existe la cabecera y las demás cabeceras son menores
            if tmp.down is None and tmp.getCoordenadaY() < indice:
                nuevo = Celda()
                nuevo.setTipo('Cabecera')
                nuevo.setEstado(False)
                nuevo.setCoordenadaX(0)
                nuevo.setCoordenadaY(indice)
                #Enlazando
                nuevo.up = tmp
                tmp.down = nuevo

                return tmp.down #Cabecera nueva

            #La cabecera ya existe
            if tmp.getCoordenadaY() == indice:
                return tmp

            #La cabecera a agregar está en medio de dos cabeceras
            if tmp.getCoordenadaY() < indice and tmp.down.getCoordenadaY() > indice:
                nuevo = Celda()
                nuevo.setTipo('Cabecera')
                nuevo.setEstado(False)
                nuevo.setCoordenadaX(0)
                nuevo.setCoordenadaY(indice)
                #Enlazando
                nuevo.down = tmp.down
                nuevo.up = tmp
                tmp.down.up = nuevo
                tmp.down = nuevo

                return tmp.down
            
            tmp = tmp.down
    
    def crearCabeceraHorizontal(self, indice):
        #Recorre las cabeceras horizontales

        tmp = self.root

        while tmp is not None:
            #No existe las cabeceras y las demás son cabeceras menores
            if tmp.right is None and tmp.getCoordenadaX() < indice:
                nuevo = Celda()
                nuevo.setTipo('Cabecera')
                nuevo.setEstado(False)
                nuevo.setCoordenadaX(indice)
                nuevo.setCoordenadaY(0)
                #Enlazando
                nuevo.left = tmp
                tmp.right = nuevo

                return tmp.right #Cabecera nueva
            
            #La cabera ya existe
            if tmp.getCoordenadaX() == indice:
                return tmp

            #La cabera a agregar está entre dos nodos
            if tmp.getCoordenadaX() < indice and tmp.right.getCoordenadaX() > indice:
                nuevo = Celda()
                nuevo.setTipo('Cabecera')
                nuevo.setEstado(False)
                nuevo.setCoordenadaX(indice)
                nuevo.setCoordenadaY(0)
                #Enlazando
                nuevo.right = tmp.right
                nuevo.left = tmp
                tmp.right.left = nuevo
                tmp.right = nuevo

                return tmp.right
            
            tmp = tmp.right

    def insertarVertical(self, nodo, cabecera):
        #Recorre de forma vertical hasta encontrar la coordenada Y donde se quiere insertar
        #nodo: Nodo (contenido) que se quiere insertar
        #cabecera: Nodo cabecera (horizontal) donde se va a insertar

        tmp = cabecera  

        while tmp is not None:
            #No existe el nodo y los demás son menores
            if tmp.down is None and tmp.getCoordenadaY() < nodo.getCoordenadaY():
                #Enlaza
                nodo.up = tmp
                tmp.down = nodo
            
            #El nodo que se quiere insertar ya existe
            if tmp.getCoordenadaY() == tmp.getCoordenadaY():
                #No hacer nada
                pass

            #El nodo que se está agregando está entre otros nodos
            if tmp.getCoordenadaY() < nodo.getCoordenadaY() and tmp.down.getCoordenadaY() > nodo.getCoordenadaY():
                #Enlazando
                nodo.down = tmp.down
                nodo.up = tmp
                tmp.down.up = nodo
                tmp.down = nodo
            
            tmp = tmp.down

    def insertarHorizontal(self, nodo, cabecera):
        #Recorre de forma horizontal hasta encontrar la coordenada X donde se quiere insertar
        #nodo: Nodo (contenido) que se quiere insertar
        #cabecera: Nodo cabecera (vertical) donde se va a insertar

        tmp = cabecera

        while tmp is not None:
            #No existe el nodo y los demás son menores
            if tmp.right is None and tmp.getCoordenadaX() < nodo.getCoordenadaX():
                #Enlaza
                nodo.left = tmp
                tmp.right = nodo
            
            #El nodo ya existe
            if tmp.getCoordenadaX() == nodo.getCoordenadaX():
                #No hacer nada
                pass

            #El nodo está en medio de dos nodos
            if tmp.getCoordenadaX() < nodo.getCoordenadaX() and tmp.right.getCoordenadaX() > nodo.getCoordenadaX():
                nodo.right = tmp.right
                nodo.left = tmp
                tmp.right.left = nodo
                tmp.right = nodo
            
            tmp = tmp.right
    
    def insertarNodo(self, tipo, estado, capacidad, x, y):
        #Obtiene las cabeceras
        cabecera_horizontal = self.crearCabeceraHorizontal(x)
        cabecera_vertical = self.crearCabeceraVertical(y)

        #Crea el nodo
        nuevo = Celda()
        nuevo.setTipo(tipo)
        nuevo.setEstado(estado)
        nuevo.setCapacidadCombate(capacidad)
        nuevo.setCoordenadaX(x)
        nuevo.setCoordenadaY(y)

        #Inserta el nodo
        self.insertarHorizontal(nuevo, cabecera_vertical)
        self.insertarVertical(nuevo, cabecera_horizontal)

    #Devuelve el primer nodo encontrado del tipo indicado por parámetro
    def getPrimero(self, tipo):
        tmp = self.root
        if tipo == 'PuntoEntrada':
            while tmp is not None:
                tmp2 = tmp
                while tmp2 is not None:
                    if tmp2.getTipo() == 'PuntoEntrada':
                        return tmp2
                    tmp2 = tmp2.right
                tmp = tmp.down
        elif tipo == 'UnidadCivil':
            while tmp is not None:
                tmp2 = tmp
                while tmp2 is not None:
                    if tmp2.getTipo() == 'UnidadCivil':
                        return tmp2
                    tmp2 = tmp2.right
                tmp = tmp.down
        elif tipo == 'Recurso':
            while tmp is not None:
                tmp2 = tmp
                while tmp2 is not None:
                    if tmp2.getTipo() == 'Recurso':
                        return tmp2
                    tmp2 = tmp2.right
                tmp = tmp.down

    def showPuntosDeEntrada(self):
        #Recorre las filas de izquierda a derecha
        #Si encuentra una celda tipo  punto de entrada, imprime la info en consola
        print('> Puntos de entrada disponible')
        tmp = self.root #Columna
        
        while tmp is not None:
            tmp2 = tmp #Columna
            while tmp2 is not None:
                if tmp2.getTipo() == 'PuntoEntrada':
                    print('# Entrada: Coordenada X: ' + str(tmp2.getCoordenadaX()) + ' - Coordenada Y: ' + str(tmp2.getCoordenadaY()))
                tmp2 = tmp2.right #Cambio de columna
            tmp = tmp.down #Cambiando fila

    def showUnidadesCiviles(self):
        #Recorre las filas de izquierda a derecha
        #si encuentra una unidad civil imprime la info en consola
        print('> Unidades civiles para rescatar')
        tmp = self.root #fila

        while tmp is not None:
            tmp2 = tmp #columna
            while tmp2 is not None:
                if tmp2.getTipo() == 'UnidadCivil':
                    print('# Unidad Civil: Coordenada X: ' + str(tmp2.getCoordenadaX()) + ' - Coordenada Y: ' + str(tmp2.getCoordenadaY()))
                tmp2 = tmp2.right #Cambio de columna
            tmp = tmp.down #Cambio de fila

    def showRecursos(self):
        #Recorre las filas de izquierda a derecha
        #Si encuentra una celda tipo Recurso, imprime la info en consola
        print('> Recursos disponibles')
        tmp = self.root

        while tmp is not None:
            tmp2 = tmp #columna
            while tmp2 is not None:
                if tmp2.getTipo() == 'Recurso':
                    print('# Recurso: Coordenada X: ' + str(tmp2.getCoordenadaX()) + ' - Coordenada Y: ' + str(tmp2.getCoordenadaY()))
                tmp2 = tmp2.right
            tmp = tmp.down

    #Busca una celda en el mapa por medio de sus coordenadas
    #Si existe coincidencia la retorna, caso contrario retorna None
    def searchCelda(self, x, y):
        #Recorre las filas por columnas
        tmp = self.root

        while tmp is not None:
            tmp2 = tmp #Columna
            while tmp2 is not None:
                if tmp2.getCoordenadaX() == x and tmp2.getCoordenadaY() == y:
                    return tmp2
                tmp2 = tmp2.right
            tmp = tmp.down
        return None

    #Escribe un archivo "dot" con los nodos de la matriz
    def showGrafica(self, nombre, columnas, tipo_mision):
        contador = 0 #Contador para las cabeceras de la matriz
        #Aquí el contador empieza en 0, porque será aumentado en uno en la validación de más abajo, antes de ser utilizado
        columns = columnas #Búmero de columnas que tiene la matriz
        grafica = None
        nombre_documento = 'Ciudad_' + nombre + '_' + tipo_mision + '.dot'

        try:
            grafica = open(nombre_documento, 'w', encoding='UTF-8') #Crea el archivo
            grafica.write('digraph G { \n')
            grafica.write('    node[shape=none] \n')    
            grafica.write('    label ="Negro: Intransitable \n Verde: Punto de entrada \n Blanco: Camino \n Rojo: Unidad militar \n Azul: Unidad Civil \n Gris: Recurso \n -------------------------------------------------------------- \n' 
                        +' Ciudad: ' +nombre+ ' \n Tipo de misión: ' +tipo_mision+ '"\n')#Texto de la grafica     
            grafica.write('\n')
            grafica.write('    nodo [label=< \n')             
            grafica.write('        <TABLE border="1" cellspacing="2" cellpadding="20" bgcolor="white"> \n')#Inicio de la tabla

            tmp = self.root
            #Recorre las filas por columnas
            while tmp is not None:
                tmp2 = tmp
                grafica.write('                <TR>\n')#Abre la fila
                while tmp2 is not None:
                    #Escribe las columnas
                    if tmp2.getTipo() == 'Intransitable':
                        grafica.write('                <TD border="1"  bgcolor="#000000"></TD> \n')#000000 -> Negro
                    elif tmp2.getTipo() == 'Camino':
                        grafica.write('                <TD border="1"  bgcolor="#FFFFFF"></TD> \n')#FFFFFF -> Blanco
                    elif tmp2.getTipo() == 'PuntoEntrada':
                        grafica.write('                <TD border="1"  bgcolor="#00DD00"></TD> \n')#00DD00 -> Verde
                    elif tmp2.getTipo() == 'UnidadCivil':
                        grafica.write('                <TD border="1"  bgcolor="#08AEF5"></TD> \n')#08AEF5 -> Azúl    
                    elif tmp2.getTipo() == 'Recurso':
                        grafica.write('                <TD border="1"  bgcolor="#9B9B9B"></TD> \n')#9B9B9B -> Gris
                    elif tmp2.getTipo() == 'UnidadMilitar':
                        grafica.write('                <TD border="1"  bgcolor="#ff1e1e"></TD> \n')#ff1e1e -> Rojo
                    elif tmp2.getTipo() == 'Cabecera':
                        #Para el nodo raíz
                        if tmp2.getCoordenadaX() == 0 and tmp2.getCoordenadaY() == 0:
                            grafica.write('                <TD border="1"  bgcolor="#FFFFFF">00</TD> \n')
                        else:
                            #Si el contador es menor que el número de columnas
                            if contador < columns:
                                contador += 1
                            else:
                                #Al recorrer las filas por columnas, primer se recorre la filas de las cabeceras horizontales
                                #Las cabeceras verticales se van agregando conforme se van agregando las filas
                                #Y la númeración de las filas en este caso empieza en 1 (exceptuando el nodo raíz que es 0,0) es necesario reiniciar
                                #el contador a 1 y no a 0.
                                contador = 1
                            grafica.write('                <TD border="1"  bgcolor="#FFFFFF">'+str(contador)+'</TD> \n')#Nodos cabecera 
                    tmp2 = tmp2.right#Cambio a la siguiente columna
                grafica.write('                </TR>\n')#Cierra la fila
                tmp = tmp.down#Cambio a la siguiente fila
            grafica.write('    </TABLE>>]; \n')#Cierra el ndod
            grafica.write('}')#Cierra el digraph
            grafica.close()#Cierra el archivo
            #Si llego hasta aquí es porque todo salió bien
            return True
        except Exception as e:
            grafica.close()#Cierra la gráfica
            return False #Algo salió mal al ejecutar el código dentro del try
            print(e)

    #Genera un archivo "dot" para las misiones completadas, misiones de rescate y extracción
    def showMision(self, nombre_ciudad, tipo_mision, coordenadas, nombre_robot, capacidad_inicial, capacidad_final, columnas_ciudad, camino_mision):
        contador = 0 #Contador para las cabeceras de la matriz
        #Aquí el contador empieza en 0, porque será aumentado en uno en la validación de más abajo, antes de ser utilizado
        columns = columnas_ciudad #Número de columnas que tiene la matriz
        grafica = None
        nombre_documento = 'Ciudad_' + nombre_ciudad + '_' + tipo_mision + '.dot'

        try:
            grafica = open(nombre_documento, 'w', encoding='UTF-8') #Crea el archivo
            grafica.write('digraph G { \n')
            grafica.write('    node[shape=none] \n')    
            grafica.write('    label ="Negro: Intransitable \n Verde: Punto de entrada \n Blanco: Camino \n Rojo: Unidad militar \n Azul: Unidad Civil \n Gris: Recurso \n -------------------------------------------------------------- \n' 
                        +' Ciudad: ' +nombre_ciudad+ ' \n Tipo de misión: ' +tipo_mision+ ' \n Unidad civil rescatada: ' +coordenadas+ ' \n Robot: ' +nombre_robot+ ' (ChapinRescue)"\n')#Texto de la grafica     
            grafica.write('\n')
            grafica.write('    nodo [label=< \n')             
            grafica.write('        <TABLE border="1" cellspacing="2" cellpadding="20" bgcolor="white"> \n')#Inicio de la tabla

            tmp = self.root
            #Recorre las filas por columnas
            while tmp is not None:
                tmp2 = tmp
                grafica.write('                <TR>\n')#Abre la fila
                while tmp2 is not None:
                    #Escribe las columnas
                    if tmp2.getTipo() == 'Intransitable':
                        grafica.write('                <TD border="1"  bgcolor="#000000"></TD> \n')#000000 -> Negro
                    elif tmp2.getTipo() == 'Camino':
                        paso = camino_mision.search(tmp2.getCoordenadaX(), tmp2.getCoordenadaY())#Si el robot paso por esa celda
                        if paso == False:
                            grafica.write('                <TD border="1"  bgcolor="#FFFFFF"></TD> \n')#FFFFFF -> Blanco
                        else:
                            grafica.write('                <TD border="1"  bgcolor="#F2D587"></TD> \n')#F2D587 -> Beige
                    elif tmp2.getTipo() == 'PuntoEntrada':
                        grafica.write('                <TD border="1"  bgcolor="#00DD00"></TD> \n')#00DD00 -> Verde
                    elif tmp2.getTipo() == 'UnidadCivil':
                        grafica.write('                <TD border="1"  bgcolor="#08AEF5"></TD> \n')#08AEF5 -> Azúl    
                    elif tmp2.getTipo() == 'Recurso':
                        grafica.write('                <TD border="1"  bgcolor="#9B9B9B"></TD> \n')#9B9B9B -> Gris
                    elif tmp2.getTipo() == 'UnidadMilitar':
                        grafica.write('                <TD border="1"  bgcolor="#FF1E1E"></TD> \n')#ff1e1e -> Rojo
                    elif tmp2.getTipo() == 'Cabecera':
                        #Para el nodo raíz
                        if tmp2.getCoordenadaX() == 0 and tmp2.getCoordenadaY() == 0:
                            grafica.write('                <TD border="1"  bgcolor="#FFFFFF">00</TD> \n')
                        else:
                            #Si el contador es menor que el número de columnas
                            if contador < columns:
                                contador += 1
                            else:
                                #Al recorrer las filas por columnas, primer se recorre la filas de las cabeceras horizontales
                                #Las cabeceras verticales se van agregando conforme se van agregando las filas
                                #Y la númeración de las filas en este caso empieza en 1 (exceptuando el nodo raíz que es 0,0) es necesario reiniciar
                                #el contador a 1 y no a 0.
                                contador = 1
                            grafica.write('                <TD border="1"  bgcolor="#FFFFFF">'+str(contador)+'</TD> \n')#Nodos cabecera 
                    tmp2 = tmp2.right#Cambio a la siguiente columna
                grafica.write('                </TR>\n')#Cierra la fila
                tmp = tmp.down#Cambio a la siguiente fila
            grafica.write('    </TABLE>>]; \n')#Cierra el ndod
            grafica.write('}')#Cierra el digraph
            grafica.close()#Cierra el archivo
            
            #Si no hubo problema al graficar
            return True
        except:
            grafica.close()#Cierra la gráfica
            return False #Algo salió mal al graficar

