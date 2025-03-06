# 4thewords_backend_jean_rangel

Este repositorio almacena el código backend de la prueba para desarrollador fullstack de 4thewords.

## Descripción General

Este proyecto representa la parte backend de la aplicación 4thewords, encargada de gestionar la lógica de negocio y la comunicación con la base de datos. Está desarrollado en Python, utilizando el framework FastAPI para la creación de APIs rápidas y eficientes.

## Estructura del Proyecto

La estructura principal del proyecto es la siguiente:

- **`main.py`**: Archivo principal que inicia la aplicación FastAPI.
- **`create_database.sql`**: Script SQL para la creación de la base de datos.
- **`README.md`**: Documentación del proyecto.

## Requisitos Previos

Antes de comenzar, asegúrate de tener instaladas las siguientes herramientas:

- [Python 3.8+](https://www.python.org/)
- [Git](https://git-scm.com/)
- [SQLite](https://www.sqlite.org/) (o cualquier otro sistema de gestión de bases de datos que prefieras)

## Instrucciones de Instalación

Sigue estos pasos para configurar el proyecto en tu máquina local:

1. **Clona el repositorio:**

   ```bash
   git clone https://github.com/MikeOnBoard/4thewords_backend_jean_rangel.git
   ```

2. **Navega al directorio del proyecto:**

   ```bash
   cd 4thewords_backend_jean_rangel
   ```

3. **Crea y activa un entorno virtual:**

   En Windows:

   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

   En macOS/Linux:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

4. **Instala las dependencias:**

   ```bash
   pip install -r requirements.txt
   ```

5. **Configura la base de datos:**

   Ejecuta el script `create_database.sql` en tu sistema de gestión de bases de datos para crear las tablas necesarias.

## Ejecución del Proyecto

Para ejecutar la aplicación en un entorno de desarrollo:

```bash
uvicorn main:app --reload
```

Esto iniciará el servidor de desarrollo y podrás acceder a la API en `http://127.0.0.1:8000`.

## Pruebas

Actualmente, no hay pruebas automatizadas configuradas para este proyecto.

## Contribución

Si deseas contribuir a este proyecto, por favor sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz commit (`git commit -m 'Añadir nueva funcionalidad'`).
4. Sube tus cambios (`git push origin feature/nueva-funcionalidad`).
5. Abre un Pull Request.

## Licencia

Este proyecto no especifica una licencia.

## Contacto o Créditos

Desarrollado por Jean Rangel. Puedes encontrar más información en su perfil de GitHub: [jerangel1](https://github.com/jerangel1).
