import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu

# Configuration de la page
st.set_page_config(
    page_title="Veille IA",
    page_icon="🤖",
    layout="wide"
)

# Lecture du fichier CSV des utilisateurs
@st.cache_data
def load_users():
    df = pd.read_csv('users.csv')
    # Conversion du dataframe en dictionnaire simple
    users_dict = {}
    
    for _, row in df.iterrows():
        username = row['name']
        users_dict[username] = {
            'password': row['password'],
            'email': row['email'],
            'role': row['role']
        }
    
    return users_dict

# Chargement des données utilisateurs
user_accounts = load_users()

# Fonction pour afficher la veille technologique IA
def show_ai_news():
    st.title("Veille Technologique : Dernières Avancées en IA 🤖")
    st.write("Découvrez les trois innovations récentes les plus marquantes dans le domaine de l'intelligence artificielle.")
    
    # Création de 3 colonnes pour afficher les innovations
    col1, col2, col3 = st.columns(3)
    
    # Première innovation
    with col1:
        st.subheader("Modèles Multimodaux")
        st.markdown("![Modèles Multimodaux](https://placehold.co/400x250/1E88E5/FFFFFF?text=Modeles+Multimodaux)")
        st.write("""
        Les modèles multimodaux comme GPT-4V, Claude 3 et Gemini peuvent désormais traiter 
        simultanément texte, images, et dans certains cas audio et vidéo. 
        Ces modèles permettent des interactions plus naturelles et complètes 
        avec l'IA, ouvrant la voie à de nouvelles applications comme 
        l'analyse d'images médicales avec contexte textuel ou la création 
        de contenu cross-média.
        """)
    
    # Deuxième innovation
    with col2:
        st.subheader("Agents IA Autonomes")
        st.markdown("![Agents IA](https://placehold.co/400x250/4CAF50/FFFFFF?text=Agents+IA+Autonomes)")
        st.write("""
        Les agents IA autonomes comme AutoGPT peuvent désormais planifier et 
        exécuter des séquences complexes de tâches avec peu d'intervention humaine. 
        Ces agents utilisent des LLMs pour décomposer les objectifs en sous-tâches, 
        les exécuter et s'auto-corriger. Ils peuvent naviguer sur le web, 
        utiliser des outils et même écrire et exécuter du code pour atteindre leurs objectifs.
        """)
    
    # Troisième innovation
    with col3:
        st.subheader("IA Générative Locale")
        st.markdown("![IA Locale](https://placehold.co/400x250/FF9800/FFFFFF?text=IA+Generative+Locale)")
        st.write("""
        Des modèles comme Llama 3, Mistral et Claude Haiku peuvent maintenant 
        fonctionner directement sur les appareils des utilisateurs. 
        Ces modèles optimisés offrent un bon équilibre entre performance 
        et taille, permettant des applications qui respectent la vie privée
        et fonctionnent sans connexion internet. Cette avancée démocratise 
        l'accès à l'IA générative tout en réduisant les coûts d'infrastructure.
        """)

# Fonction pour la page d'accueil
def show_home():
    st.title("Bienvenue sur notre Veille Technologique IA! 👋")
    st.write("""
    Cette application vous permet de découvrir les dernières avancées dans le domaine de l'intelligence artificielle.
    Utilisez le menu situé dans la barre latérale pour naviguer entre les différentes pages.
    """)
    
    st.info("Cette application a été créée dans le cadre d'un challenge Streamlit.")

# Initialisation des états de session
if "authentication_status" not in st.session_state:
    st.session_state["authentication_status"] = None
if "username" not in st.session_state:
    st.session_state["username"] = None

# Interface de connexion
if st.session_state["authentication_status"] is not True:
    st.title("Connexion")
    
    # Créer des colonnes pour centrer le formulaire
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        username = st.text_input("Nom d'utilisateur")
        password = st.text_input("Mot de passe", type="password")
        
        if st.button("Se connecter"):
            if username in user_accounts:
                if password == user_accounts[username]["password"]:
                    st.session_state["authentication_status"] = True
                    st.session_state["username"] = username
                    st.rerun()
                else:
                    st.session_state["authentication_status"] = False
                    st.error("Mot de passe incorrect")
            else:
                st.session_state["authentication_status"] = False
                st.error("Utilisateur inconnu")

# Vérification du statut d'authentification
if st.session_state["authentication_status"]:
    # Si l'utilisateur est connecté, afficher le contenu
    with st.sidebar:
        st.write(f"Bienvenue {st.session_state['username']} 👋")
        
        # Menu de navigation dans la sidebar
        selection = option_menu(
            menu_title=None,
            options=["Accueil", "Veille IA"],
            icons=["house", "robot"],
            menu_icon="cast",
            default_index=0,
        )
        
        # Bouton de déconnexion
        if st.button("Déconnexion"):
            st.session_state["authentication_status"] = None
            st.session_state["username"] = None
            st.rerun()
    
    # Affichage du contenu en fonction de la sélection
    if selection == "Accueil":
        show_home()
    elif selection == "Veille IA":
        show_ai_news()

elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est incorrect")
