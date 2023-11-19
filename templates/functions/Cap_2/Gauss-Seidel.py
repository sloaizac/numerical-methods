import numpy as np

# PROCEDIMIENTO

# Gauss-Seidel
def Gauss_Seidel(A,B,X0,tolera,iteramax):
  A = np.array(A,dtype=float) 
  B = np.array(B,dtype=float)
  D = np.diag(np.diag(A))
  L = -np.tril(A, -1)
  U = -np.triu(A, 1)
  T = np.linalg.inv(D - L) @ (D + U)
  tamano = np.shape(A)
  n = tamano[0]
  m = tamano[1]
  #  valores iniciales
  X = np.copy(X0)
  diferencia = np.ones(n, dtype=float)
  errado = 2*tolera

  itera = 0
  while not(errado<=tolera or itera>iteramax):
      # por fila
      for i in range(0,n,1):
          # por columna
          suma = 0 
          for j in range(0,m,1):
              # excepto diagonal de A
              if (i!=j): 
                  suma = suma-A[i,j]*X[j]
          
          nuevo = (B[i]+suma)/A[i,i]
          diferencia[i] = np.abs(nuevo-X[i])
          X[i] = nuevo
      errado = np.max(diferencia)
      itera = itera + 1

  # Respuesta X en columna
  X = np.transpose([X])

  # revisa si NO converge
  if (itera>iteramax):
      X=0
  # revisa respuesta
  verifica = np.dot(A,X)

  return X, verifica

# INGRESO
'''A = np.array([[3. , -0.1, -0.2],
              [0.1,  7  , -0.3],
              [0.3, -0.2, 10  ]])

B = np.array([7.85,-19.3,71.4])
'''

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
    
    for i in range(n):
        matriz.append([])
        for j in range(1):
            val = float(input("ingrese dato: "))
            matriz[i].append(val)

    #print(matriz)
    return matriz

#tam = input("ingresa el tamaño de la matriz: ")

#matA = defmatrizA(tam)
#print("Ingrese los datos de la matriz B: ")
#matB = defmatrizB(tam)
#print("Ingrese los datos de la matriz X0: ")
#X0  =defmatrizB(tam)
#tolera = float(input("ingresa la tolerancia: "))
#iteramax = int(input("ingresa las iteraciones: "))
#(X, verifica) = Gauss_Seidel(matA,matB,X0,tolera,iteramax)

# SALIDA
#print("Matriz A:")
#print(matA)
#print("Matriz B: ")
#print(matB)
#print('respuesta X: ')
#print(X)
#print('verificar A.X=B: ')
#print(verifica)