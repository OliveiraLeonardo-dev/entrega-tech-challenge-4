from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import tensorflow as tf
import joblib
import numpy as np

app = FastAPI(title="API de Previsão ITUB4 - Tech Challenge")

# Carregar os artefatos treinados no SageMaker
model = tf.keras.models.load_model('app/modelo_lstm_itub4.keras')
scaler = joblib.load('app/scaler_itub4.pkl')

class DadosEntrada(BaseModel):
    ultimos_60_dias: list 

@app.get("/")
def home():
    return {"status": "API Online", "modelo": "LSTM ITUB4"}

@app.post("/predict")
def predict(data: DadosEntrada):
    if len(data.ultimos_60_dias) != 60:
        raise HTTPException(status_code=400, detail="É necessário enviar exatamente 60 preços.")
    
    try:
        
        entrada = np.array(data.ultimos_60_dias).reshape(-1, 1)
        entrada_scaled = scaler.transform(entrada)
        
        X_input = np.reshape(entrada_scaled, (1, 60, 1))
        
        
        pred = model.predict(X_input)
        
        preco_final = scaler.inverse_transform(pred)
        
        return {
            "previsao_proximo_dia": float(round(preco_final[0][0], 2)),
            "unidade": "BRL"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))