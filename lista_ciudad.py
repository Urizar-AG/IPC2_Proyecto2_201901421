from nodo_ciudad import Ciudad

class ListaCiudades():

    def __init__(self):
        self.size = 0
        self.head = None
        self.contador_ciudades_civiles = 0 #Cantidad de ciudades que tienen unidades civiles
        self.contador_ciudades_recursos = 0 #Cantidad de ciudades que tiene celdas tipo "Recurso"

    #Añade al final
    def addEnd(self, nombre, filas, columnas):
        nuevo = Ciudad(nombre, filas, columnas)
        self.size += 1
        if self.head is None:
            self.head = nuevo
        else:
            tmp = self.head
            while tmp.next is not None:
                tmp = tmp.next
            tmp.next = nuevo

    #Busca una ciudad por su nombre y tipo, si encuentra coincidencia retorna el nodo, caso contrario retorna None
    def searchCiudad(self, nombre):
        tmp = self.head
        while tmp is not None:
            if tmp.getNombre() == nombre:
                return tmp
            tmp = tmp.next
        return None 
    
    #Elimina el nodo de la ciudad que recibe por parámetro
    def deleteCiudad(self, nombre):
        tmp = self.head
        while tmp is not None:
            if tmp.getNombre() == nombre:
                #Si el nodo a eliminar es el primero
                if tmp == self.head:
                    self.head = tmp.next
                    tmp.next = None
                    self.size -= 1 #Actualiza el tamaño de la lista
                #Si el nodo a eliminar es el último
                elif tmp.next is None:
                    anterior = self.head #Nodo anterior al nodo actual(el nodo actual es el que se está borrando)
                    while anterior.next.getNombre() != tmp.getNombre():
                        anterior = anterior.next
                    anterior.next = None
                    self.size -= 1
                #Si no es el primer nodo o el último nodo
                else:
                    siguiente = tmp.next #Nodo siguiente al nodo actual
                    anterior = self.head #Nodo anterior al nodo actual
                    while anterior.next.getNombre() != tmp.getNombre():
                        anterior = anterior.next
                    anterior.next = siguiente #El nodo anterior a actual ahora apunta al nodo siguiente del actual.
                    tmp.next = None
                    self.size -= 1
            tmp = tmp.next

    #Muestra el nombre de las ciudades donde existe por lo menos una unidad civil
    def showCiudadesCiviles(self):
        print('> Ciudades disponibles')
        tmp = self.head
        while tmp is not None:
            if tmp.getContadorUnidadesCiviles() > 0:
                print('# Nombre: ' + str(tmp.getNombre()))
            tmp = tmp.next

    #Muestra el nombre de las ciudades donde existe por lo menos una celda tipo "Recurso"
    def showCiudadesRecursos(self):
        print('> Ciudades disponibles')
        tmp = self.head
        while tmp is not None:
            if tmp.getContadorRecursos() > 0:
                print('#Nombre: ' + str(tmp.getNombre()))
            tmp = tmp.next

    #Getters y setters
    def getContadorCiudadesCiviles(self):
        return self.contador_ciudades_civiles
    
    def setContadorCiudadesCiviles(self, cantidad):
        self.contador_ciudades_civiles = cantidad

    def getContadorCiudadesRecursos(self):
        return self.contador_ciudades_recursos
    
    def setContadorCiudadesRecursos(self, cantidad):
        self.contador_ciudades_recursos = cantidad

    #Devuelve el primer nodo de la lista
    def getPrimero(self):
        return self.head

    #Devuelve el tamaño de la lista
    def getSize(self):
        return self.size
    
    #Verifica si la lista está o no vacía
    #True si está vacía, False caso contrario
    def isEmpty(self):
        if self.size == 0:
            return True
        else:
            return False
