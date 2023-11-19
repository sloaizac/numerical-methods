import sympy as sp
import pandas as pd
import numpy as np
from sympy.plotting import plot

x=sp.symbols('x')


def funcion(func):
    global x
    return sp.sympify(func)

#metodo de la biseccion
def Bisec(func,xl,xu,es):
    func=funcion(func)
    itera=0 
    plt = plot(func, show=False)
    m_itera=np.array([]) #matriz q almacena valores de itera
    m_xl=np.array([])   #matriz q alamacena valores de xl
    m_xu=np.array([])   #matriz q alamcena valores de xu
    xr=0
    m_xr=np.array([])   #matriz q almacena valroes de xr
    ea=100 
    m_ea=np.array([])   #matriz q alamcena valore s de ea
    fl=func.evalf(subs={x: xl}) #reamplazmos x por xl y evaluamos la funcion
    #incio del bucle
    while ea>es :
        
        xanterior=xr
        xr=(xl+xu)/2
        fr=func.evalf(subs={x:xr})
        itera=itera+1
        if xr != 0:
            ea=abs((xr-xanterior)/xr)*100
        test=fl*fr
        #agregamos valores a las matrices vacias
        m_itera=np.append(m_itera,itera)
        m_xl=np.append(m_xl,xl)
        m_xu=np.append(m_xu,xu)
        m_xr=np.append(m_xr,xr)
        m_ea=np.append(m_ea,ea)                     
        
        if test < 0 :
            xu=xr
        elif test >0:
            xl=xr
            fl=fr
        else:
            ea=0
    #representamos datos en pandas
    iteracion=pd.Series(m_itera,name="Iteracion")
    xl=pd.Series(m_xl,name="Intervalo a")
    xu=pd.Series(m_xu,name="Intervalo b")
    xr=pd.Series(m_xr,name="Raiz")
    ea=pd.Series(m_ea,name="Error")
    tabla=pd.concat([iteracion,xl,xu,xr,ea],axis=1) #unimos en columnas
    return tabla, plt

#fun = input("Ingresa la funcion: ")
#xl = float(input("Ingresa intervalo a: "))
#xu = float(input("Ingresa intervalo b: "))
#es = float(input("Ingresa tolerancia: "))

#a=Bisec(fun,xl,xu,es)

#a=Bisec('x**10-1',0,0.1,0.01)
#print(a)