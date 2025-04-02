# /API/Docker/Dockerfile

# Recordemos crear la Imagen: docker build -t <nombreImagen> .
# Ejecutar el contenedor: docker run -p <puerto_host>:<puerto_docker> <nombreImagen>

# Usa una imagen base oficial de Python.
# En este caso, se usa la versión 3.13 con la variante slim-bookworm
# La variante "slim" es más pequeña, lo que resulta en una imagen final más ligera.
# bookworm es el nombre de una distribución de Debian, lo que proporciona un sistema base estable.
FROM python:3.13-slim-bookworm

# Establece el directorio de trabajo dentro del contenedor.
# Todos los comandos subsiguientes se ejecutarán en este directorio.
WORKDIR /app

# Copia el archivo requisitos.txt al contenedor.
# requisitos.txt contiene la lista de dependencias de Python que se necesitan.
# Se copia antes que el resto del código para aprovechar el caché de Docker.
# Si requisitos.txt no cambia, las capas de instalación de dependencias se reutilizarán, acelerando la construcción.
COPY ./requisitos.txt /app/

# Instala las dependencias de Python especificadas en requisitos.txt.
# --no-cache-dir le dice a pip que no use un caché local, lo que reduce el tamaño de la imagen.
RUN pip install --no-cache-dir -r requisitos.txt

# Copia el resto del código de la aplicación al contenedor.
# Esto incluye app.py y cualquier otro archivo o directorio en ./Python
COPY ./apisPy /app/

# Expone el puerto 8000.
# Esto indica que el contenedor escuchará en el puerto 8000.
# No publica el puerto automáticamente; para hacerlo, se debe usar -p al ejecutar el contenedor.
EXPOSE 8000

# Define el comando para ejecutar la aplicación cuando se inicie el contenedor.
# En este caso, se usa Gunicorn como servidor WSGI para ejecutar la aplicación Flask.
#  - "gunicorn": El comando para ejecutar Gunicorn.
#  - "--workers 1": Especifica el número de procesos worker que Gunicorn usará para manejar solicitudes.
#                   Ajusta este número según las necesidades de la aplicación y los recursos del servidor.
#  - "--bind 0.0.0.0:8000": Le dice a Gunicorn que escuche en todas las interfaces de red (0.0.0.0) en el puerto 8000.
#  - "app:app": Especifica el módulo y la aplicación Flask que Gunicorn debe ejecutar.
#              El primer "app" se refiere al nombre del archivo Python (app.py),
#              y el segundo "app" se refiere a la instancia de la aplicación Flask dentro de ese archivo.
CMD ["gunicorn", "--workers", "1", "--bind", "0.0.0.0:8000", "apiPrueba:app"]
