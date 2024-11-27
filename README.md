# EDA-SAM

## Trabajo práctico Final

integrantes: Santiago Darnes, Gonzalo Jara

Este repositorio contiene una API RESTful diseñada para modelar el comportamiento del SIU guaraní universitario. La API permite gestionar usuarios, cursos, asignaturas, inscripciones y calificaciones, entre otros aspectos clave de la gestión académica.

## Características principales

- **Gestión de usuarios**: Permite crear y administrar cuentas para estudiantes, docentes y personal administrativo.
- **Gestión de cursos y asignaturas**: Crea y organiza cursos, inscribe estudiantes y asigna docentes.
- **Evaluación**: Permite registrar calificaciones y otros tipos de evaluaciones.
- **Mensajería interna**: Permite la comunicación entre estudiantes y docentes a través de un sistema de mensajes.

## Endpoints principales


### 1. **Inicio de sesión**
- **POST /login**: Iniciar sesión.
- **GET /login/logout**: Cerrar la sesión.

### 2. **Página principal**
- **POST /home/student**: Mira las ultimas noticias y accede a datos o reportes como estudiante.
- **GET /api/cursos**: Obtener la lista de cursos disponibles.
- **GET /api/cursos/{id}**: Obtener información detallada de un curso.

### 3. **Inscripciones**
- **POST /api/inscripciones**: Inscribir a un estudiante en un curso.
  - **Cuerpo**:
    ```json
    {
      "usuario_id": 1,
      "curso_id": 5
    }
    ```
- **GET /api/inscripciones**: Obtener las inscripciones de un usuario o de un curso.

### 5. **Calificaciones**
- **POST /api/calificaciones**: Revisa tus calificaciones en todas las materias.
- **GET /api/calificaciones**: Obtener las calificaciones de un estudiante o curso.

## Instalación

### Requisitos

- **Node.js** (versión >= 14.0.0)
- **Base de datos**: La API se conecta a una base de datos PostgreSQL (o la que se indique en la configuración).

### Pasos para la instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu-usuario/campus-virtual-api.git
   cd campus-virtual-api
   ```

2. Instala las dependencias:
   ```bash
   npm install
   ```

3. Configura la base de datos:
   - Crea una base de datos en tu sistema de gestión de bases de datos (PostgreSQL, MySQL, etc.).
   - Modifica el archivo `config/db.js` con las credenciales de tu base de datos.

4. Ejecuta las migraciones para crear las tablas en la base de datos:
   ```bash
   npm run migrate
   ```

5. Inicia la API:
   ```bash
   npm start
   ```

La API estará disponible en `http://localhost:3000` (puedes cambiar el puerto según sea necesario en la configuración).

## Autenticación

La API utiliza autenticación basada en tokens JWT (JSON Web Token). Para obtener un token de acceso, utiliza el endpoint:

- **POST /api/login**: Iniciar sesión con el correo electrónico y contraseña del usuario.

Ejemplo de solicitud:

```json
{
  "email": "juan.perez@universidad.com",
  "password": "tu-contraseña-segura"
}
```

La respuesta incluirá un token JWT que debes incluir en las cabeceras de las solicitudes siguientes:

```bash
Authorization: Bearer {tu-token}
```

## Tecnologías utilizadas

- **Node.js**: Entorno de ejecución de JavaScript del lado del servidor.
- **Express**: Framework web para Node.js.
- **Sequelize**: ORM para interactuar con la base de datos.
- **JWT**: JSON Web Token para la autenticación.
- **PostgreSQL**: Sistema de gestión de bases de datos relacional (puede adaptarse a otros SGBD).

## Contribuciones

Las contribuciones son bienvenidas. Si deseas contribuir, por favor sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b nueva-funcionalidad`).
3. Realiza tus cambios y haz commit (`git commit -am 'Añadir nueva funcionalidad'`).
4. Haz push a la rama (`git push origin nueva-funcionalidad`).
5. Abre un Pull Request describiendo los cambios realizados.

## Licencia

Este proyecto está bajo la Licencia MIT - consulta el archivo [LICENSE](LICENSE) para más detalles.

---

Este es un ejemplo básico, y puedes añadir o modificar la información según los requerimientos específicos de tu API y cómo está estructurada.