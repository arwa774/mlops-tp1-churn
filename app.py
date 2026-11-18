# ===== 1. Importer les bibliothèques =====
import os                          # lire les variables d'environnement
from typing import Literal         # pour limiter les valeurs possibles d'un champ
import mlflow                      # charger le modèle (Registry ou dossier)
import mlflow.sklearn
import pandas as pd                # fabriquer le tableau attendu par le modèle
from fastapi import FastAPI        # le cadre de travail de l'API
from pydantic import BaseModel     # décrire et valider les données reçues

# ===== 2. Créer l'application =====
app = FastAPI(title="API Churn")

# ===== 3. Lire la configuration dans les variables d'environnement =====
# os.getenv("NOM", "valeur") : valeur de la variable, ou valeur par défaut
TRACKING_URI = os.getenv("MLFLOW_TRACKING_URI", "sqlite:///mlflow.db")
MODEL_URI = os.getenv("MODEL_URI", "models:/churn-model@champion")

# ===== 4. Charger le champion UNE SEULE FOIS, au démarrage =====
mlflow.set_tracking_uri(TRACKING_URI)
model = mlflow.sklearn.load_model(MODEL_URI)
print(f"Modèle chargé depuis : {MODEL_URI}")

# ===== 5. Décrire les données attendues =====
class Client(BaseModel):
    age: int
    salaire: float
    abonnement: Literal["Basique", "Standard", "Premium"]
    anciennete: float
    consommation: float

# ===== 6. Route /health =====
@app.get("/health")
def health():
    return {"status": "ok"}

# ===== 7. Route /predict =====
@app.post("/predict")
def predict(client: Client):
    # a) transformer le client reçu en tableau d'une ligne
    ligne = pd.DataFrame([client.model_dump()])
    # b) transformer « abonnement » en colonnes 0/1, comme à l'entraînement
    ligne = pd.get_dummies(ligne)
    # c) garder les colonnes du modèle, dans le bon ordre ; les absentes valent 0
    ligne = ligne.reindex(columns=model.feature_names_in_, fill_value=0)
    # d) prédire : 1 = part, 0 = reste
    resultat = int(model.predict(ligne)[0])
    return {"churn": resultat,
            "message": "Le client va partir" if resultat == 1 else "Le client reste"}