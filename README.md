# Proyecto Bench - Sistema de Gestión de Desarrolladores

Sistema Flask para gestionar desarrolladores core y bench en proyectos de desarrollo.

## ¿Qué es?

Un sistema que permite:
- Asignar desarrolladores como "Core" (responsables principales) o "Bench" (soporte) en proyectos
- Solicitar días libres y refuerzos
- Visualizar calendario de asignaciones
- Gestionar usuarios y proyectos

## Cómo ejecutar

### 1. Configurar MySQL
Primero instala MySQL y crea una base de datos:
```sql
CREATE DATABASE proyecto_bench;
CREATE USER 'usuario'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON proyecto_bench.* TO 'usuario'@'localhost';
FLUSH PRIVILEGES;
```

### 2. Crear entorno virtual
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

**Nota**: Si tienes problemas con `mysqlclient`, puedes instalar solo PyMySQL:
```bash
pip install PyMySQL
```

### 4. Configurar variables de entorno
```bash
cp .env.example .env
# Editar .env con tus credenciales de MySQL
```

### 5. Ejecutar la aplicación
```bash
python app.py
```

### 6. Abrir en navegador
```
http://localhost:5000
```

## Configuración de MySQL

### Opción 1: Usar Docker (recomendado)
```bash
docker run --name mysql-proyecto-bench -e MYSQL_ROOT_PASSWORD=rootpass -e MYSQL_DATABASE=proyecto_bench -e MYSQL_USER=usuario -e MYSQL_PASSWORD=password -p 3306:3306 -d mysql:8.0
```

### Opción 2: Instalación local
- **Ubuntu/Debian**: `sudo apt install mysql-server`
- **macOS**: `brew install mysql`
- **Windows**: Descargar de mysql.com

## Estructura del proyecto

```
flask-proyecto-bench/
├── app.py                 # Aplicación principal
├── requirements.txt       # Dependencias
├── README.md             # Esta documentación
└── app/
    ├── static/
    │   ├── css/
    │   │   └── style.css  # Estilos personalizados
    │   └── js/
    │       └── main.js    # JavaScript principal
    └── templates/
        ├── base.html      # Plantilla base
        ├── index.html     # Página principal
        ├── proyectos.html # Lista de proyectos
        ├── proyecto_detalle.html # Detalle de proyecto
        ├── usuarios.html  # Lista de usuarios
        ├── about.html     # Acerca de
        └── contact.html   # Contacto
```

## Rutas disponibles

- `/` - Página principal con Hello World
- `/proyectos` - Lista de proyectos
- `/proyecto/<id>` - Detalle de proyecto específico
- `/usuarios` - Lista de usuarios
- `/about` - Información del proyecto
- `/contact` - Formulario de contacto

## Tecnologías utilizadas

- **Backend**: Flask, SQLAlchemy, Flask-Login, WTForms
- **Frontend**: HTML5, CSS3, Bootstrap 5, JavaScript
- **Base de datos**: MySQL

## Próximos pasos de desarrollo

### Sprint 1: Bootstrap + Base de datos
- Configurar SQLAlchemy y Flask-Migrate
- Crear modelos de Usuario, Proyecto, Asignación
- Implementar migraciones

### Sprint 2: Autenticación
- Sistema de login/registro con Flask-Login
- Roles y permisos
- Formularios con WTForms

### Sprint 3: CRUD Proyectos
- Crear, editar, eliminar proyectos
- Asignar desarrolladores core y bench
- Validaciones y manejo de errores

### Sprint 4: Calendario y solicitudes
- Sistema de solicitudes de bench
- Calendario de asignaciones
- Notificaciones

## Contribuir

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -m 'Agrega nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request

## Licencia

MIT License - ver archivo LICENSE para más detalles.