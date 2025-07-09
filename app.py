from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_cors import CORS  # Agregar esta línea
import json
import os
from datetime import datetime

app = Flask(__name__)
CORS(app)  # Agregar esta línea
app = Flask(__name__, template_folder='app/templates', static_folder='app/static') # asignamos donde estan los templates y los archivos estáticos
app.secret_key = os.getenv('SECRET_KEY', 'tu-clave-secreta-super-segura-aqui')

# Configuración para JSON
DATA_FOLDER = 'data'

def ensure_data_folder():
    """Crear carpeta data si no existe"""
    if not os.path.exists(DATA_FOLDER):
        os.makedirs(DATA_FOLDER)

def load_json_data(filename):
    """Cargar datos desde archivo JSON"""
    filepath = os.path.join(DATA_FOLDER, filename)
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def save_json_data(filename, data):
    """Guardar datos en archivo JSON"""
    ensure_data_folder()
    filepath = os.path.join(DATA_FOLDER, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def init_default_data():
    """Inicializar datos por defecto si no existen"""
    # Usuarios completos con datos ficticios
    usuarios_default = {
        "usuarios": [
            {
                "id": 1,
                "nombre": "Ana García",
                "email": "ana.garcia@empresa.com",
                "rol": "tech_lead",
                "activo": True,
                "fecha_registro": "2023-12-01T09:00:00",
                "skills": ["React", "Node.js", "Python", "Leadership"],
                "seniority": "senior"
            },
            {
                "id": 2,
                "nombre": "Carlos Rodríguez",
                "email": "carlos.rodriguez@empresa.com",
                "rol": "developer",
                "activo": True,
                "fecha_registro": "2024-01-15T10:30:00",
                "skills": ["Vue.js", "Laravel", "MySQL", "Docker"],
                "seniority": "mid"
            },
            {
                "id": 3,
                "nombre": "María López",
                "email": "maria.lopez@empresa.com",
                "rol": "developer",
                "activo": True,
                "fecha_registro": "2024-01-20T11:00:00",
                "skills": ["React Native", "Flutter", "Firebase"],
                "seniority": "junior"
            },
            {
                "id": 4,
                "nombre": "Diego Martínez",
                "email": "diego.martinez@empresa.com",
                "rol": "developer",
                "activo": True,
                "fecha_registro": "2023-11-10T14:15:00",
                "skills": ["Angular", "Spring Boot", "PostgreSQL"],
                "seniority": "senior"
            },
            {
                "id": 5,
                "nombre": "Sofia Chen",
                "email": "sofia.chen@empresa.com",
                "rol": "designer",
                "activo": True,
                "fecha_registro": "2024-02-01T08:30:00",
                "skills": ["Figma", "UI/UX", "Frontend", "Design Systems"],
                "seniority": "mid"
            },
            {
                "id": 6,
                "nombre": "Roberto Silva",
                "email": "roberto.silva@empresa.com",
                "rol": "developer",
                "activo": False,
                "fecha_registro": "2023-09-15T16:00:00",
                "skills": ["PHP", "WordPress", "jQuery"],
                "seniority": "mid",
                "fecha_salida": "2024-06-30"
            }
        ]
    }
    
    # Proyectos realistas con datos completos
    proyectos_default = {
        "proyectos": [
            {
                "id": 1,
                "nombre": "E-commerce Mobile App",
                "descripcion": "Aplicación móvil para tienda online con carrito, pagos y notificaciones push",
                "fecha_inicio": "2024-02-01",
                "fecha_fin": "2024-06-30",
                "estado": "activo",
                "core_developers": [1, 3],
                "bench_developers": [2],
                "tecnologias": ["React Native", "Node.js", "MongoDB", "Stripe"],
                "cliente": "TechStore S.A.",
                "presupuesto": 85000,
                "prioridad": "alta"
            },
            {
                "id": 2,
                "nombre": "Sistema de Gestión Escolar",
                "descripcion": "Plataforma web para administrar estudiantes, profesores, calificaciones y horarios",
                "fecha_inicio": "2024-01-15",
                "fecha_fin": "2024-08-15",
                "estado": "activo",
                "core_developers": [4],
                "bench_developers": [2, 5],
                "tecnologias": ["Angular", "Spring Boot", "PostgreSQL", "Docker"],
                "cliente": "Colegio San Martín",
                "presupuesto": 120000,
                "prioridad": "media"
            },
            {
                "id": 3,
                "nombre": "Dashboard Analytics",
                "descripcion": "Tablero de control con métricas en tiempo real y reportes automáticos",
                "fecha_inicio": "2024-03-01",
                "fecha_fin": "2024-05-31",
                "estado": "planificacion",
                "core_developers": [1],
                "bench_developers": [4, 5],
                "tecnologias": ["React", "D3.js", "Python", "Redis"],
                "cliente": "DataCorp Inc.",
                "presupuesto": 95000,
                "prioridad": "alta"
            },
            {
                "id": 4,
                "nombre": "API de Facturación",
                "descripcion": "Microservicio para generar y gestionar facturas electrónicas",
                "fecha_inicio": "2023-11-01",
                "fecha_fin": "2024-02-29",
                "estado": "completado",
                "core_developers": [2, 4],
                "bench_developers": [],
                "tecnologias": ["Laravel", "MySQL", "PDF", "SOAP"],
                "cliente": "FactuFácil LTDA",
                "presupuesto": 45000,
                "prioridad": "baja"
            },
            {
                "id": 5,
                "nombre": "App de Delivery",
                "descripcion": "Aplicación para pedidos de comida con tracking en tiempo real",
                "fecha_inicio": "2024-04-01",
                "fecha_fin": "2024-09-30",
                "estado": "planificacion",
                "core_developers": [3],
                "bench_developers": [1, 2],
                "tecnologias": ["Flutter", "Node.js", "Socket.io", "Maps API"],
                "cliente": "FoodExpress",
                "presupuesto": 135000,
                "prioridad": "alta"
            }
        ]
    }
    
    # Asignaciones realistas
    asignaciones_default = {
        "asignaciones": [
            {
                "id": 1,
                "proyecto_id": 1,
                "usuario_id": 1,
                "tipo": "core",
                "fecha_asignacion": "2024-02-01",
                "fecha_fin": "2024-06-30",
                "porcentaje_dedicacion": 80,
                "activa": True,
                "rol_proyecto": "Tech Lead"
            },
            {
                "id": 2,
                "proyecto_id": 1,
                "usuario_id": 3,
                "tipo": "core",
                "fecha_asignacion": "2024-02-15",
                "fecha_fin": "2024-06-30",
                "porcentaje_dedicacion": 100,
                "activa": True,
                "rol_proyecto": "Mobile Developer"
            },
            {
                "id": 3,
                "proyecto_id": 1,
                "usuario_id": 2,
                "tipo": "bench",
                "fecha_asignacion": "2024-03-01",
                "fecha_fin": "2024-04-30",
                "porcentaje_dedicacion": 40,
                "activa": True,
                "rol_proyecto": "Backend Support"
            },
            {
                "id": 4,
                "proyecto_id": 2,
                "usuario_id": 4,
                "tipo": "core",
                "fecha_asignacion": "2024-01-15",
                "fecha_fin": "2024-08-15",
                "porcentaje_dedicacion": 90,
                "activa": True,
                "rol_proyecto": "Full Stack Lead"
            },
            {
                "id": 5,
                "proyecto_id": 2,
                "usuario_id": 2,
                "tipo": "bench",
                "fecha_asignacion": "2024-02-01",
                "fecha_fin": "2024-03-31",
                "porcentaje_dedicacion": 60,
                "activa": False,
                "rol_proyecto": "Backend Developer"
            },
            {
                "id": 6,
                "proyecto_id": 2,
                "usuario_id": 5,
                "tipo": "bench",
                "fecha_asignacion": "2024-01-20",
                "fecha_fin": "2024-08-15",
                "porcentaje_dedicacion": 50,
                "activa": True,
                "rol_proyecto": "UI/UX Designer"
            }
        ]
    }
    
    # Solicitudes variadas
    solicitudes_default = {
        "solicitudes": [
            {
                "id": 1,
                "usuario_id": 3,
                "proyecto_id": 1,
                "tipo": "dias_libres",
                "fecha_inicio": "2024-03-15",
                "fecha_fin": "2024-03-18",
                "motivo": "Vacaciones de Semana Santa",
                "estado": "aprobada",
                "fecha_solicitud": "2024-03-01T09:00:00",
                "aprobado_por": 1,
                "fecha_aprobacion": "2024-03-02T14:30:00"
            },
            {
                "id": 2,
                "usuario_id": 2,
                "proyecto_id": 2,
                "tipo": "refuerzo",
                "fecha_inicio": "2024-04-01",
                "fecha_fin": "2024-04-30",
                "motivo": "Necesitamos acelerar el desarrollo del módulo de reportes",
                "estado": "pendiente",
                "fecha_solicitud": "2024-03-25T16:45:00",
                "desarrolladores_solicitados": [4, 5],
                "horas_adicionales": 40
            },
            {
                "id": 3,
                "usuario_id": 4,
                "proyecto_id": 2,
                "tipo": "cambio_asignacion",
                "fecha_inicio": "2024-05-01",
                "fecha_fin": "2024-05-31",
                "motivo": "Reducir dedicación por compromisos en otro proyecto",
                "estado": "rechazada",
                "fecha_solicitud": "2024-04-20T11:15:00",
                "nuevo_porcentaje": 60,
                "rechazado_por": 1,
                "fecha_rechazo": "2024-04-22T09:00:00",
                "motivo_rechazo": "Período crítico del proyecto, no es posible reducir dedicación"
            }
        ]
    }
    
    # Crear archivos si no existen
    if not os.path.exists(os.path.join(DATA_FOLDER, 'usuarios.json')):
        save_json_data('usuarios.json', usuarios_default)
    
    if not os.path.exists(os.path.join(DATA_FOLDER, 'proyectos.json')):
        save_json_data('proyectos.json', proyectos_default)
    
    if not os.path.exists(os.path.join(DATA_FOLDER, 'asignaciones.json')):
        save_json_data('asignaciones.json', asignaciones_default)
    
    if not os.path.exists(os.path.join(DATA_FOLDER, 'solicitudes.json')):
        save_json_data('solicitudes.json', solicitudes_default)

def get_proyectos():
    """Obtener lista de proyectos desde JSON"""
    data = load_json_data('proyectos.json')
    return data.get('proyectos', [])

def get_usuarios():
    """Obtener lista de usuarios desde JSON"""
    data = load_json_data('usuarios.json')
    return data.get('usuarios', [])

def get_proyecto_by_id(proyecto_id):
    """Obtener proyecto específico por ID"""
    proyectos = get_proyectos()
    return next((p for p in proyectos if p['id'] == proyecto_id), None)

def get_asignaciones_by_proyecto(proyecto_id):
    """Obtener asignaciones de un proyecto específico"""
    data = load_json_data('asignaciones.json')
    asignaciones = data.get('asignaciones', [])
    return [a for a in asignaciones if a['proyecto_id'] == proyecto_id and a['activa']]

def get_usuario_by_id(usuario_id):
    """Obtener usuario específico por ID"""
    usuarios = get_usuarios()
    return next((u for u in usuarios if u['id'] == usuario_id), None)

# ===== RUTAS ORIGINALES (mantenidas igual) =====

@app.route('/')
def index():
    proyectos = get_proyectos()[:3]  # Mostrar solo los primeros 3
    return render_template('index.html', proyectos=proyectos)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/proyectos')
def proyectos_lista():
    proyectos = get_proyectos()
    return render_template('proyectos.html', proyectos=proyectos)

@app.route('/proyecto/<int:proyecto_id>')
def proyecto_detalle(proyecto_id):
    proyecto = get_proyecto_by_id(proyecto_id)
    if not proyecto:
        flash('Proyecto no encontrado', 'error')
        return redirect(url_for('proyectos_lista'))
    
    # Obtener información adicional del proyecto
    asignaciones = get_asignaciones_by_proyecto(proyecto_id)
    
    # Agregar nombres de usuarios a las asignaciones
    for asignacion in asignaciones:
        usuario = get_usuario_by_id(asignacion['usuario_id'])
        if usuario:
            asignacion['usuario_nombre'] = usuario['nombre']
            asignacion['usuario_email'] = usuario['email']
    
    return render_template('proyecto_detalle.html', proyecto=proyecto, asignaciones=asignaciones)

@app.route('/usuarios')
def usuarios_lista():
    usuarios = get_usuarios()
    # Filtrar solo usuarios activos
    usuarios_activos = [u for u in usuarios if u.get('activo', True)]
    return render_template('usuarios.html', usuarios=usuarios_activos)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        email = request.form.get('email')
        mensaje = request.form.get('mensaje')
        
        # Aquí podrías guardar en un JSON de contactos
        flash(f'Gracias {nombre}, tu mensaje ha sido enviado!', 'success')
        return redirect(url_for('contact'))
    
    return render_template('contact.html')

# ===== RUTAS ADICIONALES PARA DATOS JSON =====

@app.route('/api/datos')
def api_datos():
    """API para obtener todos los datos JSON"""
    return jsonify({
        "usuarios": load_json_data('usuarios.json'),
        "proyectos": load_json_data('proyectos.json'),
        "asignaciones": load_json_data('asignaciones.json'),
        "solicitudes": load_json_data('solicitudes.json')
    })

@app.route('/api/proyectos')
def api_proyectos():
    """API para obtener solo proyectos"""
    return jsonify(get_proyectos())

@app.route('/api/usuarios')
def api_usuarios():
    """API para obtener solo usuarios"""
    return jsonify(get_usuarios())

@app.route('/dashboard')
def dashboard():
    """Dashboard con estadísticas"""
    proyectos = get_proyectos()
    usuarios = get_usuarios()
    
    # Estadísticas simples
    stats = {
        'total_proyectos': len(proyectos),
        'proyectos_activos': len([p for p in proyectos if p['estado'] == 'activo']),
        'total_usuarios': len([u for u in usuarios if u.get('activo', True)]),
        'presupuesto_total': sum(p.get('presupuesto', 0) for p in proyectos if p['estado'] == 'activo')
    }
    
    return jsonify(stats)

@app.route('/solicitudes')
def solicitudes_lista():
    """Ver todas las solicitudes"""
    data = load_json_data('solicitudes.json')
    solicitudes = data.get('solicitudes', [])
    
    # Agregar nombres de usuarios y proyectos
    for solicitud in solicitudes:
        usuario = get_usuario_by_id(solicitud['usuario_id'])
        proyecto = get_proyecto_by_id(solicitud['proyecto_id'])
        
        if usuario:
            solicitud['usuario_nombre'] = usuario['nombre']
        if proyecto:
            solicitud['proyecto_nombre'] = proyecto['nombre']
    
    return jsonify(solicitudes)

if __name__ == '__main__':
    print("🚀 Iniciando Proyecto Bench (versión JSON)...")
    print("📁 Inicializando datos JSON...")
    init_default_data()
    print("✅ Servidor listo en http://localhost:5000")
    print("📊 Datos ficticios cargados:")
    print("   - 6 usuarios con skills y roles")
    print("   - 5 proyectos con presupuestos reales")
    print("   - 6 asignaciones core/bench")
    print("   - 3 solicitudes de ejemplo")
    print("\n🌐 Rutas disponibles:")
    print("   http://localhost:5000/ - Página principal")
    print("   http://localhost:5000/proyectos - Lista de proyectos")
    print("   http://localhost:5000/usuarios - Lista de usuarios")
    print("   http://localhost:5000/api/datos - API completa JSON")
    print("   http://localhost:5000/dashboard - Estadísticas")
    app.run(debug=True)