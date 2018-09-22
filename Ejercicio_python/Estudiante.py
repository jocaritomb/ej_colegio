class Estudiante:
    def __init__(self,nombre,nota):
        self.nombre=nombre
        self.nota=nota
    def getNombre(self):
        return self.nombre
    def getnota(self):
        return self.nota
    def setNombre(self,nombre):
        self.nombre=nombre
    def setnota(self,nota):
        self.nota=nota