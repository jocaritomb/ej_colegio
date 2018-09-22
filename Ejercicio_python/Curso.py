class curso:
    def __init__(self,grado,curso,cantidadProfesores,datosProfesor,cantidadEstudiantes,listaEstudiante):
        self.grado=grado
        self.curso=curso
        self.cantidadProfesores=cantidadProfesores
        self.cantidadEstudiantes=cantidadEstudiantes
        self.listaEstudiante=listaEstudiante
    
    def getGrado (self):
        return self.grado
    def getCurso (self):
        return self.curso
    def getCantidadProfesores (self):
        return self.cantidadProfesores
    def getCantidadEstudiantes (self):
        return self.cantidadEstudiantes
    def getListaEstudiante (self):
        return self.listaEstudiante
    
    def setGrado(self,grado):
        self.grado=grado
    def setCurso(self,curso):
        self.curso=curso
    def setCantidadProfesores(self,cantidadProfesores):
        self.cantidadProfesores=cantidadProfesores
    def setCantidadEstudiantes(self,cantidadEstudiantes):
        self.cantidadEstudiantes=cantidadEstudiantes
    def setListaEstudiante(self,listaEstudiante):
        self.listaEstudiante=listaEstudiante
    