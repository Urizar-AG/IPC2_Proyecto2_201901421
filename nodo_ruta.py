#De los nodos que se visitan solo es necesario guardar las coordenadas de ellos

class Ruta:
    
    def __init__(self, x, y):
        self.coordenada_x = x
        self.coordenada_y = y
        self.next = None
    
    def getCoordenadaX(self):
        return self.coordenada_x
    
    def getCoordenadaY(self):
        return self.coordenada_y
