from nodo_ruta import Ruta

class ListaRutas():

    def __init__(self):
        self.size = 0
        self.head = None
    
    #Añade al final de la lista
    def addEnd(self, x, y):
        nuevo = Ruta(x, y)
        self.size += 1
        if self.head is None:
            self.head = nuevo
        else:
            tmp = self.head
            while tmp.next is not None:
                tmp = tmp.next
            tmp.next = nuevo
    
    #Devuelve el primer nodo de la lista
    def getFirst(self):
        return self.head    

    #Para buscar si un nodo ya existe en la lista
    def search(self, x, y):
        tmp = self.head
        while tmp is not None:
            #Si existe el nodo en la lista, retorna el nodo
            if tmp.getCoordenadaX() == x and tmp.getCoordenadaY() == y:
                return tmp
            tmp = tmp.next
        #Si no existe el nodo en la lista
        return False
    
    #Elimina el primer nodo
    def deleteFirst(self):
        tmp = self.head
        self.head = tmp.next
        tmp.next = None
        self.size -= 1
    
    #Elimina el último nodo
    def deleteLast(self):
        tmp = self.head
        while tmp is not None:
            if tmp.next is None:
                anterior = self.head #Nodo penúltimo
                while anterior.next.getCoordenadaX() != tmp.getCoordenadaX() and anterior.next.getCoordenadaY() != tmp.getCoordenadaY():
                    #Mientras el siguiente a 'anterior' no sea el último
                    anterior = anterior.next
                #Cuando encontro el penúltimo
                anterior.next = None #El penúltimo pasa a  apuntar a None
                self.size -= 1
            tmp = tmp.next

    #Elimina todos los nodos de la lista
    def clearLista(self):
        self.head = None
        self.size = 0

    #Devuelve el tamaño de la lista
    def getSize(self):
        return self.size

'''
    def show(self):
        tmp = self.head
        while tmp is not None:
            print(tmp.getCoordenadaX(), tmp.getCoordenadaY())
            tmp = tmp.next
'''
