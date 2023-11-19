import numpy as np
import pandas as pd

def SOR(x0, A, b, Tol, niter, w):
    c = 0
    error = Tol + 1
    D = np.diag(np.diag(A))
    L = -np.tril(A, -1)
    U = -np.triu(A, 1)
    err=np.array([])
    m_itera=np.array([]) 
    m_x=np.array([])  
    while error > Tol and c < niter:
        T = np.linalg.inv(D - w*L) @ ((1 - w)*D + w*U)
        C = w * np.linalg.inv(D - w*L) @ b
        x1 = T @ x0 + C
        E = np.linalg.norm(x1 - x0, np.inf)
        err = np.append(err, E)
        m_itera=np.append(m_itera,c)
        m_x=np.append(m_x,str(x1).replace("\n", ""))
        error = E
        x0 = x1
        c += 1

    if error < Tol:
        s = x0
        n = c
        print(f'Es una aproximación de la solución del sistema con una tolerancia = {Tol}')
    else:
        s = x0
        n = c
        print(f'Fracasó en {niter} iteraciones')
    itera=pd.Series(m_itera,name="Iteration")
    err=pd.Series(err,name="Error")
    Xi = pd.Series(m_x, name="")

    tabla=pd.concat([itera,err,Xi],axis=1)

    return pd.DataFrame(s), tabla

