# EDU-SAM

## Trabajo práctico Final

Integrantes: Santiago Darnes, Gonzalo Jara

Este repositorio contiene una API RESTful diseñada para modelar el comportamiento del SIU Guaraní universitario. La API permite gestionar usuarios, cursos, asignaturas, inscripciones y calificaciones, entre otros aspectos clave de la gestión académica.

## Características principales

- **Gestión de usuarios**: Permite crear y administrar cuentas para estudiantes, docentes y personal administrativo.
- **Gestión de cursos y asignaturas**: Crea y organiza cursos, inscribe estudiantes y asigna docentes.
- **Evaluación**: Permite registrar calificaciones y otros tipos de evaluaciones.

## Endpoints principales

### 1. **Inicio de sesión**
- **POST /login**: Iniciar sesión.
- **GET /login/logout**: Cerrar la sesión.

### 2. **Página principal**
- **POST /home/student**: Recupera las últimas noticias y permite al estudiante acceder a sus datos o reportes personalizados.
  
### 3. **Gestión de asignaturas y cursos**
- **POST /subject_registration/**: Permite a un estudiante registrarse en una asignatura.
- **GET /subject_registration/**: Obtiene la lista de asignaturas en las que un estudiante está registrado.
- **POST /exam_registration/**: Permite registrar un estudiante en un examen asociado a una asignatura.
- **GET /exam_registration/**: Muestra los exámenes registrados para un estudiante.

### 4. **Reportes**
- **GET /reports**: Permite generar y acceder a los reportes académicos de un estudiante. Los reportes pueden incluir calificaciones y otros datos relevantes de las asignaturas.

### 5. **Trámites**
- **GET /procedures**: Proporciona una lista de trámites administrativos o académicos disponibles para el usuario.

### 6. **Datos personales del estudiante**
- **GET /personal_data/student**: Obtiene la información personal de un estudiante, como nombre, dirección, contacto y otros datos relevantes para el sistema académico.


## Instalación

### Requisitos

- **Python**: (versión >= 3.7).
- **Flask**: Framework web para Python.
- **Base de datos**: La API se conecta a una base de datos PostgreSQL alojada en *NeonTech*.

### Pasos para la instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/SantiagoDarnes/edu-sam
   cd edu-sam
   ```

2. Crea un entorno virtual (opcional pero recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Para Linux/Mac
   venv\Scripts\activate  # Para Windows
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Configura la base de datos:
   - Crea una base de datos en **NeonTech** o tu proveedor de base de datos PostgreSQL.
   - Modifica el archivo de configuración `config.py` con las credenciales de tu base de datos.

5. Ejecuta las migraciones para crear las tablas en la base de datos:
   ```bash
   flask db upgrade
   ```

6. Inicia la API:
   ```bash
   flask run
   ```

La API estará disponible en `http://localhost:5000` (puedes cambiar el puerto según sea necesario en la configuración).


## Tecnologías utilizadas

- **Python**: Lenguaje de programación utilizado para desarrollar la API.
- **Flask**: Framework web ligero para Python.
- **SQLAlchemy**: ORM utilizado para interactuar con la base de datos PostgreSQL.
- **PostgreSQL (NeonTech)**: Sistema de gestión de bases de datos relacional.


## Licencia

Este proyecto está bajo la Licencia MIT - consulta el archivo [LICENSE](LICENSE) para más detalles.
