# Usar una imagen base oficial de Python
FROM python:3.9-slim

# Establecer el directorio de trabajo en la imagen
WORKDIR /app

# Copiar el archivo de requisitos y instalar las dependencias
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copiar el resto de la aplicación
COPY . .

# Establecer la variable de entorno para Flask
ENV FLASK_APP=app.py

# Exponer el puerto que Flask usará
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["flask", "run", "--host=0.0.0.0"]
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
