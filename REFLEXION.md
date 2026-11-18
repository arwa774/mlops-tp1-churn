## TP3 : MLflow

1. Quel est le meilleur modèle ? Je peux le prouver : MLflow trie les runs par f1
   et les résultats sont conservés avec leur date. Essai-1 et essai-3 sont à
   égalité (f1 = 0.889), essai-2 est plus faible (f1 = 0.333).
2. Peut-on redonner exactement le modèle de l'Essai 1 ? Oui, avec
   mlflow.sklearn.load_model("runs:/<id>/model"), grâce à l'identifiant du run.
3. Un camarade peut-il reproduire mon travail ? En partie : le code, les
   paramètres et les versions sont connus, mais pas l'environnement identique.
   Docker résoudra ce problème.

## TP4 : Registry et API

1. Comment désigner officiellement le modèle à utiliser ? Avec l'alias champion :
   models:/churn-model@champion pointe vers la version choisie, et on peut le
   déplacer en une ligne.
2. Comment une application peut-elle utiliser le modèle ? Par une requête web à
   l'API : POST /predict avec un JSON, la réponse contient la prédiction.
3. Que se passe-t-il quand on change de champion ? On déplace l'alias et on
   redémarre l'API : le code de l'API et des applications clientes ne change pas.