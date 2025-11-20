# Usar imagen base de Python 3.13
FROM python:3.13-slim

# Establecer variables de entorno
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Crear directorio de trabajo
WORKDIR /app

# Crear directorio para los modelos
RUN mkdir -p models

# Copiar archivo de requirements
COPY requirements.txt .

# Instalar dependencias del sistema necesarias para scikit-learn
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Instalar dependencias de Python
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copiar scripts de entrenamiento
COPY train.py .

# Comando por defecto: ejecutar el entrenamiento
CMD ["python", "train_pre.py"]
