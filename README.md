##Objectif de l'exercice :

▸ Installer et configurer DVC dans un projet.
▸ Versionner un jeu de données.
▸ Suivre les modifications des données et gérer les versions.
▸ Suivre et gérer les modèles et les résultats d’entraînement.

##Partie 1 : Installation et configuration de DVC

1. Créez un répertoire pour votre projet et initialisez Git dans ce répertoire (assurez-vous que Git est
installé sur votre machine).

2. Installez DVC sur votre machine et initialisez le dans votre projet.
  
3. Ajoutez les fichiers DVC créés et commitez-les dans Git.
  
##Partie 2 : Versionner un jeu de données
1. Téléchargez un dataset de votre choix et placez-le dans le répertoire du projet.
2. Utilisez DVC pour suivre le fichier data.csv. Après cette étape, un fichier data.csv.dvc qui
versionne les métadonnées du fichier de données doit être créer.
3. Ajoutez les fichiers générés par DVC dans Git et commitez-les.
4. Configurez un stockage distant pour sauvegarder vos données. Par exemple, vous pouvez utiliser
un stockage local pour cet exercice. Puis, poussez les données versionnées vers ce stockage.

##Partie 3 : Suivi d'un modèle et des résultats

1. Créez un script Python pour entraîner un modèle sur les données et sauvegardez le modèle
entraîné sous le nom model.joblib.
2. Utilisez DVC pour suivre le modèle entraîné.
3. Créez un pipeline DVC pour suivre l'ensemble du processus de transformation des données et
d'entraînement du modèle.
4. Ajoutez les fichiers model.joblib.dvc et dvc.yaml dans Git et commitez-les.

##Partie 4 : Gérer les versions des données et modèles
1. Modifiez ou remplacez les données dans data.csv et ré-exécutez l'entraînement du modèle en
utilisant DVC.
2. Consultez les différentes versions des données et des modèles via Git et DVC.
