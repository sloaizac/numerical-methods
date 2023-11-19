import numpy as np

def matrizLU(mat):
    m = len(mat)
    matriz=np.zeros([m,m])
    U=np.zeros([m,m])
    L=np.zeros([m,m])

    matriz=np.array(mat,dtype=float) 
    U=np.array(mat,dtype=float)
    #Operaciones para hacer ceros debajo de la diagonal principal

    for k in range(0,m):
        for r in range(0,m):
            if (k==r):
                L[k,r]=1
            if(k<r):
                factor=(matriz[r,k]/matriz[k,k])
                L[r,k]=factor
                for c in range(0,m):
                    matriz[r,c]=matriz[r,c] - (factor*matriz[k,c])
                    U[r,c]=matriz[r,c]
    return L,U

def forward_substitution(L, b):
    AB  = np.concatenate((L,b),axis=1)
    tamano = np.shape(AB)
    n = tamano[0]
    m = tamano[1]
    for i in range(0,n-1,1):
        pivote   = AB[i,i]
        adelante = i + 1
        for k in range(adelante,n,1):
            factor  = AB[k,i]/pivote
            AB[k,:] = AB[k,:] - AB[i,:]*factor
    return AB


def back_substitution(U, y):
    AB  = np.concatenate((U,y),axis=1)
    tamano = np.shape(AB)
    n = tamano[0]
    m = tamano[1]
    ultfila = n-1
    ultcolumna = m-1
    X = np.zeros(n,dtype=float)

    for i in range(ultfila,0-1,-1):
        suma = 0
        for j in range(i+1,n,1):
            suma = suma + AB[i,j]*X[j]
        b = AB[i,ultcolumna]
        X[i] = (b-suma)/AB[i,i]

    X = np.transpose([X])
    return X

def Doolittle(A,b):
    A=np.array(A,dtype=float)
    b=np.array(b,dtype=float)

    L,U= matrizLU(A)
    z=forward_substitution(L,b)
    x=back_substitution(U,z)
    return L,U,x

'''A = np.array([
    [2, -1, -2],
    [-4, 6, 3],
    [-4, -2, -8]
])

b = np.array([-1, 13, -6])'''

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

A = defmatrizA(tam)
B = defmatrizB(tam)

(L,U,X)=Doolittle(A, B)
print("Matriz A: ")
print(A)
print("Matriz B: ")
print(B)
print("Matriz L")
print(L)
print("Matriz U")
print(U)
print("Solucion")
print(X)
print("Verificacion Ax=B: ")
print(np.dot(A,X))