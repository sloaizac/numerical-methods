import sympy as sp
import pandas as pd
import numpy as np
from sympy.plotting import plot

x=sp.symbols('x')

def funcion(ecua):
    global x
    return sp.sympify(ecua)

def secante(fx,a,b,tolera,iteraciones):
    global x
    fx=funcion(fx)
    E=tolera+1
    xi=a
    x0=b
    c=0
    plt = plot(fx, show=False)
    m_itera=np.array([]) 
    m_x0=np.array([])   
    m_error=np.array([])

    while (E>tolera and c<iteraciones and (fx.evalf(subs={x:x0})-fx.evalf(subs={x:xi}))!=0):
        c=c+1
        x2=x0-((fx.evalf(subs={x:x0})*(x0-xi))/(fx.evalf(subs={x:x0})-fx.evalf(subs={x:xi})))

        
        m_itera=np.append(m_itera,c)
        m_x0=np.append(m_x0,x0)
        m_error=np.append(m_error,E)
        E=abs(xi-x0)
        x0=xi
        xi=x2
        
        

    itera=pd.Series(m_itera,name="Iteracion")
    Xi = pd.Series(m_x0, name="Raiz")
    ea = pd.Series(m_error,name="Error")

    tabla=pd.concat([itera,Xi,ea],axis=1)
    return tabla, plt

#fun = input("Ingresa la funcion: ")
#a = float(input("Ingresa intervalo a: "))
#b = float(input("Ingresa intervalo b: "))
#tol = float(input("Ingresa la tolerancia: "))
#ite = float(input("Ingresa las iteraciones: "))

#res=secante('x**3+x**2+2*x+1',-1,0,0.001,100)
#res=secante(fun,a,b,tol,ite)
#print(res)