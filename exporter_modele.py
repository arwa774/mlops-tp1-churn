import mlflow
import mlflow.sklearn

# Se connecter à la base du Registry (celle du TP4)
mlflow.set_tracking_uri("sqlite:///mlflow.db")

# Charger le champion depuis le Registry
model = mlflow.sklearn.load_model("models:/churn-model@champion")

# L'écrire dans un dossier ordinaire « model » (sera copié dans l'image)
mlflow.sklearn.save_model(model, "model", serialization_format="cloudpickle")
print("Champion exporté dans le dossier model/")