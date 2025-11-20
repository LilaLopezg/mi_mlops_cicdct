#!/usr/bin/env python3
"""
Script para hacer predicciones usando el modelo de consumo de alcohol entrenado.
Ejemplo de uso:
    python predict_consumo.py --age 20 --gender 1 --parent_alcohol 0 --academic_semester 3
"""

import pickle
import numpy as np
import os
import argparse


def load_model(model_path="models/consumo_model_smoteenn_latest.pkl"):
    """Carga el modelo entrenado desde el archivo pickle"""
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"No se encontró el modelo en: {model_path}")
    
    with open(model_path, "rb") as f:
        model_data = pickle.load(f)
    
    return model_data


def predict_consumo(features, model_path="models/consumo_model_smoteenn_latest.pkl"):
    """
    Realiza una predicción del nivel o riesgo de consumo de alcohol.
    
    Args:
        features (list[float]): Lista de valores de entrada para las variables seleccionadas.
        model_path (str): Ruta al modelo entrenado.
    
    Returns:
        dict: Resultado con predicción y probabilidad.
    """
    model_data = load_model(model_path)
    model = model_data["model"]
    scaler = model_data["scaler"]
    target_names = model_data.get("target_names", ["No consumo", "Consumo"])

    # Convertir y escalar entrada
    X = np.array([features])
    X_scaled = scaler.transform(X)

    # Predicción
    pred = model.predict(X_scaled)[0]
    probs = model.predict_proba(X_scaled)[0]

    return {
        "input_features": features,
        "prediction": target_names[pred],
        "prediction_index": int(pred),
        "probabilities": {
            target_names[i]: float(p) for i, p in enumerate(probs)
        },
        "confidence": float(max(probs))
    }


def main():
    """Ejecuta la predicción desde la línea de comandos"""
    parser = argparse.ArgumentParser(description="Predicción de consumo de alcohol")
    parser.add_argument("--age", type=float, required=True, help="Edad del estudiante")
    parser.add_argument("--gender", type=int, required=True, help="Género (0=femenino, 1=masculino)")
    parser.add_argument("--parent_alcohol", type=int, required=True, help="Padres con historial de alcoholismo (0/1)")
    parser.add_argument("--academic_semester", type=int, required=True, help="Semestre académico actual")
    parser.add_argument("--model_path", type=str, default="models/consumo_model_smoteenn_latest.pkl", help="Ruta al modelo")

    args = parser.parse_args()

    features = [args.age, args.gender, args.parent_alcohol, args.academic_semester]

    try:
        result = predict_consumo(features, args.model_path)
        
        print("=" * 60)
        print("🔍 PREDICCIÓN DE CONSUMO DE ALCOHOL")
        print("=" * 60)
        print(f"Entrada: {result['input_features']}")
        print(f"Predicción: {result['prediction']}")
        print(f"Confianza: {result['confidence']:.4f}")
        print("Probabilidades:")
        for k, v in result["probabilities"].items():
            print(f"  {k}: {v:.4f}")
        print("=" * 60)

    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    main()
