# Usar una imagen oficial de Python como imagen base
FROM python:3.8-slim

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar los archivos requeridos para instalar las dependencias
COPY requirements.txt ./

# Instalar cualquier dependencia necesaria
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código de la aplicación Flask en el contenedor
COPY . .

# Exponer el puerto que utiliza Flask
EXPOSE 5000

# Comando para correr la aplicación
CMD ["python", "./codebreaker.py"]
