import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from streamlit_option_menu import option_menu
from streamlit_authenticator import Authenticate

# Paramétrage des données utilisateurs (respecter ce format)
lesDonneesDesComptes = {
    'usernames': {
        'Correcteur': {
            'name': 'Correcteur',
            'password': 'bienveillance',
            'email': 'album@gmail.com',
            'failed_login_attemps': 0,  # Sera géré automatiquement
            'logged_in': False,          # Sera géré automatiquement
            'role': 'utilisateur'
        },
        'Moi': {
            'name': 'Moi',
            'password': 'moiMDP',
            'email': 'admin@gmail.com',
            'failed_login_attemps': 0,  # Sera géré automatiquement
            'logged_in': False,          # Sera géré automatiquement
            'role': 'administrateur'
        }
    }
}

authenticator = Authenticate(
    lesDonneesDesComptes,       # Les données des comptes
    "cookie name",              # Le nom du cookie, un str quelconque
    "cookie key",               # La clé du cookie, un str quelconque
    30,                         # Le nombre de jours avant que le cookie expire
)


# Pour afficher le formulaire
authenticator.login()

# Accès en fonction des informations à renseigner
if st.session_state["authentication_status"]:

    # Création du menu qui va afficher les choix qui se trouvent dans la variable options
    with st.sidebar:
        # Le bouton de déconnexion
        authenticator.logout("Déconnexion")
        st.write("Enjoy your visit")
        selection = option_menu(menu_title=None,options = ["🕶️😑 Accueil", "🕶️😼Photos"])

    # On indique au programme quoi faire en fonction du choix
    if selection == "🕶️😑 Accueil":
        st.title("Welcome on my page")
        st.header("Ici, ma page d'accueil !")
        st.image("images/accueil.jpeg")

    elif selection == "🕶️😼Photos":
        st.header("Et ici, la galérie d'art")  

        # Création de 3 colonnes 
        col1, col2, col3 = st.columns(3)

        # Contenu de la première colonne : 
        with col1:
            st.subheader("A l'heure du festin")
            st.image("images/souriant.jpeg")

        # Contenu de la deuxième colonne :
        with col2:
            st.subheader("Après le festin")
            st.image("images/epuise.jpeg")

        # Contenu de la troisième colonne : 
        with col3:
            st.subheader("Lorsque le festin est en retard")
            st.image("images/enerve.jpeg")

# Streamlit qui permet de garder les données entre les interactions de l'utilisateur avec l'application
elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est/sont incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning('Les champs username et mot de passe doivent être remplie')
    st.header("Bonjour à toi, très cher 'Correcteur.'")
    st.header("Je t'exprime par avance toute ma gratitute pour la 'bienveillance' de ta correction.")
    