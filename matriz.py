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

