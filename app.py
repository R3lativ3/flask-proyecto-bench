from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'tu-clave-secreta-aqui')

# Configuración de MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'mysql+pymysql://root:password@localhost/proyecto_bench')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Datos de ejemplo (en un proyecto real usarías una base de datos)
proyectos = [
    {'id': 1, 'nombre': 'Proyecto Alpha', 'descripcion': 'Sistema de gestión de usuarios'},
    {'id': 2, 'nombre': 'Proyecto Beta', 'descripcion': 'API de pagos'},
    {'id': 3, 'nombre': 'Proyecto Gamma', 'descripcion': 'Dashboard analítico'}
]

usuarios = [
    {'id': 1, 'nombre': 'Juan Pérez', 'email': 'juan@ejemplo.com', 'rol': 'developer'},
    {'id': 2, 'nombre': 'María García', 'email': 'maria@ejemplo.com', 'rol': 'admin'},
    {'id': 3, 'nombre': 'Carlos López', 'email': 'carlos@ejemplo.com', 'rol': 'developer'}
]

@app.route('/')
def index():
    return render_template('index.html', proyectos=proyectos[:3])

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/proyectos')
def proyectos_lista():
    return render_template('proyectos.html', proyectos=proyectos)

@app.route('/proyecto/<int:proyecto_id>')
def proyecto_detalle(proyecto_id):
    proyecto = next((p for p in proyectos if p['id'] == proyecto_id), None)
    if not proyecto:
        flash('Proyecto no encontrado', 'error')
        return redirect(url_for('proyectos_lista'))
    return render_template('proyecto_detalle.html', proyecto=proyecto)

@app.route('/usuarios')
def usuarios_lista():
    return render_template('usuarios.html', usuarios=usuarios)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        email = request.form.get('email')
        mensaje = request.form.get('mensaje')
        
        # Aquí procesarías el formulario
        flash(f'Gracias {nombre}, tu mensaje ha sido enviado!', 'success')
        return redirect(url_for('contact'))
    
    return render_template('contact.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)