#Nodo para la matriz ortogonal

class Celda:

    def __init__(self):
        self.tipo = None #Intransitable, PuntoEntrada, Camino, UnidadMilitar, UnidadCivil, Recurso
        self.estado = None #True -> Transitable, False -> No es transitable
        self.capacidad_combate = None # Capacidad != None solo para las unidades militares
        #Coordenadas
        self.coordenada_x = None
        self.coordenada_y = None
        #Apuntadores
        self.right = None
        self.up = None
        self.left = None
        self.down = None
    
    #Getters y Setters
    def getTipo(self):
        return self.tipo
    
    def setTipo(self, tipo):
        self.tipo = tipo

    def getEstado(self):
        return self.estado
    
    def setEstado(self, nuevo_estado):
        self.estado = nuevo_estado
    
    def getCapacidadCombate(self):
        return self.capacidad_combate
    
    def setCapacidadCombate(self, capacidad):
        self.capacidad_combate = capacidad

    def getCoordenadaX(self):
        return self.coordenada_x
    
    def setCoordenadaX(self, x):
        self.coordenada_x = x
        
    def getCoordenadaY(self):
        return self.coordenada_y
    
    def setCoordenadaY(self, y):
        self.coordenada_y = y
