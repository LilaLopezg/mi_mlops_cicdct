#!/bin/bash
# Script para construir la imagen Docker del predictor

set -e

echo "🏗️  Construyendo imagen Docker del predictor consumo de alcohol..."

# Construir desde la raíz del proyecto para acceder a la carpeta models
cd "$(dirname "$0")/.."

# Verificar que existe el modelo
if [ ! -f "models/consumo_model_smoteenn_latest.pkl" ]; then
    echo "❌ Error: No se encontró el modelo consumo_model_smoteenn_latest.pkl en la carpeta models/"
    echo "   Ejecuta primero el entrenamiento: cd training && python train_pre.py"
    exit 1
fi
#!/bin/bash

set -e

echo "🐳 Construyendo imagen Docker para el predictor..."
docker build -t consumo-training :latest .

echo "✅ Imagen construida exitosamente: consumo-predictor:latest"
mkdir -p predictor/models && cp models/consumo_model_smoteenn_latest.pklpredictor/models/

# Construir imagen
docker build -f predictor/Dockerfile -t consumo-training :latest .

echo "✅ Imagen construida exitosamente: consumo-training:latest"
echo ""
echo "Para ejecutar el contenedor:"
echo "  predictor/run_predictor.sh"
echo ""
echo "Para hacer predicciones personalizadas:"
echo "  docker run --rm consumo-training:latest python predict_api.py --sepal_length 6.0 --sepal_width 3.0 --petal_length 4.5 --petal_width 1.5"