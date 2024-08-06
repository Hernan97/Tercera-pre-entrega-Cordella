# Proyecto de Gestión de Estudiantes, Profesores y Cursos

Este proyecto es una aplicación web que permite gestionar información sobre estudiantes, profesores y cursos. A continuación se describe cómo configurar y probar el proyecto.

## Estructura del Proyecto

1. **Base de Datos**: 
   - **Descripción**: Base de datos que contiene tablas para Estudiantes, Profesores y Cursos.
   - **Archivos**: `database.sql` (o el archivo SQL que utilices para importar la base de datos).

2. **Archivos HTML**:
   - **Descripción**: Archivos HTML para la interfaz de usuario.
   - **Archivos**:
     - `estudiantes.html`
     - `profesores.html`
     - `cursos.html`

## Configuración Inicial

1. **Importar la Base de Datos**:
   - Importa el archivo SQL en tu sistema de gestión de bases de datos (MySQL, PostgreSQL, SQLite, etc.).
   - Asegúrate de que las tablas `Estudiantes`, `Profesores` y `Cursos` estén correctamente creadas y pobladas con datos de ejemplo si es necesario.

2. **Configurar el Servidor Web**:
   - Si estás usando un servidor web local como XAMPP, WAMP o MAMP, coloca los archivos HTML en el directorio correspondiente (por ejemplo, `htdocs` en XAMPP).

## Pruebas y Funcionalidades

### 1. Página de Estudiantes

- **Archivo**: `estudiantes.html`
- **Funcionalidad**: Muestra una lista de estudiantes. Puedes realizar operaciones como agregar, editar o eliminar estudiantes (dependiendo de la implementación).
- **Instrucciones**: No esta en funcionamiento actualmente. 
  1. Abre `estudiantes.html` en tu navegador.
  2. Verifica que se muestre la lista de estudiantes importados desde la base de datos.
  3. Prueba las funcionalidades disponibles (si están implementadas).

### 2. Página de Profesores

- **Archivo**: `profesores.html`
- **Funcionalidad**: Muestra una lista de profesores. Permite realizar operaciones relacionadas con profesores.
- **Instrucciones**:
  1. Abre `profesores.html` en tu navegador.
  2. Verifica que se muestre la lista de profesores importados desde la base de datos.
  3. Prueba las funcionalidades disponibles (si están implementadas).

### 3. Página de Cursos

- **Archivo**: `cursos.html`
- **Funcionalidad**: Muestra una lista de cursos. Permite gestionar información relacionada con los cursos.
- **Instrucciones**:
  1. Abre `cursos.html` en tu navegador.
  2. Verifica que se muestre la lista de cursos importados desde la base de datos.
  3. Prueba las funcionalidades disponibles (si están implementadas).

### 4. Página de Precios

- **Archivo**: `precios.html`
- **Funcionalidad**: Muestra una lista de cursos. Permite visualizar los precios relacionada con los cursos.
- **Instrucciones**:
  1. Abre `precios.html` en tu navegador.
  2. Verifica que se muestre la lista de cursos importados desde la base de datos.
  3. Prueba las funcionalidades disponibles (si están implementadas).


### 5. Página de Search

- **Archivo**: `entregables.html`
- **Funcionalidad**: Muestra la base de datos de los alumnos y de los cursos que estan vigente.
- **Instrucciones**:
  1. Abre `entregables.html` en tu navegador.
  2. Verifica que se muestre la lista de cursos y estudiantes importados desde la base de datos.
  3. Prueba las funcionalidades disponibles (si están implementadas).

### 6. Página de CrearCurso

- **Archivo**: `creacurso.html`
- **Funcionalidad**:  Te permite crear un nuevo curso.
- **Instrucciones**: indicar manualmente /crearcurso, dado que no se integro ningun html directo
  1. Abre `crearcurso.html` en tu navegador.
  2. Creacion de un nuevo curso en la base de datos.
  3. Prueba las funcionalidades disponibles (si están implementadas).

### 6. Página de CreaEstudiante

- **Archivo**: `crearestudiante.html`
- **Funcionalidad**:  Te permite crear un nuevo estudiante.
- **Instrucciones**: indicar manualmente /creaestudiante, dado que no se integro ningun html directo
  1. Abre `crearestudiante.html` en tu navegador.
  2. Creacion de un nuevo estudiante en la base de datos.
  3. Prueba las funcionalidades disponibles (si están implementadas).

## Notas Adicionales

- Asegúrate de que tu servidor web esté en funcionamiento y que la base de datos esté correctamente configurada antes de probar las páginas HTML.
- Si encuentras algún problema, verifica los archivos de configuración del servidor y los scripts de conexión a la base de datos.

## Contribuciones

Si deseas contribuir a este proyecto, por favor sigue estos pasos:

1. Realiza un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza los cambios y haz commit (`git commit -am 'Añadir nueva funcionalidad'`).
4. Envía un pull request.
