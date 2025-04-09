# 🤖 Application de Veille Technologique IA

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)

## 📋 Présentation

Cette application Streamlit a été créée dans le cadre d'un challenge Wild Code School pour présenter une veille technologique sur les dernières avancées en intelligence artificielle. Elle démontre l'utilisation des fonctionnalités avancées de Streamlit : menu de navigation, système d'authentification et déploiement en ligne.

![Aperçu de l'application](https://placehold.co/800x400/1E88E5/FFFFFF?text=Veille+Technologique+IA)

## ✨ Fonctionnalités

- **🔐 Authentification sécurisée** : Système de connexion basé sur un fichier CSV
- **🧭 Navigation intuitive** : Menu latéral pour accéder aux différentes sections
- **📊 Veille IA** : Présentation des trois dernières innovations majeures en IA
- **🌐 Compatible Cloud** : Prêt pour le déploiement sur Streamlit Cloud

## 🏗️ Structure de l'application

### Pages principales

| Page | Description |
|------|-------------|
| **🏠 Accueil** | Introduction générale à l'application |
| **🤖 Veille IA** | Présentation des trois innovations récentes en IA |

### Innovations présentées

1. **Modèles Multimodaux** - Traitement simultané de texte, images et audio
2. **Agents IA Autonomes** - Planification et exécution de tâches complexes
3. **IA Générative Locale** - Modèles optimisés pour les appareils des utilisateurs

## 🔑 Identifiants de connexion

Pour tester l'application, vous pouvez utiliser les identifiants suivants :

| Rôle | Identifiant | Mot de passe |
|------|-------------|--------------|
| **Utilisateur standard** | `utilisateur` | `utilisateurMDP` |
| **Administrateur** | `root` | `rootMDP` |

## 🚀 Installation et démarrage local

```bash
# Cloner le repository
git clone https://github.com/votre-nom/veille-ia-streamlit.git
cd veille-ia-streamlit

# Installer les dépendances
pip install -r requirements.txt

# Lancer l'application
streamlit run app.py
```

## ☁️ Déploiement sur Streamlit Cloud

1. **Créer un compte** sur [Streamlit Cloud](https://streamlit.io/)
2. **Créer un repository GitHub** contenant les fichiers de l'application
3. **Se connecter** à Streamlit Cloud et cliquer sur "New app"
4. **Sélectionner le repository** et configurer le déploiement
5. **Cliquer sur "Deploy"** pour mettre l'application en ligne
6. **Configurer la visibilité** en mode public dans les paramètres

![Déploiement Streamlit](https://placehold.co/800x300/4CAF50/FFFFFF?text=Streamlit+Cloud+Deployment)

## 📁 Fichiers inclus

```
veille-ia-streamlit/
├── app.py              # Code principal de l'application
├── users.csv           # Base de données des utilisateurs
├── requirements.txt    # Dépendances nécessaires
└── README.md           # Documentation
```

## ⚙️ Personnalisation

L'application est conçue pour être facilement modifiable :

- **Modifier les utilisateurs** : Ajoutez ou modifiez les entrées dans `users.csv`
- **Changer les contenus** : Mettez à jour les informations dans les fonctions `show_home()` et `show_ai_news()`
- **Ajouter des pages** : Étendez le menu en ajoutant de nouvelles options et fonctions correspondantes

## 🔧 Résolution des problèmes courants

| Problème | Solution |
|----------|----------|
| Erreurs d'authentification | Vérifiez le format du fichier CSV et les versions des dépendances |
| Images non affichées | Utilisez des URLs d'images accessibles publiquement |
| Erreurs de dépendances | Mettez à jour `requirements.txt` avec les versions exactes |

## 📝 Notes de développement

Cette application utilise les fonctionnalités avancées de Streamlit :

- `streamlit_option_menu` pour la navigation entre les pages
- Stockage des états dans `st.session_state` pour la gestion de l'authentification
- Mise en page responsive avec `st.columns()`

---

Créé par Loïc| [Wild Code School](https://www.wildcodeschool.com/)
