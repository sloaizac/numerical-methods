import sympy as sp
import pandas as pd
import numpy as np
from sympy.plotting import plot

x=sp.symbols('x')

def funcion(ecua):
    global x
    return sp.sympify(ecua)

def Busqueda_Incremental(ecuacion, a, b, deltaX):
    global x
    ecuacion=funcion(ecuacion)

    iteracion=0
    plt = plot(ecuacion, show=False)
    m_itera=np.array([])
    m_a=np.array([])
    m_xi=np.array([])
    while(a<b):
        Xi = a + deltaX
        FunA = ecuacion.evalf(subs={x:a})
        FunXi = ecuacion.evalf(subs={x:Xi})
        if (FunA *FunXi )<0:
            iteracion=iteracion+1
            m_itera=np.append(m_itera,iteracion)
            m_a=np.append(m_a,a)
            m_xi=np.append(m_xi,Xi)
            a=Xi
        else:
            a=Xi
        itera=pd.Series(m_itera,name="Raiz")
        interA = pd.Series(m_a, name="Xi-dx")
        interXi =pd.Series(m_xi,name="Xi")

        tabla=pd.concat([itera,interA,interXi],axis=1)
    return tabla, plt
        


#iniamos el programa con lo siguiente parametros
#res = Busqueda_Incremental('sin(x)',-7,7,0.3)

