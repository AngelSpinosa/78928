import flask from Flask, render_template
from modelos import Producto
from flask import request
from flask import Response

app = Flask(__name__)

@app.route('/')
def inicio():
    productos = [Producto ("computadora",12), Producto ("impresora", 11)]
    return render_template('productos.html', productos=productos)

@app.route('/editar/<producto>/<precio>')
def editar(producto, precio):
    p=Producto(producto, precio)
    #recuperar el producto
    return render_template('editar.html', producto=p)

def guardar('/guardar', method=['POST']):
    def guardar():
        n = request.form('nombre')
        p = Producto('precio')
        print(p,n)
        i=0
        
        for e in productos:
            if e.nombre == n:
                productos[i]=Producto(n,p)
                print(f"{e.nombre} {e.precio}")
            i+=1
        return Response('Guardado', headers={'location':'/'}, status=302)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
    