# Trazador cúbico natural
# Condición: S''(x_0) = S''(x_n) = 0
import numpy as np
import matplotlib.pyplot as plt

def Interpolacion(xi,fi):
    xi = np.array(xi)
    fi = np.array(fi)

    lenXi=len(xi)
    A=np.zeros((lenXi,lenXi))

    for i in range(lenXi):
        A.T[i]=xi**i
    
    a=np.linalg.solve(A,fi)

    xteorico=np.linspace(min(xi),max(xi),100)
    yteorica=0
    for i in range(lenXi):
        yteorica=yteorica+a[i]*xteorico**i
    tabla=[[], []]
    for i in range(len(xteorico)):
        tabla[0].append(xteorico[i])
        tabla[1].append(yteorica[i])
        
    return tabla

'''xi = [1,2,4.5]
fi = [2.5,5,6.7]  '''

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

tabla=Interpolacion(xi,fi)

print("Xi\t\t\tYi")
for i in range(len(tabla[0])):
    print(tabla[0][i],"\t",tabla[1][i])

#Grafica
plt.plot(xi,fi,'ro')
plt.plot(tabla[0],tabla[1],'b-')
plt.legend()
plt.xlabel('X')
plt.ylabel('Y')
plt.title("Interpolacion")
plt.show()