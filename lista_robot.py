from nodo_robot import Robot

class ListaRobots():

    def __init__(self):
        self.size = 0 #Tamaño de la lista
        self.contador_fighter = 0 #Cantidad de robots ChapinFighter en la lista
        self.contador_rescue = 0 #Cantidad de robotos ChapinRescue en la lista
        self.head = None

    #Añade al final de la lista
    def addEnd(self, nombre, tipo):
        nuevo = Robot(nombre, tipo)
        self.size += 1
        if self.head is None:
            self.head = nuevo
            if nuevo.getTipo() == 'ChapinFighter':#Si el robot que se está agregando es ChapinFighter
                self.contador_fighter += 1
            else:#Si el robot que se está agregan es ChapinRescue
                self.contador_rescue += 1
        else:
            tmp = self.head
            while tmp.next is not None:
                tmp = tmp.next
            tmp.next = nuevo
            if nuevo.getTipo() == 'ChapinFighter':
                self.contador_fighter += 1
            else:
                self.contador_rescue += 1

    #Busca un robot por su nombre y tipo, si encuentra coincidencia retorna el nodo, caso contrario retorna None
    def searchRobot(self, nombre, tipo):
        if tipo == 'ChapinFighter':#Si el robot a buscar es ChapinFighter
            tmp = self.head
            while tmp is not None:
                if tmp.getNombre() == nombre:
                    if tmp.getTipo() == tipo:#Si el tipo de robot cuyo nomre coincidio, coincide con ChapinFighter
                        return tmp
                tmp = tmp.next
        else:#Si el robot a buscar es ChapinRescue
            tmp = self.head
            while tmp is not None:
                if tmp.getNombre() == nombre:
                    if tmp.getTipo() == tipo:#Si el tipo de robot cuyo nombre coincidio, coincide con ChapinRescue
                        return tmp
                tmp = tmp.next
        return None #Si no encuentra ninguna coincidencia

    #Muestra la info de los robot ChapinFighter en la lista
    def showChapinFighter(self):
        tmp = self.head
        print('> Robots ChapinFighter Disponibles')
        while tmp is not None:
            if tmp.getTipo() == 'ChapinFighter':
                print('# Nombre: ' + str(tmp.getNombre()) + ' - ' + ' Capacidad de combate: ' + str(tmp.getCapacidadCombate()))
            tmp = tmp.next
    
    #Muestra la info de los robot ChapinRescue en la lista
    def showChapinRescue(self):
        tmp = self.head
        print('> Robots ChapinRescue Disponbiles')
        while tmp is not None:
            if tmp.getTipo() == 'ChapinRescue':
                print('# Nombre:' + str(tmp.getNombre()))
            tmp = tmp.next

    def getContadorFighter(self):
        return self.contador_fighter
    
    def getContadorRescue(self):
        return self.contador_rescue

    #Devuelve el tamaño de la lista    
    def getSize(self):
        return self.size
    
    #True si la lista está vacía, caso contrario False
    def isEmpty(self):
        if self.size == 0:
            return True
        else:
            return False
