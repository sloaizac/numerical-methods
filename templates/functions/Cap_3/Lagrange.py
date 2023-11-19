   # Interpolacion de Lagrange
# divisoresL solo para mostrar valores
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

# PROCEDIMIENTO
def Lagrange(xi,fi):
    xi = np.array(xi)
    fi = np.array(fi)

    # Polinomio de Lagrange
    n = len(xi)
    x = sym.Symbol('x')
    polinomio = 0
    divisorL = np.zeros(n, dtype = float)
    for i in range(0,n,1):
        
        # Termino de Lagrange
        numerador = 1
        denominador = 1
        for j  in range(0,n,1):
            if (j!=i):
                numerador = numerador*(x-xi[j])
                denominador = denominador*(xi[i]-xi[j])
        terminoLi = numerador/denominador

        polinomio = polinomio + terminoLi*fi[i]
        divisorL[i] = denominador

    # simplifica el polinomio
    polisimple = polinomio.expand()

    # para evaluación numérica
    px = sym.lambdify(x,polisimple)

    # Puntos para la gráfica
    muestras = 101
    a = np.min(xi)
    b = np.max(xi)
    pxi = np.linspace(a,b,muestras)
    pfi = px(pxi)

    # SALIDA
    """print('    valores de fi: ',fi)
    print('divisores en L(i): ',divisorL)
    print()
    print('Polinomio de Lagrange, expresiones')
    print(polinomio)
    print()
    print('Polinomio de Lagrange: ')
    print(polisimple)"""

    return polisimple,pxi,pfi

# INGRESO , Datos de prueba

def defmatriz(n):
    '''n = int(input("ingrese filas"))
    m = int(input("ingrese columnas"))'''
    #a = n*m
    matriz = []
    n = int(n)
    #val = float(input("ingrese dato: "))
    matriz = [float(input("ingrese dato: ")) for i in range(n)] 

    #print(matriz)
    return matriz

tam = input("ingresa el tamaño de los arreglos: ")

print("Ingrese los datos de Xi: ")
xi = defmatriz(tam)
print("Ingrese los datos Yi: ")
fi = defmatriz(tam)

'''xi = np.array([0, 0.2, 0.3, 0.4])
fi = np.array([1, 1.6, 1.7, 2.0])'''

polisimple,pxi,pfi=Lagrange(xi,fi)

print("Polinomio: ", polisimple)

# Gráfica
plt.plot(xi,fi,'o', label = 'Puntos')
plt.plot(pxi,pfi, label = 'Polinomio')
plt.legend()
plt.xlabel('xi')
plt.ylabel('fi')
plt.title(polisimple)
plt.show()