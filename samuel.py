# =========================================
# samuel gonzales costablanca
# Universidad de La Salle
# Taller de Python
# =========================================

# ======== EJERCICIO 1 =========
print("\n=== EJERCICIO 1: PROMEDIO ===")

promedios = []
num_promedios = 4

for i in range(num_promedios):
    while True:
        try:
            nota = float(input(f"Ingrese nota {i+1}: "))
            if 0 <= nota <= 5:
                promedios.append(nota)
                break
            else:
                print("Debe estar entre 0 y 5")
        except:
            print("Error, ingrese número válido")

print("Promedio:", sum(promedios)/num_promedios)


# ========= EJERCICIO 2 =========
print("\n=== EJERCICIO 2: APROBADOS ===")

notas = [("Ana",4.5),("Luis",2.8),("Santiago",3.9),("María",2.5)]

for n, nota in notas:
    if nota >= 3:
        print(f"{n} aprobó con {nota}")
    else:
        print(f"{n} reprobó con {nota}")


# ========= EJERCICIO 3 =========
print("\n=== EJERCICIO 3: AGENDA ===")

agenda = {}

def agenda_menu():
    while True:
        print("\n1.Agregar 2.Buscar 3.Eliminar 4.Ver 5.Salir")
        op = input("Opción: ")

        if op == "1":
            agenda[input("Nombre: ")] = input("Teléfono: ")

        elif op == "2":
            nombre = input("Buscar: ")
            print(agenda.get(nombre, "No existe"))

        elif op == "3":
            agenda.pop(input("Eliminar: "), None)

        elif op == "4":
            print(agenda)

        elif op == "5":
            break


# ========= EJERCICIO 4 =========
print("\n=== EJERCICIO 4: INVENTARIO ===")

inventario = {
    "Manzanas": {"precio":2500,"cantidad":10},
    "Leche": {"precio":3000,"cantidad":5},
    "Pan": {"precio":1500,"cantidad":20}
}

total = sum(p["precio"]*p["cantidad"] for p in inventario.values())
print("Valor total:", total)


# ========= EJERCICIO 5 =========
print("\n=== EJERCICIO 5: FRECUENCIA ===")

palabras = ["Salle","Software","neumococo","Salle","Software","Salle"]
rep = {}

for p in palabras:
    rep[p] = rep.get(p,0) + 1

print(rep)


# ========= EJERCICIO 6 =========
print("\n=== EJERCICIO 6: TEMPERATURAS ===")

temps = {
    "Bogotá":[18,20,19,17,21,22,19],
    "Medellín":[25,27,26,28,29,30,27],
    "Cali":[30,32,31,33,34,35,32]
}

for c, t in temps.items():
    print(c, "Max:", max(t), "Min:", min(t))


# ========= EJERCICIO 7 =========
print("\n=== EJERCICIO 7: NOTAS ===")

def convertir(n):
    if n >= 90: return "A"
    elif n >= 80: return "B"
    elif n >= 70: return "C"
    elif n >= 60: return "D"
    else: return "F"

est = [("Ana",95),("Luis",82),("Santiago",74),("María",58)]

for n, nota in est:
    print(n, convertir(nota))


# ========= EJERCICIO 8 =========
print("\n=== EJERCICIO 8: CARRITO ===")

carrito = {}

def agregar(nombre, precio, cantidad):
    if nombre in carrito:
        carrito[nombre]["cantidad"] += cantidad
    else:
        carrito[nombre] = {"precio":precio,"cantidad":cantidad}

def total_carrito():
    return sum(p["precio"]*p["cantidad"] for p in carrito.values())


# ========= EJERCICIO 9 =========
print("\n=== EJERCICIO 9: AGRUPAR ===")

productos = [("Manzana","Frutas"),("Banano","Frutas"),("Lechuga","Verduras")]
inv = {}

for p,c in productos:
    inv.setdefault(c, []).append(p)

print(inv)


# ========= EJERCICIO 10 =========
print("\n=== EJERCICIO 10: VOTACIÓN ===")

candidatos = ["Ana","Luis","Santiago"]
votos = ["Ana","Luis","Ana","Santiago","Luis","Ana"]

conteo = {c:0 for c in candidatos}

for v in votos:
    if v in conteo:
        conteo[v] += 1

ganador = max(conteo, key=conteo.get)

print("Resultados:", conteo)
print("Ganador:", ganador)

