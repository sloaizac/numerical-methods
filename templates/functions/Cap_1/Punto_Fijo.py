import sympy as sp
import numpy as np
import pandas as pd
from sympy.plotting import plot

x=sp.symbols('x')

def funcion(ecua='x+2'):
    global x
    return sp.sympify(ecua)

def MetodoPF(ecuacion,x_0,es):
    global x
    ecuacion=funcion(ecuacion)+x 
    plt = plot(ecuacion, show=False)
    ea=100
    x_r=x_0 
    iteracion=0 
    m_itera=np.array([])
    m_xr=np.array([])
    m_error=np.array([])
    #print("\nIteracion\t Xi\t\t\t\t\tError aproximado")
    #print("------------------------------------------------------------------------")
    while ea>es:
        x_anterior=x_r
        x_r=ecuacion.evalf(subs={x:x_anterior})
        iteracion+=1
        if x_r !=0:
            ea=abs((x_r-x_anterior)/x_r)*100
            m_error=np.append(m_error,ea)
        m_itera=np.append(m_itera,iteracion)
        m_xr=np.append(m_xr,x_r)
        #print(iteracion,"\t\t\t",x_r,"\t",ea)
    itera=pd.Series(m_itera,name="Iteracion")
    interXi = pd.Series(m_xr, name="Xi")
    interError =pd.Series(m_error,name="Error")

    tabla=pd.concat([itera,interXi,interError],axis=1)
    return tabla, plt

#iniamos el programa con lo siguiente parametros
#a=MetodoPF('exp(-x)-x',0,0.01)

#fun = input("Ingresa la funcion: ")
#x0 = float(input("Ingresa X0: "))
#es = float(input("Ingresa tolerancia: "))

#esu=MetodoPF(fun,x0,es)

#print("Raiz aproximada: ",resu)