from flask import Flask , request
import random

app = Flask(__name__)

@app.route('/')

def home():
    return '''

<h1> Aplicación Calculadora </h1> 

<p> Opciones Disponibles: </p>

<ul>

    <li> <a href="/suma?a=8&b=12"> Suma  </li>
    <li> <a href="/resta?num1=15&num2=5"> Resta </li>
    <li> <a href="/multiplicacion?dig1=4&dig2=6"> Multiplicación </li>
    <li> <a href="/division?divd=5&divs=2"> División </li>


        
</ul>    

'''




#Esta es una de las rutas adicionales en la aplicación 
@app.route('/suma')
def ruta_suma():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    resultado= a + b
    return f'''
    <h2> "La suma de los numeros {a} y {b} es: {resultado}" </h2>
    <br> <a href="/"> Volver al Home </a>
    '''


@app.route('/resta')
def ruta_resta():
    num1 = request.args.get('num1', type=float)
    num2 = request.args.get('num2', type=float)
    resultado= num1 - num2
    return f'''
    <h2> "La resta de los numeros {num1} y {num2} es: {resultado}" </h2>
    <br> <a href="/"> Volver al Home </a>
    '''

@app.route('/multiplicacion')
def ruta_multiplicacion():
    dig1 = request.args.get('dig1', type=float)
    dig2 = request.args.get('dig2', type=float)
    resultado= dig1 * dig2
    return f'''
    <h2> "La multiplicación de los numeros {dig1} y {dig2} es: {resultado}" </h2>
    <br> <a href="/"> Volver al Home </a>
    '''

@app.route('/division')
def ruta_division():
    divd = request.args.get('divd', type=float)
    divs = request.args.get('divs', type=float)
    if divs != 0:
        #el resultado debe redondearse a división de piso 
        resultado= divd // divs  
        return f'''
        <h2> "La división de los numeros {divd} y {divs} es: {resultado}" </h2>
        <br> <a href="/"> Volver al Home </a>
        '''
    else:
        return "Error: No se puede dividir por cero."








# Este apartado nos permite actulizar rapidamente los cambios realizados en el código sin necesidad de reiniciar el servidor cada vez que se realice una modificación.
if __name__ == '__main__':
    app.run(debug=True)

