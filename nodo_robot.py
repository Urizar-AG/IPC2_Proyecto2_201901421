
class Robot:

    def init(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
        self.capacidad_combate = 0
        self.next = None

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre    

    def getCapacidadCombate(self):
        return self.capacidad_combate

    def setCapacidadCombate(self, capacidad):
        self.capacidad_combate = capacidad
        