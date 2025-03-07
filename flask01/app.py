from flask import Flask
app = Flask (__name__)
@app.route('/')
def hola_mundo():
    return 'Hola Mundo'
<<<<<<< HEAD
if __name__ == "__main__":
    app.run(host='0.0.0.0')
=======
    
@app.route('/hola')
def hola_html():
    return '<h1 style="color:red;">Hola Mundo</h1>'
    
@app.route('/json')
def algo():
    return '{"nombre":"john}'

app route('/xml')
def xml():
    return '<?xml version="1.0" encoding="UTF-8" ?><nombre>John</nombre>'

if __name__ == "__main__":
    app.run(host='0.0.0.0'
debug=True)
>>>>>>> 3b1781c (Rutas en flask)
