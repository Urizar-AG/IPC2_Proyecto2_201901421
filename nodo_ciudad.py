from matriz import MatrizOrtogonal

class Ciudad:

    def __init__(self, nombre, filas, columnas):
        self.nombre = nombre
        self.filas = filas
        self.columnas = columnas
        self.mapa = MatrizOrtogonal()
        self.contador_recursos = 0 #Cantidad de celdas tipo "Recurso" que tiene la ciudad
        self.contador_puntos_entradas = 0 #Cantidad de celdas tipo "PuntoEntrada" que tiene la ciudad
        self.contador_unidades_civiles = 0 #Cantidad de celdas tipo "UnidadCivil" que tiene la ciudad
        self.contador_unidades_militares = 0 #Cantidad de celdas tipo "UnidadMilitar" que tiene la ciudad
        self.next = None
    
    #Getters y Setters

    def getNombre(self):
        return self.nombre

    def setNombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre
    
    def getFilas(self):
        return self.filas
    
    def getColumnas(self):
        return self.columnas
    
    def getContadorRecursos(self):
        return self.contador_recursos
        
    def setContadorRecursos(self, cantidad):
        self.contador_recursos = cantidad
    
    def getContadorPuntosDeEntrada(self):
        return self.contador_puntos_entradas
    
    def setContadorPuntosDeEntrada(self, cantidad):
        self.contador_puntos_entradas = cantidad

    def getContadorUnidadesCiviles(self):
        return self.contador_unidades_civiles
    
    def setContadorUnidadesCiviles(self, cantidad):
        self.contador_unidades_civiles = cantidad
    
    def getContadorUnidadesMilitares(self):
        return self.contador_unidades_militares
    
    def setContadorUnidadesMilitares(self, cantidad):
        self.contador_unidades_militares = cantidad
