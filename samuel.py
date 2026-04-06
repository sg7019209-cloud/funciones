def analizar_notas(lista_notas):
    promedio = sum(lista_notas) / len(lista_notas)
    nota_alta = max(lista_notas)
    nota_baja = min(lista_notas)
    return promedio, nota_alta, nota_baja#punto 2 //punto3 
#2 
def aprobados(lista_estudiantes):
    return [nombre for nombre, nota in lista_estudiantes if nota >= 3.0]
#3

def buscar(nombre):
    return agenda.get(nombre, "No encontrado")

def eliminar(nombre):
    agenda.pop(nombre, None)
    #4
def valor_total(inventario):
    total = 0
    for producto in inventario:
        total += producto["precio"] * producto["cantidad"]
    return total
#5
def frecuencia_palabras(lista):
    diccionario = {}
    for palabra in lista:
        diccionario[palabra] = diccionario.get(palabra, 0) + 1
    return diccionario
#6
def temperaturas(datos):
    max_temp = ("", float("-inf"))
    min_temp = ("", float("inf"))

    for ciudad, temps in datos.items():
        for t in temps:
            if t > max_temp[1]:
                max_temp = (ciudad, t)
            if t < min_temp[1]:
                min_temp = (ciudad, t)

    return max_temp, min_temp
#7
def convertir_nota(nota):
    if nota >= 4.5:
        return "A"
    elif nota >= 4.0:
        return "B"
    elif nota >= 3.0:
        return "C"
    elif nota >= 2.0:
        return "D"
    else:
        return "F"

def reporte(estudiantes):
    return [(nombre, convertir_nota(nota)) for nombre, nota in estudiantes]
#8
carrito = []

def agregar_producto(nombre, precio):
    carrito.append(precio)

def aplicar_descuento(porcentaje):
    return sum(carrito) * (1 - porcentaje / 100)

def total():
    return sum(carrito)
#9
def agrupar(lista):
    resultado = {}
    for producto, categoria in lista:
        if categoria not in resultado:
            resultado[categoria] = []
        resultado[categoria].append(producto)
    return resultado

#10
def votos(lista_votos, candidatos):
    conteo = {c: 0 for c in candidatos}
    invalidos = 0

    for voto in lista_votos:
        if voto in candidatos:
            conteo[voto] += 1
        else:
            invalidos += 1

    total = sum(conteo.values())
    ganador = max(conteo, key=conteo.get)
    porcentaje = (conteo[ganador] / total) * 100 if total > 0 else 0

    return ganador, porcentaje, invalidos