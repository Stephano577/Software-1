class Alumno:
    #Cuando cree un alumno, se proporcionbara un nombre y edad
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    def getnombre(self):
        return self.__nombre
    
    def getedad(self):
        return self.__edad
a1 = Alumno ("Maria, 20")
a2 = Alumno ("Juan, 21")
a3 = Alumno ("Ana, 10")

edad_mayor = 0
edad_menor = 99

if a1.getedad() > edad_mayor:
    edad_mayor = a1.getedad
    alumno_mayor = a1.getnombre()
if a2.getedad() > edad_mayor:
    edad_mayor = a2.getedad
    alumno_mayor = a2.getnombre()
if a3.getedad() > edad_mayor:
    edad_mayor = a3.getedad
    alumno_mayor = a3.getnombre()

print(f'El alumno mayor es {alumno_mayor} y tiene {edad_mayor}años de edad')

alumnos = (a1, a2, a3)

for alum in alumnos:
    if alum.getedad() < edad_menor:
        edad_menor = alum.getedad()
        edad_mayor = alum.getnombre()

print (f'El alumno menor es {alumno_menor} y tiene {edad_menor} años de edad')