
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as plt
import pyplot
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


#load dataset
df = pd.read_csv('./data/heart_disease_health_indicators.csv')
df['Age'] = df['Age']*4



#initialisation de la page web
st.set_page_config(page_title="Data Analyse", page_icon=":book:", layout="wide")

#pour les animations
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


#local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_heartbeat = load_lottieurl("https://assets7.lottiefiles.com/private_files/lf30_jrkcz8oc.json")
lottie_heartbeat2 = load_lottieurl("https://assets7.lottiefiles.com/private_files/lf30_bkwar9l2.json")
img_correlations = Image.open("./images/correlations.PNG")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Bonjour ! :wave:")
    st.title("Peut-on prédire une attaque cardiaque ?")

# ---- Exploration des donnees ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Exploration des données")
        st.write("##")
        st.write(
            """
            Informations sur le Dataset :
            - Nombres de personnes intérogés : 253 680
            - Date de l'enquete : 2015
            - Zone : Amérique
            - Auteur : CDC (Centres pour le contrôle et la prévention des maladies)

            """
        )
        st.write("[Dataset >](https://www.kaggle.com/datasets/alexteboul/heart-disease-health-indicators-dataset)")
    with right_column:
        st_lottie(lottie_heartbeat, height=300, key="heartbeat")

# ---- PROJECT ----
with st.container():
    st.write("---")
    st.header("Mon etude")
    st.write("##")
    code1 = '''fc = heart_data['Smoker'].tolist()
fs = []
for x in range(len(fc)):
    if int(fc[x]) == 1:
        fs.append(fc[x])
        

print("Nombre de personnes qui fumes ", len(fs))'''
    
    st_lottie(lottie_heartbeat2, height=200, key="heartbeat2")
    st.subheader("Integrate Lottie Animations Inside Your Streamlit App")
    st.code(code1, language='python')
    st.write("""Nombre de personnes qui fumes  112423""")

    st.write("---")
    st.write("##")
    st.write("""Extrait des données""")
    st.dataframe(df)

    st.write("---")
    st.write("##")
    st.write("""Quelques chiffres...""")
    st.dataframe(df.describe())
    
    st.write("---")
    st.write("##")
    ax = sns.histplot(df['Age'], kde=False, color='red')
    ax.set(xlabel='Age', ylabel='Nombres de personnes')
    st.pyplot(plt)
    

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Test ! Donnez votre avis !")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/avrit.max@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
