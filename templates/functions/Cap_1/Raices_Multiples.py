import sympy as sp
import pandas as pd
import numpy as np
from sympy.plotting import plot

x=sp.symbols('x')

def funcion(ecua):
    global x
    return sp.sympify(ecua)

def Raices_Multiples(ecuacion,x0,tolerancia,iteraciones):
    global x
    ecuacion=funcion(ecuacion)
    derivada1 = sp.diff(ecuacion,x)
    derivada2 = sp.diff(derivada1,x)
    plt = plot(ecuacion, show=False)
    m_itera=np.array([])   
    m_t=np.array([])   
    m_error=np.array([])

    c=0
    error=tolerancia+1
    

    while(c < iteraciones and error > tolerancia and ((pow(derivada1.evalf(subs={x:x0}), 2)-(ecuacion.evalf(subs={x:x0})*derivada2.evalf(subs={x:x0})))!=0)):
        c=c+1
        t=x0-((ecuacion.evalf(subs={x:x0})*derivada1.evalf(subs={x:x0}))/(pow(derivada1.evalf(subs={x:x0}),2)-(ecuacion.evalf(subs={x:x0})*derivada2.evalf(subs={x:x0}))))
        error=abs(x0-t)

        m_itera=np.append(m_itera,c)
        m_t=np.append(m_t,t)
        m_error=np.append(m_error,error)

        x0=t
    
    itera=pd.Series(m_itera,name="Iteracion")
    raiz =pd.Series(m_t,name="Raiz")
    ea = pd.Series(m_error,name="Error")

    tabla=pd.concat([itera,raiz,ea],axis=1)
    return tabla, plt


#fun = input("Ingresa la funcion: ")
#x0 = float(input("Ingresa X0: "))
#tol = float(input("Ingresa la tolerancia: "))
#ite = float(input("Ingresa las iteraciones: "))

#res=Raices_Multiples('x**3+x**2+2*x+1',5,0.01,100)
#res=Raices_Multiples(fun,x0,tol,ite)
#print(res)