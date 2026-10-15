# TP1 MLOps : Prédiction du churn

**Auteur :** Arwa El hadj Mbarek (GitHub : arwa774)
**Module :** MLOps, Polytech Sousse

## Description

Premier modèle de Machine Learning du projet fil rouge : prédire si un client quitte l'entreprise (churn) à partir de 500 clients fictifs. Ce TP est volontairement une version de départ, sans outils MLOps (ni Git avancé, ni MLflow), afin de comprendre leurs limites.

## Contenu du dépôt

| Fichier | Rôle |
|---|---|
| `generate_data.py` | Génère le dataset fictif de 500 clients |
| `churn_data.csv` | Dataset généré (features + target `churn`) |
| `churn_model.ipynb` | Notebook : exploration, préparation, entraînement, évaluation, 3 essais |
| `model.pkl` | Modèle sauvegardé (contient l'Essai 3) |
| `.gitignore` | Exclut `venv/` et les fichiers temporaires |

## Données

- **Features :** `age`, `salaire`, `abonnement`, `anciennete`, `consommation`
- **Target :** `churn` (0 = le client reste, 1 = le client part)
- **Règle de génération :** churn = 1 si `consommation < 30` et `anciennete < 2`
- **Seed :** `np.random.seed(42)` pour la reproductibilité

## Installation

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install pandas numpy scikit-learn jupyter joblib
```

## Utilisation

1. Générer les données :
```powershell
   python generate_data.py
```
2. Ouvrir `churn_model.ipynb` dans VS Code, sélectionner le kernel du `venv`, puis exécuter les cellules dans l'ordre.

## Modèle

- Algorithme : `RandomForestClassifier`
- Split : 80 % entraînement (400 clients) / 20 % test (100 clients)
- Métriques : accuracy et classification report

| Essai | Configuration | Accuracy |
|---|---|---|
| 1 | 100 arbres, profondeur 5, 5 features | à compléter |
| 2 | 50 arbres, profondeur 3, 5 features | à compléter |
| 3 | 100 arbres, profondeur 5, sans `salaire` | à compléter |

## Limites observées (pourquoi le MLOps)

- **Data leakage :** la règle de génération du churn utilise directement `consommation` et `anciennete`, donc l'accuracy est très élevée voire égale à 1.0.
- **Modèle écrasé :** `model.pkl` est écrasé à chaque essai, il est impossible de retrouver l'Essai 1.
- **Pas de traçabilité :** aucun historique des paramètres ni des performances entre les essais.
- **Reproductibilité non garantie :** résultats potentiellement différents selon la machine et les versions des bibliothèques.

