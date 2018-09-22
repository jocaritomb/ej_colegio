class profesor:
    def __init__(self,nombre,suplente):
        self.nombre=nombre
        self.suplente=suplente
    def getNombre(self):
        return self.nombre
    def getSuplente(self):
        return self.suplente
    def setNombre(self,nombre):
        self.nombre=nombre
    def setSuplente(self,suplente):
        self.suplente=suplente