# app.py
import streamlit as st
import pandas as pd
import numpy as np
import joblib
import json
import pickle

# Configuration de la page
st.set_page_config(
    page_title="Prédiction Santé Financière PME",
    page_icon="🏦",
    layout="wide"
)

# Titre
st.title("🏦 Prédiction de la Santé Financière des PME Africaines")
st.markdown("---")

# Chargement du modèle et des métadonnées
@st.cache_resource
def load_model_and_metadata():
    """Charge le modèle et les métadonnées une seule fois"""
    try:
        model = joblib.load('financial_health_model.pkl')
        
        with open('model_metadata.json', 'r') as f:
            metadata = json.load(f)
        
        with open('transformers.pkl', 'rb') as f:
            transformers = pickle.load(f)
        
        return model, metadata, transformers
    except FileNotFoundError as e:
        st.error(f"❌ Fichier introuvable : {e}")
        st.info("Veuillez d'abord exécuter le notebook pour générer les fichiers du modèle.")
        return None, None, None

model, metadata, transformers = load_model_and_metadata()

if model is None:
    st.stop()

def safe_float_convert(series):
    """Convertit une série en float de manière sécurisée"""
    try:
        # Convertir en string d'abord
        series = series.astype(str)
        # Remplacer 'nan' par NaN
        series = series.replace('nan', np.nan)
        # Convertir en float
        return pd.to_numeric(series, errors='coerce').astype(float)
    except:
        return pd.Series([np.nan] * len(series), index=series.index).astype(float)

# Fonction de preprocessing identique à celle du notebook
def preprocess_input(input_dict, metadata, transformers):
    """Applique les mêmes transformations que dans le notebook"""
    
    # Création du DataFrame avec toutes les colonnes nécessaires
    df = pd.DataFrame(columns=metadata['feature_names'])
    
    # Remplir les colonnes avec les valeurs d'entrée
    for col in metadata['feature_names']:
        if col in input_dict:
            df.loc[0, col] = input_dict[col]
        else:
            df.loc[0, col] = np.nan
    
    # Récupération des maps d'encodage
    ord_map = transformers['ord_map']
    financial_products = transformers['financial_products']
    CAT_COLS = transformers['cat_cols']
    
    # Convertir TOUTES les colonnes en string d'abord pour éviter les problèmes de type
    for col in df.columns:
        df[col] = df[col].astype(str).replace('nan', np.nan)
    
    # 1. Encodage ordinal des produits financiers
    for c in financial_products:
        col_name = c + '_num'
        if c in df.columns:
            # Appliquer le mapping
            df[col_name] = df[c].map(ord_map).fillna(-1)
    
    # 2. Feature composite : Indice d'inclusion financière
    fin_cols = [c + '_num' for c in financial_products if c + '_num' in df.columns]
    if fin_cols:
        df['fin_sum'] = df[fin_cols].clip(lower=0).sum(axis=1)
    else:
        df['fin_sum'] = 0
    
    # 3. Transformations logarithmiques - Conversion explicite en float
    for col in ['personal_income', 'business_expenses', 'business_turnover']:
        if col in df.columns:
            # Conversion en float avec gestion des erreurs
            values = pd.to_numeric(df[col], errors='coerce')
            values = values.fillna(0).astype(float)
            # Vérifier que values est bien un float
            values = values.values if hasattr(values, 'values') else values
            # Appliquer log1p
            log_values = np.log1p(np.array(values, dtype=float))
            df[f'log_{col}'] = log_values
    
    # 4. Ratio dépenses/chiffre d'affaires
    if 'business_expenses' in df.columns and 'business_turnover' in df.columns:
        expenses = pd.to_numeric(df['business_expenses'], errors='coerce').fillna(0).astype(float)
        turnover = pd.to_numeric(df['business_turnover'], errors='coerce').fillna(1).astype(float)
        # Éviter la division par zéro
        turnover = turnover.replace(0, 1)
        df['expense_ratio'] = (expenses / turnover).clip(0, 10)
    
    # 5. Âge de l'entreprise en mois
    if 'business_age_years' in df.columns:
        years = pd.to_numeric(df['business_age_years'], errors='coerce').fillna(0).astype(float)
        months = pd.to_numeric(df['business_age_months'], errors='coerce').fillna(0).astype(float)
        df['biz_age_months_total'] = years * 12 + months
    else:
        months = pd.to_numeric(df['business_age_months'], errors='coerce').fillna(0).astype(float)
        df['biz_age_months_total'] = months
    
    # 6. Encodage des colonnes catégorielles
    for col in CAT_COLS:
        if col in df.columns:
            # Convertir en codes catégoriels
            df[col] = df[col].astype(str)
            df[col] = pd.Categorical(df[col]).codes.astype(float)
            df.loc[df[col] < 0, col] = -1  # Remplacer -1 par -1 au lieu de NaN
    
    # 7. Sélectionner uniquement les features attendues par le modèle
    df_processed = df[metadata['feature_names']].copy()
    
    # 8. Remplacer toutes les valeurs restantes par -1 (pour gérer les NaN)
    for col in df_processed.columns:
        # Conversion finale en float
        df_processed[col] = pd.to_numeric(df_processed[col], errors='coerce').fillna(-1)
        # S'assurer que c'est bien un float
        df_processed[col] = df_processed[col].astype(float)
    
    return df_processed

# Informations du modèle dans la sidebar
with st.sidebar:
    st.header("ℹ️ Informations du modèle")
    st.write(f"**Type :** {metadata['model_type']}")
    st.write(f"**Date :** {metadata['training_date'].split()[0]}")
    st.write(f"**Features :** {metadata['n_features']}")
    
    st.markdown("---")
    st.header("📝 Saisie des données")

# Sidebar - Formulaire de saisie
with st.sidebar:
    # Informations générales
    st.subheader("👤 Informations générales")
    owner_age = st.number_input("Âge du propriétaire", min_value=18, max_value=100, value=35, step=1)
    business_age_months = st.number_input("Âge de l'entreprise (mois)", min_value=0, max_value=600, value=24, step=1)
    business_age_years = st.number_input("Âge de l'entreprise (années)", min_value=0, max_value=50, value=2, step=1)
    
    # Informations financières
    st.subheader("💰 Informations financières")
    personal_income = st.number_input("Revenu personnel", min_value=0, value=50000, step=1000)
    business_expenses = st.number_input("Dépenses de l'entreprise", min_value=0, value=20000, step=1000)
    business_turnover = st.number_input("Chiffre d'affaires", min_value=0, value=100000, step=1000)
    
    # Pays
    st.subheader("🌍 Localisation")
    country = st.selectbox("Pays", options=['eswatini', 'zimbabwe', 'malawi', 'kenya', 'uganda', 'tanzania', 'rwanda'])
    
    # Attitudes et perceptions
    st.subheader("📊 Attitudes")
    attitude_stable = st.selectbox("Environnement commercial stable ?", 
                                   options=['Yes', 'No', "Don’t know or N/A"])
    attitude_worried = st.selectbox("Inquiet de fermeture ?",
                                    options=['Yes', 'No', "Don’t know or N/A"])
    
    # Compliance
    compliance_tax = st.selectbox("Conformité fiscale",
                                  options=['Yes', 'No', "Don’t know or N/A"])
    
    # Accès financier
    st.subheader("🏦 Accès financier")
    has_mobile_money = st.selectbox("Mobile Money", 
                                    options=['Have now', 'Never had', "Used to have but don't have now"])
    has_insurance = st.selectbox("Assurance",
                                options=['Have now', 'Never had', "Used to have but don't have now"])
    has_credit_card = st.selectbox("Carte de crédit",
                                   options=['Have now', 'Never had', "Used to have but don't have now"])
    has_debit_card = st.selectbox("Carte de débit",
                                 options=['Have now', 'Never had', "Used to have but don't have now"])
    has_bank_account = st.selectbox("Compte bancaire",
                                    options=['Have now', 'Never had', "Used to have but don't have now"])
    has_loan_account = st.selectbox("Compte de prêt",
                                    options=['Have now', 'Never had', "Used to have but don't have now"])
    has_internet_banking = st.selectbox("Internet banking",
                                        options=['Have now', 'Never had', "Used to have but don't have now"])
    
    # Motivations
    st.subheader("🎯 Motivations")
    motivation_money = st.selectbox("Motivation : gagner plus d'argent",
                                    options=['Yes', 'No', "Don’t know or N/A"])
    
    # Risques
    st.subheader("⚠️ Risques perçus")
    future_risk = st.selectbox("Risque de vol de stock",
                               options=['Yes', 'No', "Don’t know or N/A"])
    
    # Autres colonnes nécessaires
    st.subheader("📋 Autres informations")
    medical_insurance = st.selectbox("Assurance médicale",
                                     options=['Have now', 'Never had', "Used to have but don't have now"])
    funeral_insurance = st.selectbox("Assurance obsèques",
                                     options=['Have now', 'Never had', "Used to have but don't have now"])
    uses_friends_family = st.selectbox("Utilise l'épargne famille/amis",
                                       options=['Yes', 'No', 'Never had', "Don’t know or N/A"])
    uses_informal_lender = st.selectbox("Utilise des prêteurs informels",
                                       options=['Yes', 'No', 'Never had', "Don’t know or N/A"])
    
    # Perception de l'assurance
    perception_no_cover = st.selectbox("L'assurance ne couvre pas les pertes ?",
                                       options=['Yes', 'No', "Don't know"])
    perception_cannot_afford = st.selectbox("Ne peut pas payer l'assurance ?",
                                           options=['Yes', 'No', "Don't know"])

# Construction du dictionnaire d'entrée (tout en string pour éviter les problèmes)
input_dict = {
    'owner_age': str(owner_age),
    'business_age_months': str(business_age_months),
    'business_age_years': str(business_age_years),
    'personal_income': str(personal_income),
    'business_expenses': str(business_expenses),
    'business_turnover': str(business_turnover),
    'country': country,
    'attitude_stable_business_environment': attitude_stable,
    'attitude_worried_shutdown': attitude_worried,
    'compliance_income_tax': compliance_tax,
    'has_mobile_money': has_mobile_money,
    'has_insurance': has_insurance,
    'has_credit_card': has_credit_card,
    'has_debit_card': has_debit_card,
    'has_bank_account': has_bank_account,
    'has_loan_account': has_loan_account,
    'has_internet_banking': has_internet_banking,
    'motivation_make_more_money': motivation_money,
    'future_risk_theft_stock': future_risk,
    'medical_insurance': medical_insurance,
    'funeral_insurance': funeral_insurance,
    'uses_friends_family_savings': uses_friends_family,
    'uses_informal_lender': uses_informal_lender,
    'perception_insurance_doesnt_cover_losses': perception_no_cover,
    'perception_cannot_afford_insurance': perception_cannot_afford,
    'has_motor_vehicle_insurance': 'Never had',
    'motor_vehicle_insurance': 'Never had',
    'business_age': str(business_age_years),
}

# Bouton de prédiction
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    predict_button = st.button("🔮 PRÉDIRE LA SANTÉ FINANCIÈRE", type="primary", use_container_width=True)

if predict_button:
    with st.spinner("Analyse en cours..."):
        try:
            # Preprocessing des données
            input_processed = preprocess_input(input_dict, metadata, transformers)
            
            # Vérification des types
            st.write("Debug - Vérification des types après preprocessing :")
            for col in input_processed.columns[:5]:  # Afficher les 5 premières colonnes
                st.write(f"{col}: {input_processed[col].dtype}, valeur: {input_processed[col].values[0]}")
            
            # Prédiction
            prediction = model.predict(input_processed)
            prediction_proba = model.predict_proba(input_processed)
            
            inv_map = metadata['inv_label_map']
            predicted_class = inv_map[str(prediction[0])]
            
            # Affichage des résultats
            st.markdown("---")
            st.header("📊 RÉSULTATS DE L'ANALYSE")
            
            # Métriques principales
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric(
                    label="🟡 Santé Basse",
                    value=f"{prediction_proba[0][0]*100:.1f}%"
                )
            with col2:
                st.metric(
                    label="🟠 Santé Moyenne",
                    value=f"{prediction_proba[0][1]*100:.1f}%"
                )
            with col3:
                st.metric(
                    label="🟢 Santé Élevée",
                    value=f"{prediction_proba[0][2]*100:.1f}%"
                )
            
            # Résultat principal
            st.markdown("---")
            if predicted_class == 'High':
                st.success("### 🎉 PRÉDICTION : SANTÉ FINANCIÈRE ÉLEVÉE")
                st.info("✨ L'entreprise présente d'excellents indicateurs de santé financière.")
            elif predicted_class == 'Medium':
                st.warning("### 📊 PRÉDICTION : SANTÉ FINANCIÈRE MOYENNE")
                st.info("📈 L'entreprise montre des signes positifs mais nécessite une attention.")
            else:
                st.error("### ⚠️ PRÉDICTION : SANTÉ FINANCIÈRE BASSE")
                st.info("🔧 Des améliorations sont nécessaires pour stabiliser la situation.")
            
            # Graphique
            st.markdown("---")
            st.subheader("📈 Distribution des probabilités")
            
            chart_data = pd.DataFrame({
                'Catégorie': ['Basse', 'Moyenne', 'Élevée'],
                'Probabilité': [prediction_proba[0][0], prediction_proba[0][1], prediction_proba[0][2]]
            })
            st.bar_chart(chart_data.set_index('Catégorie'))
            
            # Recommandations
            st.markdown("---")
            st.subheader("💡 RECOMMANDATIONS")
            
            if predicted_class == 'Low':
                st.write("""
                - 📈 **Formaliser l'activité** : Ouvrir un compte bancaire professionnel
                - 💳 **Développer l'inclusion financière** : Utiliser le mobile money
                - 📊 **Améliorer la gestion** : Tenir une comptabilité régulière
                - 🤝 **Rechercher du mentorat** auprès d'entreprises établies
                """)
            elif predicted_class == 'Medium':
                st.write("""
                - 📊 **Optimiser la trésorerie** : Mieux gérer les flux financiers
                - 🎓 **Se former** : Formation en gestion financière d'entreprise
                - 💳 **Explorer les services** : Assurance, crédit, épargne
                - 📈 **Planifier la croissance** : Établir un plan sur 3 ans
                """)
            else:
                st.write("""
                - 🌍 **Envisager l'expansion** : Explorer de nouveaux marchés
                - 👥 **Former une équipe** : Déléguer certaines responsabilités
                - 💼 **Optimiser fiscalement** : Consulter un expert comptable
                - 🎯 **Devenir mentor** : Partager votre expérience
                """)
            
        except Exception as e:
            st.error(f"❌ Erreur lors de la prédiction : {str(e)}")
            st.info("Vérifiez que les données saisies sont correctes.")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: gray; font-size: 12px;'>
    🔮 Modèle HistGradientBoosting entraîné sur données PME Africaines<br>
    ⚠️ Outil d'aide à la décision - Consultation d'un expert recommandée
</div>
""", unsafe_allow_html=True)