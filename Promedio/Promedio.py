Lloyd = {
    "nombre":"Lloyd",
    "tareas": [90,97,75,92],
    "pruebas": [ 88,40,94],
    "exámenes": [ 75,90]
    }
Alice = {
    "nombre":"Alice",
    "tareas": [100,92,98,100],
    "pruebas": [82,83,91],
    "exámenes": [89,97]
    }
Tyler = {
    "nombre":"Tyler",
    "tareas": [0,87,75,22],
    "pruebas": [0,75,78],
    "exámenes": [100,100]
    }

def promedio(contenido):
    return sum(contenido)/len(contenido)

def obtenerCalificacionenLetras(nota):
    nota = round(nota)
    if  nota >= 90: return "A"
    elif  90 > nota >= 80: return "B"
    elif  80 > nota >= 70: return "C"
    elif  70 > nota >= 60: return "D"
    elif  60 > nota: return "F"

def calcularPromedio(chico):
    bar = promedio
    return bar(chico["tareas"])*.1 + bar(chico["pruebas"])*.3 + bar(chico["exámenes"])*.6

def calcularPromedioClase(listaEstudiantes):
    listaPromedio=[]
    for estudiante in listaEstudiantes:
        listaPromedio.append(calcularPromedio(estudiante))
    promedio=sum(listaPromedio)/len(listaPromedio)
    return promedio

estudiantes = [Lloyd,Alice,Tyler]
print calcularPromedioClase(estudiantes)
print obtenerCalificacionenLetras(calcularPromedioClase(estudiantes))
