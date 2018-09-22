"""
'''
Para trabajar con Json se debe importar
Import json
para decodificar/dencode
json.loads () pasar de objeto json a objeto python 

codificar

json.dumps() 

'''
"""
import json
from Colegio import Colegio

class Aplicacion:
    def __init__(self):
        self.cargarInformacion()
        self.inicializarColegio()
        self.inicializarPrimaria()
        self.inicializarBachillerato()
        self.inicializarCurso()
    def cargarInformacion(self):
        data=open("data/data.json","r")
        ##self.data= json.load(data)
        self.data=json.loads(data.read())
    def mostrarData(self):
        print (self.data["nombre"])
    def inicializarColegio(self):
        self.colegio=Colegio(self.data["nombre"],self.data["estudiantes"],self.data["profesores"],self.data["grados"],self.data["cursos"],self.data["primaria"],self.data["bachillerato"])
    def getColegio(self):
        return self.colegio
   
    def inicializarPrimaria(self):
        self.getColegio().inicializarPrimaria()
    def getPrimariacolegio(self):
        return self.getColegio().getPrimaria()
    def getCantidadEstudiantesPrimaria(self):
        return self.getColegio().getPrimaria().getEstudiantes()
   
    def inicializarBachillerato(self):
        self.getColegio().inicializarBachillerato()
    def getBachilleratocolegio(self):
        return self.getColegio.getBachillerato()
    def getCantidadEstudiantesBachillerato(self):
        return self.getColegio().getBachillerato().getEstudiantes()

aplicacion=Aplicacion()
#aplicacion.mostrarData()
print (aplicacion.getColegio().getNombre())
print (aplicacion.getCantidadEstudiantesPrimaria())
print (aplicacion.getCantidadEstudiantesBachillerato())