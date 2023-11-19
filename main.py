from flask import Flask, render_template, request
import numpy as np
from templates.functions.Cap_1.Biseccion import *
from templates.functions.Cap_1.Busqueda_Incremental import *
from templates.functions.Cap_1.Punto_Fijo import *
from templates.functions.Cap_1.Regla_Falsa import *
from templates.functions.Cap_1.Raices_Multiples import *
from templates.functions.Cap_1.Newton import *
from templates.functions.Cap_1.Secante import *
from templates.functions.Cap_2.Jacobi import *
from templates.functions.Cap_2.SOR import *
from templates.functions.Cap_3.Vandermonde import *
from templates.functions.Cap_3.Diferencias_Divididas import *
from templates.functions.Cap_3.Spline_Grado1 import *
from templates.functions.Cap_3.Spline_Grado2 import *
from matplotlib import pyplot
import sympy as sp

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/funciones')
def inicio_funciones():
    return render_template('inicio.html')


@app.route('/sobre_proyecto')
def sobre_proyecto():
    return render_template('sobre_proyecto.html')

@app.route("/bisection", methods=['POST', 'GET'])
def bisection():
    if request.method == 'POST':
        # Obtener los datos del formulario
        func = request.form['func']
        xl = float(request.form['xl'])
        xu = float(request.form['xu'])
        es = float(request.form['es'])
        result, plt = Bisec(func, xl, xu, es)
        
        return render_template('biseccion.html', result=result, plt=plt)
    
    return render_template('biseccion.html', result=None, plt=None)

@app.route("/busqincr", methods=['POST', 'GET'])
def busqincr():
    if request.method == 'POST':
        # Obtener los datos del formulario
        ecuacion = request.form['ecuacion']
        a = float(request.form['a'])
        b = float(request.form['b'])
        deltaX = float(request.form['deltaX'])
        result, plt = Busqueda_Incremental(ecuacion, a, b, deltaX)
        return render_template('busqueda_incr.html', result=result, plt=plt)
        
    return render_template('busqueda_incr.html', result=None, plt=None)

@app.route("/pf", methods=['POST', 'GET'])
def pf():
    if request.method == 'POST':
        # Obtener los datos del formulario
        ecuacion = request.form['ecuacion']
        x_0 = float(request.form['x_0'])
        es = float(request.form['es'])
        
        result, plt = MetodoPF(ecuacion, x_0, es)
        return render_template('pf.html', result=result, plt=plt)
    
    return render_template('pf.html', result=None, plt=None)

@app.route("/falseRule", methods=['POST', 'GET'])
def falseRule():
    if request.method == 'POST':
        # Obtener los datos del formulario
        ecua = request.form['ecua']
        a = float(request.form['a'])
        b = float(request.form['b'])
        tolera = float(request.form['tolera'])
        
        result, plt = Regla_falsa(ecua,a,b,tolera)
        return render_template('falseRule.html', result=result, plt=plt)
    
    return render_template('falseRule.html', result=None, plt=None)

@app.route("/newton", methods=['POST', 'GET'])
def newton():
    if request.method == 'POST':
        # Obtener los datos del formulario
        ecuacion = request.form['ecuation']
        x_0 = float(request.form['x_0'])
        es = float(request.form['es'])
        maxIte =  float(request.form['maxIte'])
        
        result, plt = newton1(ecuacion,x_0,es,maxIte)
        return render_template('newton.html', result=result, plt=plt)
    
    return render_template('newton.html', result=None, plt=None)

@app.route("/multipleRoots", methods=['POST', 'GET'])
def multipleRoots():
    if request.method == 'POST':
        # Obtener los datos del formulario
        ecuacion = request.form['ecuacion']
        x0 = float(request.form['x0'])
        tolerancia = float(request.form['tolerancia'])
        iteraciones = float(request.form['iteraciones'])
        
        result, plt = Raices_Multiples(ecuacion,x0,tolerancia,iteraciones)
        return render_template('multipleRoots.html', result=result, plt=plt)
    
    return render_template('multipleRoots.html', result=None, plt=None)

@app.route("/secant", methods=['POST', 'GET'])
def secant():
    if request.method == 'POST':
        # Obtener los datos del formulario
        fx = request.form['fx']
        a = float(request.form['a'])
        b = float(request.form['b'])
        tolera = float(request.form['tolera'])
        iteraciones = float(request.form['iteraciones'])
        
        result, plt = secante(fx,a,b,tolera,iteraciones)
        return render_template('secant.html', result=result, plt=plt)
    
    return render_template('secant.html', result=None, plt=None)


@app.route("/jacobi", methods=['POST', 'GET'])
def jacobi():
    if request.method == 'POST':
        # Obtener los datos del formulario
        A = request.form['A']
        B = request.form['B']
        ite = float(request.form['ite'])
        tol = float(request.form['tol'])
        matA = np.matrix(A)
        matB = np.matrix(B)
        x0 = np.matrix("0; 0; 0")
        result, tabla = matJacobiSeid(x0,matA,matB,tol,ite, 0)
        
        return render_template('jacobi.html', result=result, tabla=tabla)
        
    return render_template('jacobi.html', result=None, tabla=None)

@app.route("/seidel", methods=['POST', 'GET'])
def seidel():
    if request.method == 'POST':
        # Obtener los datos del formulario
        A = request.form['A']
        B = request.form['B']
        ite = float(request.form['ite'])
        tol = float(request.form['tol'])
        matA = np.matrix(A)
        matB = np.matrix(B)
        x0 = np.matrix("0; 0; 0")
        result, tabla = matJacobiSeid(x0,matA,matB,tol,ite, 1)
        return render_template('seidel.html', result=result, tabla=tabla)
    
    return render_template('seidel.html', result=None, tabla=None)

@app.route("/sor", methods=['POST', 'GET'])
def sor():
    if request.method == 'POST':
        # Obtener los datos del formulario
        A = request.form['A']
        B = request.form['B']
        ite = float(request.form['ite'])
        tol = float(request.form['tol'])
        matA = np.matrix(A)
        matB = np.matrix(B)
        x0 = np.matrix("0; 0; 0")
        result, tabla = SOR(x0,matA,matB,tol,ite, 1.2)
        return render_template('sor.html', result=result, tabla=tabla)
    
    return render_template('sor.html', result=None, tabla=None)

@app.route("/vandermonde", methods=['POST', 'GET'])
def vandermonde():
    if request.method == 'POST':
        # Obtener los datos del formulario
        xi = request.form['xi']
        yi = request.form['yi']
        matriz,coeficiente,polinomio,plt = vander(np.fromstring(xi, dtype=float, sep=' '), np.fromstring(yi, dtype=float, sep=' '))
        return render_template('vandermonde.html', matriz=matriz, coeficiente=coeficiente, polinomio=polinomio, plt=plt)
    
    return render_template('vandermonde.html', matriz=None, coeficiente=None, polinomio=None, plt=None)    

@app.route("/divdif", methods=['POST', 'GET'])
def divdif():
    if request.method == 'POST':
        # Obtener los datos del formulario
        xi = request.form['xi']
        yi = request.form['yi']
        polinomio,plt = Diferencias_Divididas(np.fromstring(xi, dtype=float, sep=' '), np.fromstring(yi, dtype=float, sep=' '))
        return render_template('divdif.html', polinomio=polinomio, plt=plt)
    
    return render_template('divdif.html', polinomio=None, plt=None)  

@app.route("/spline1", methods=['POST', 'GET'])
def spline1():
    if request.method == 'POST':
        # Obtener los datos del formulario
        xi = request.form['xi']
        yi = request.form['yi']
        tabla = trazalineal(np.fromstring(xi, dtype=float, sep=' '), np.fromstring(yi, dtype=float, sep=' '))
        tabla2 = traza3natural(np.fromstring(xi, dtype=float, sep=' '), np.fromstring(yi, dtype=float, sep=' '))
        return render_template('spline1.html', tabla=tabla, plt=None)
    
    return render_template('spline1.html', tabla=None, plt=None)  
        
app.run(host='0.0.0.0', port=81, debug=True)
