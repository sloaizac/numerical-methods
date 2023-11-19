import sympy as sp
from sympy.plotting import plot
import pandas as pd
import numpy as np

x=sp.symbols('x')

def funcion(ecua):
    global x
    return sp.sympify(ecua)

def newton1(ecuacion,x_0,es,maxIte):
    global x
    ecuacion=funcion(ecuacion)
    derivada=sp.diff(ecuacion)
    plt = plot(ecuacion, show=False)
    f_NR=x-(ecuacion/derivada)#formula de Newton Rhapson
    ea=100 #error aproximado 100%
    m_itera=np.array([]) 
    m_x0=np.array([])   
    m_error=np.array([])
    x_r=x_0 #x_i+1
    interaciones=0
    #print("\nIteracion\t Xi\t\t\tError aproximado")
    #print("------------------------------------------------------------------------")
    while ea>es:
        m_itera=np.append(m_itera,interaciones)
        m_x0=np.append(m_x0,x_r)
        m_error=np.append(m_error,ea)
        x_anterior=x_r # x_anterior = x_i
        x_r=f_NR.evalf(subs={x:x_anterior})
        if x_r !=0:
            ea=abs((x_r-x_anterior)/x_r)*100
        interaciones=interaciones+1
        #print(interaciones,"\t\t",x_r,"\t",ea)
        if interaciones>=maxIte:
            #print("\nEl metodo no converge\n")
            break
    itera=pd.Series(m_itera,name="Iteracion")
    Xi = pd.Series(m_x0, name="Raiz")
    ea = pd.Series(m_error,name="Error")
    tabla=pd.concat([itera,Xi,ea],axis=1)
    return tabla, plt
#iniamos el programa con lo siguiente parametros
#ecua=input("Ecuacion: ")
#x_0=float(input("X0: "))
#tolerancia=float(input("Tolerancia: "))
#maxItera=int(input("Iteraciones: "))
#a=MetodoPF(ecua,x_0,tolerancia,maxItera)
#print("\nRaiz aproximada: ",a)