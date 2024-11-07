# train_model.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib

# Charger les données
data = pd.read_csv("C:\\Users\\hajer\\Desktop\\IDS5\\mlops\\tp3\\projet_dvc\\data.csv")

# Préparer les données
X = data.drop("Species", axis=1)  # Remplacez "species" par la colonne cible dans votre dataset Iris
y = data["Species"]

# Diviser les données en ensemble d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entraîner le modèle de régression logistique
model = LogisticRegression(max_iter=200)  # max_iter augmenté pour assurer la convergence
model.fit(X_train, y_train)

# Évaluer le modèle
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Précision du modèle : {accuracy * 100:.2f}%")

# Sauvegarder le modèle entraîné
joblib.dump(model, "model.joblib")
print("Modèle entraîné et sauvegardé sous 'model.joblib'")
