from flask import Flask
from rutas impor rutas_bp

app = Flask(__name__)
app.register_blueprint(rutas_bp)

@app.route('/')
def inicio():
    return 'Inicio'

if _name_ == '__main__':
    app.run(host='0.0.0.0', debug=True)