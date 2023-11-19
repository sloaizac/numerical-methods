# Trazador (spline) lineal, grado 1
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

def trazalineal(xi,fi):
    n = len(xi)
    x = sym.Symbol('x')
    px_tabla = []
    
    tramo = 1
    while not(tramo>=n):
        # con 1ra diferencia finita avanzada 
        numerador = fi[tramo]-fi[tramo-1]
        denominador = xi[tramo]-xi[tramo-1]
        m = numerador/denominador
        pxtramo = fi[tramo-1] + m*(x-xi[tramo-1])
        px_tabla.append(pxtramo)
        tramo = tramo + 1
        
    return px_tabla

# PROGRAMA
# INGRESO , Datos de prueba
#xi = [0.1 , 0.2, 0.3, 0.4]
#fi = [1.45, 1.8, 1.7, 2.0]
#muestras = 10 # entre cada par de puntos

