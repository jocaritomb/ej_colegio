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
        return nombre
    def setNombre(self, nombre):
        self.nombre=nombre

aplicacion=Colegio ("Colegio X",10,20,30,40,[50, 50],[60, 60])
print (aplicacion.getNombre())
aplicacion.setNombre("Colegio y")
print (aplicacion.getNombre())
