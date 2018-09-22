from Primaria import Primaria
from Bachillerato import Bachillerato

class Colegio:
    # metodo init, cuando va a inicializar la clase lo primero que ejecuta
    def __init__(self,nombre,cantidadEstudiantes,cantidadProfesores,cantidadGrados,cantidadCursos,arregloPrimaria,arregloBachillerato):
        self.nombre=nombre
        self.cantidadEstudiantes=cantidadEstudiantes
        self.cantidadProfesores=cantidadProfesores
        self.cantidadGrados=cantidadGrados
        self.cantidadCursos=cantidadCursos
        self.arregloPrimaria=arregloPrimaria
        self.arregloBachillerato=arregloBachillerato

    def getNombre(self):
        return (self.nombre)
    def getCantidadEstudiantes(self):
        return self.cantidadEstudiantes
    def getCantidadProfesores(self):
        return self.cantidadProfesores
    def getCantidadGrados (self):
        return self.cantidadGrados
    def getCantidadCursos(self):
        return self.cantidadCursos
    def getArregloPrimaria(self):
        return self.arregloPrimaria
    def getArregloBachillerato(self):
        return self.arregloBachillerato
    def setNombre(self, nombre):
        self.nombre=nombre
    def setCantidadEstudiantes(self, cantidadEstudiantes):
        self.cantidadEstudiantes=cantidadEstudiantes
    def setCantidadProfesores(self,cantidadProfesores):
        self.cantidadProfesores=cantidadProfesores
    def setCantidadGrados (self,cantidadGrados):
        self.cantidadGrados=cantidadGrados
    def setCantidadCursos(self,cantidadCursos):
        self.cantidadCursos=cantidadCursos
    def setArregloPrimaria(self,arregloPrimaria):
        self.arregloPrimaria=arregloPrimaria
    def setArregloBachillerato(self,arregloBachillerato):
        self.arregloBachillerato=arregloBachillerato

    def inicializarPrimaria(self):
        self.primaria=Primaria (self.arregloPrimaria[0]["estudiantes"],self.arregloPrimaria[0]["profesores"],self.arregloPrimaria[0]["grados"],self.arregloPrimaria[0]["cursos"],self.arregloPrimaria[0]["curso"])
    def getPrimaria (self):
        return self.primaria 

    def inicializarBachillerato(self):
        self.bachillerato=Bachillerato (self.arregloBachillerato[0]["estudiantes"],self.arregloBachillerato[0]["profesores"],self.arregloBachillerato[0]["grados"],self.arregloBachillerato[0]["cursos"],self.arregloBachillerato[0]["curso"])
    def getBachillerato (self):
        return self.bachillerato 
   
   

