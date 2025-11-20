# Imagen base de Python
FROM --platform=linux/amd64 python:3.11-slim
#FROM python:3.11-slim


# Crear directorio de trabajo
WORKDIR /app

# Instalar dependencias del sistema necesarias
RUN apt-get update && apt-get install -y build-essential

# Copiar requirements y script
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copiar todo lo demás
COPY . .

# Comando por defecto
CMD ["python", "train_pre.py"]
