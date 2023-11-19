# Método de Gauss
# Solución a Sistemas de Ecuaciones
# de la forma A.X=B

import numpy as np

def calcular(A,B):
    # PROCEDIMIENTO
    casicero = 1e-15 # Considerar como 0

    # Evitar truncamiento en operaciones
    A = np.array(A,dtype=float) 
    B = np.array(B,dtype=float) 

    # Matriz aumentada
    AB  = np.concatenate((A,B),axis=1)
    AB0 = np.copy(AB)

    # Pivoteo parcial por filas
    tamano = np.shape(AB)
    n = tamano[0]
    m = tamano[1]

    # Para cada fila en AB
    for i in range(0,n-1,1):
        # columna desde diagonal i en adelante
        columna  = abs(AB[i:,i])
        dondemax = np.argmax(columna)
        
        # dondemax no está en diagonal
        if (dondemax !=0):
            # intercambia filas
            temporal = np.copy(AB[i,:])
            AB[i,:] = AB[dondemax+i,:]
            AB[dondemax+i,:] = temporal
    AB1 = np.copy(AB)

    # eliminación hacia adelante
    for i in range(0,n-1,1):
        pivote   = AB[i,i]
        adelante = i + 1
        for k in range(adelante,n,1):
            factor  = AB[k,i]/pivote
            AB[k,:] = AB[k,:] - AB[i,:]*factor

    # sustitución hacia atrás
    ultfila = n-1
    ultcolumna = m-1
    X = np.zeros(n,dtype=float)

    for i in range(ultfila,0-1,-1):
        suma = 0
        for j in range(i+1,ultcolumna,1):
            suma = suma + AB[i,j]*X[j]
        b = AB[i,ultcolumna]
        X[i] = (b-suma)/AB[i,i]

    X = np.transpose([X])

    return (AB0, AB1, AB, X)

# INGRESO

#A = [[4,2,5],[2,5,8],[5,4,3]]
#B = [[60.70],[92.90],[56.30]]
def defmatrizA(n):
    '''n = int(input("ingrese filas"))
    m = int(input("ingrese columnas"))'''
    #a = n*m
    matriz = []
    n = int(n)

    for i in range(n):
        matriz.append([])
        for j in range(n):
            val = float(input("ingrese dato: "))
            matriz[i].append(val)

    #print(matriz)
    return matriz

def defmatrizB(n):
    '''n = int(input("ingrese filas"))
    m = int(input("ingrese columnas"))'''
    #a = n*m
    matriz = []
    n = int(n)
    print("Ingrese los datos de la matriz B: ")
    for i in range(n):
        matriz.append([])
        for j in range(1):
            val = float(input("ingrese dato: "))
            matriz[i].append(val)

    #print(matriz)
    return matriz

tam = input("ingresa el tamaño de la matriz: ")

matA = defmatrizA(tam)
matB = defmatrizB(tam)

print("Matriz A:")
print(matA)
print("Matriz B: ")
print(matB)

# Calcular
(AB0, AB1, AB, X) = calcular(matA,matB)

# SALIDA
print('Matriz aumentada:')
print(AB0)
print('Pivoteo parcial por filas')
print(AB1)
print('eliminación hacia adelante')
print(AB)
print('Matriz X: ')
print(X)
print("Verificacion Ax=B: ")
print(np.dot(matA,X))