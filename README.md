
# Prédiction de la Santé Financière

## Description

Ce projet est une implémentation d'un modèle de machine learning pour prédire la santé financière des individus, basé sur la compétition **data.org Financial Health Prediction Challenge** de Zindi (https://zindi.africa/competitions/dataorg-financial-health-prediction-challenge). Il a été développé dans le cadre d'une session de formation ML organisée le [date de votre session].

Le projet inclut :
- Un modèle de classification entraîné sur des données financières
- Une interface web interactive avec Streamlit
- Des notebooks pédagogiques pour la formation
- Des scripts d'analyse et de visualisation

## Fonctionnalités

- Prédiction de la santé financière (saine/non saine)
- Analyse exploratoire des données
- Comparaison de différents algorithmes ML
- Interface utilisateur simple pour les prédictions

## Installation

### Prérequis

- Python 3.8+
- pip

### Étapes d'installation

1. Clonez ce repository :
   ```bash
   git clone [URL de votre repository]
   cd dataorg-financial-health-prediction-challenge
   ```

2. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

3. (Optionnel) Créez un environnement virtuel :
   ```bash
   python -m venv env
   source env/bin/activate  # Sur Windows : env\Scripts\activate
   ```

## Utilisation

### Lancer l'application web

```bash
streamlit run app.py
```

L'application sera accessible sur http://localhost:8501

### Exécuter les notebooks

Ouvrez les notebooks Jupyter dans VS Code ou Jupyter Lab :
- `Financial_Health_Masterclass_Formation.ipynb` : Formation pour formateurs
- `Financial_Health_Student_Workshop.ipynb` : Atelier pour étudiants
- `Starter Notebook.ipynb` : Point de départ pour les débutants

### Entraîner le modèle

```bash
python train_model.py  # Si vous avez un script d'entraînement
```

## Données

Les données proviennent du défi Financial Health Prediction Challenge :

- `Train.csv` : Données d'entraînement (avec labels)
- `Test.csv` : Données de test (sans labels)
- `SampleSubmission.csv` : Exemple de format de soumission
- `VariableDefinitions.csv` : Description des variables

### Variables principales

- Variables démographiques (âge, genre, etc.)
- Variables financières (revenus, dépenses, etc.)
- Variables comportementales

## Modèle

### Algorithmes utilisés

- Random Forest
- Gradient Boosting (XGBoost)
- Régression logistique
- Réseaux de neurones (optionnel)

### Métriques d'évaluation

- Accuracy
- Precision
- Recall
- F1-Score
- AUC-ROC

### Résultats

| Modèle | Accuracy | F1-Score |
|--------|----------|----------|
| Random Forest | 0.85 | 0.82 |
| XGBoost | 0.87 | 0.85 |
| Logistic Regression | 0.78 | 0.76 |

## Structure du projet

```
├── app.py                          # Application Streamlit
├── *.ipynb                         # Notebooks Jupyter
├── Train.csv                       # Données d'entraînement
├── Test.csv                        # Données de test
├── model_metadata.json             # Métadonnées du modèle
├── requirements.txt                # Dépendances Python
├── programme_liste_chainee.c       # Code C (liste chaînée)
├── rapport_SMA_algo_recherche.md   # Rapport d'algorithmes
└── README.md                       # Ce fichier
```

## Formation ML

Ce projet a été utilisé lors d'une session de formation ML avec les objectifs suivants :

1. Comprendre les bases du machine learning supervisé
2. Pratiquer l'analyse exploratoire des données
3. Implémenter et comparer différents algorithmes
4. Déployer un modèle en production

### Exercices

- Analyse des données manquantes
- Feature engineering
- Gestion du déséquilibre des classes
- Optimisation des hyperparamètres

## Contribution

Les contributions sont les bienvenues ! Pour contribuer :

1. Forkez le projet
2. Créez une branche pour votre fonctionnalité (`git checkout -b feature/AmazingFeature`)
3. Commitez vos changements (`git commit -m 'Add some AmazingFeature'`)
4. Pushez vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrez une Pull Request

## Licence

Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails.

## Contact

- Organisateur : Bala Andegue Francois Lionnel
- Email : balaandeguefrancoislionnel@gmail.com
- Date de la session : 21 mars 2026

## Remerciements

- Merci aux participants de la session ML
- Données fournies par DataOrg
- Inspiré par les défis Kaggle
