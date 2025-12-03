import pandas as pd
import joblib
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# 1. Cargar el Modelo Entrenado
model_filename = "bank_pipeline.pkl"

try:
    # Cargamos el "cerebro" matemático
    model = joblib.load(model_filename)
    print(f"--> ¡ÉXITO! Modelo '{model_filename}' cargado correctamente.")
except FileNotFoundError:
    print(f"--> ERROR CRÍTICO: No encuentro el archivo '{model_filename}'.")
    print("    Asegúrate de que el archivo .pkl esté en la misma carpeta que app.py")

# 2. Inicializar la Aplicación API
app = FastAPI(title="Bank Marketing Prediction API", version="1.0")


# 3. Definir el Dominio de Datos (Validation)
# Esto actúa como un "filtro" estricto. Si envían texto en la edad, la API da error antes de molestar al modelo.
class ClientData(BaseModel):
    age: int
    duration: int
    campaign: int
    pdays: int
    previous: int
    job: str
    marital: str
    education: str
    default: str
    housing: str
    loan: str
    contact: str
    month: str
    day_of_week: str
    poutcome: str


# 4. El Endpoint (La función que se ejecutará al llamar a la API)
@app.post("/predict")
def predict(data: ClientData):
    try:
        # Convertimos el objeto recibido a un DataFrame (formato matriz)
        # data.dict() convierte el input en un diccionario de Python
        input_df = pd.DataFrame([data.dict()])

        # Hacemos la predicción
        # [0] es porque predict devuelve un array, y queremos el primer elemento
        prediction = model.predict(input_df)[0]

        # Probabilidad (Opcional, pero muy útil para Risk Scoring)
        probability = model.predict_proba(input_df)[0].tolist()

        return {
            "prediccion_clase": int(prediction),
            "resultado_texto": "SUSCRIBE" if prediction == 1 else "NO SUSCRIBE",
            "probabilidad_confianza": probability
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 5. Endpoint de prueba (Health Check)
@app.get("/")
def home():
    return {"mensaje": "La API de Inteligencia Artificial está ONLINE"}