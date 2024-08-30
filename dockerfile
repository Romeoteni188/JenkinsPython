# Usa una imagen base de Python
FROM python:3.11-slim

# Instala las dependencias necesarias
RUN apt-get update && \
    apt-get install -y \
    python3-tk \
    && rm -rf /var/lib/apt/lists/*

# Copia el archivo de requerimientos y el código fuente al contenedor
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r /app/requirements.txt
RUN pip install --upgrade pip

COPY . /app/
WORKDIR /app

# Exponer el puerto en el que la aplicación se ejecutará
EXPOSE 8080

# Comando para ejecutar la aplicación
CMD ["python", "libro.py"]
