import sympy as sp
import numpy as np
import pandas as pd
from sympy.plotting import plot

x=sp.symbols('x')

def funcion(func):
    global x
    return sp.sympify(func)

def Regla_falsa(ecua,a,b,tolera):
    global x
    ecuacion=funcion(ecua)
    tramo = abs(b-a)
    plt = plot(ecuacion, show=False)
    iteracion = 0
    fa = ecuacion.evalf(subs={x:a})
    fb = ecuacion.evalf(subs={x:b})
    m_itera=np.array([])
    m_a=np.array([])
    m_b=np.array([])
    m_fa=np.array([])
    m_fb=np.array([])
    m_xi=np.array([])
    m_fxi=np.array([])
    m_error=np.array([])
    while not(tramo<=tolera):
        c = ((a*fb) - (b*fa))/(fa-fb)
        fc = ecuacion.evalf(subs={x:c})
        iteracion+=1
        m_itera=np.append(m_itera,iteracion)
        m_a=np.append(m_a,a)
        m_b=np.append(m_b,b)
        m_fa=np.append(m_fa,fa)
        m_fb=np.append(m_fb,fb)
        m_xi=np.append(m_xi,c)
        #m_fxi=np.append(m_fxi,fc)
        cambio = np.sign(fa)*np.sign(fc)
        if np.sign(fa) == np.sign(fb):
            print("Error: La función no tiene un cambio de signo en el intervalo dado.")
            return None, None
        if cambio>=0:
            
            tramo = abs(c-a)
            m_error=np.append(m_error,tramo)
            a = c
            fa = fc
        else:
            tramo = abs(b-c)
            m_error=np.append(m_error,tramo)
            b = c
            fb = fc
    itera=pd.Series(m_itera,name="Iteracion")
    intera = pd.Series(m_a, name="a")
    interb = pd.Series(m_b, name="b")
    interfa = pd.Series(m_fa, name="f(a)")
    interfb = pd.Series(m_fb, name="f(b)")
    interxi = pd.Series(m_xi, name="Xi")
    interError =pd.Series(m_error,name="Error")
    #interfxi = pd.Series(m_fxi, name="f(xi)")

    tabla=pd.concat([itera,intera,interb,interfa,interfb,interxi,interError],axis=1)
    return tabla, plt

#fun = input("Ingresa la funcion: ")
#a = float(input("Ingresa intervalo a: "))
#b = float(input("Ingresa intervalo b: "))
#tol = float(input("Ingresa la tolerancia: "))

#(c,tramo)=Regla_falsa('x**3+x**2+2*x+1',-1,0,0.01)
#(Raiz,Error)=Regla_falsa(fun,a,b,tol)

# SALIDA
#print("")
#print('raiz:  ',Raiz)
#print('error: ',Error)