import streamlit as st
import base64

st.set_page_config(page_title="Mandat Sanitaire", layout="wide", page_icon="🐾")

# === Base64 images ===
def img_to_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

admin_b64 = img_to_base64("icons/admin.png")
interface_b64 = img_to_base64("icons/interface.png")

# ---------------------------
# CHARGEMENT CSS
# ---------------------------

def load_css(path="style.css"):
    with open(path, "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
load_css("style.css")

def home():

    st.set_page_config(page_title="Accueil", layout="wide")
    # Redirection par cartes (form)
    page = st.query_params.get("page")
    if page == "Admin":
        st.switch_page("pages/0_Dashboard.py")
    elif page == "InterfaceUser":
        st.switch_page("pages/1_Saisie.py")
    st.sidebar.empty()

    st.markdown('<div class="home-page">', unsafe_allow_html=True)
    st.markdown("""
<div class="hero-background">
<h1 class="hero-title" style='color:white;'>Mandat Sanitaire - Plateforme de Vaccination</h1>
<p class="hero-subtitle">Suivi des campagnes, statistiques en temps réel et saisie terrain</p>
</div>
</div>
            """, unsafe_allow_html=True)

    st.markdown(f"""
<div class="card-container" style="margin-bottom:50px;">
<form action="" method="get">
<button name="page" value="Admin" class="card-button">
<img src="data:image/png;base64,{admin_b64}" />
<div class="card-title">Dashboard D'analyse</div>
<div class="card-description" style='margin-bottom:20px;'>
    Visualiser les KPIs, filtrer par région/date, suivre les campagnes (ovins, caprins, bovins, rage).
</div>
</button>
</form>

<form action="" method="get">
<button name="page" value="InterfaceUser" class="card-button">
<img src="data:image/png;base64,{interface_b64}" />
<div class="card-title">Interface de Saisie</div>
<div class="card-description" style='margin-bottom:20px;'>
    Saisir les vaccinations sur le terrain et enregistrer directement dans le fichier Excel.
</div>
</button>
</form>
</div>
            """, unsafe_allow_html=True)


# === Navigation configuration ===
# === Configuration de la navigation ===
nav = st.navigation({
    "Accueil": [home],
    "Dashboard": [
        st.Page("pages/0_Dashboard.py", title="Dashboard D'analyse"),
    ],
    "Interface": [
        st.Page("pages/1_Saisie.py", title="Interface De Saisie"),
    ],
}, position="top")


nav.run()

