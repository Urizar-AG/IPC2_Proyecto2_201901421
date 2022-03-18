
class Robot:

    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo #ChapinFighter o ChapinRescue
        self.capacidad_combate = 0
        self.next = None

    #Getters y Setters

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre    
    
    def getTipo(self):
        return self.tipo

    def getCapacidadCombate(self):
        return self.capacidad_combate

    def setCapacidadCombate(self, capacidad):
        self.capacidad_combate = capacidad
