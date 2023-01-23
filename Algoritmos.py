from Pasajero import Pasajero
import random


def crear_pasajeros(n_pasajeros):
    pasajeros = []
    for i in range(n_pasajeros):
        pasajeros.append(Pasajero(i+1, round(random.normalvariate(50, 5), 2),
                                  round(random.normalvariate(75, 10), 2), random.choice([6, 8])))
    return pasajeros


def generar_primer_p(pasajeros):
    pasajeros_id = []
    for pasajero in pasajeros:
        pasajeros_id.append(pasajero.id)
    return pasajeros_id


def arr_numeros(numero):
    arr = []
    for num in range(numero):
        arr.append(num)
    return arr

# crea un arreglo temporal con -1 el cual será el arreglo que se retorna como resultado


def llenar_resultado(n):
    resultado = []
    for _ in range(n):
        resultado.append(-1)
    return resultado


def generar_rango_cruza(cant_genes):
    # se crea el rango a evaluar en individuo1 y While para que a y b no sean iguales
    a, b = 0, 0
    while a == b:
        a, b = random.choices(cant_genes, k=2)
    # condicion para que "a" siempre sea menor que "b"
    if a > b:
        a, b = b, a
    return a, b
