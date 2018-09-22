class Bachillerato:
    def __init__(self,estudiantes,profesores,grados,cursos,curso):
        self.estudiantes=estudiantes
        self.profesores=profesores
        self.grados=grados
        self.cursos=cursos
        self.curso=curso
    def getEstudiantes(self):
        return self.estudiantes
    def getProfesores(self):
        return self.profesores
    def getGrados(self):
        return self.grados
    def getCursos(self):
        return self.cursos
    def getCurso(self):
        return self.curso
    def setEstudiantes(self,estudiantes):
        self.estudiantes=estudiantes
    def setProfesores(self,profesores):
        self.profesores=profesores
    def setGrados(self,grados):
        self.grados=grados
    def setCursos(self,cursos):
        self.cursos=cursos
    def setCurso(self,curso):
        self.curso=curso