import streamlit as st
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = """
Tu es IA Safe, un outil de réduction de risque pour l’usage de l’IA au travail.

Objectif :
- analyser un texte
- détecter les informations sensibles
- évaluer le niveau de risque
- proposer une version anonymisée
- rassurer sans donner d’avis juridique

Règles :
- jamais dire "tu as le droit / tu n’as pas le droit"
- parler en bonnes pratiques professionnelles
- ton calme et non culpabilisant

Structure STRICTE de réponse :

1. 🔍 Analyse
2. ⚠️ Niveau de risque (Vert / Orange / Rouge)
3. ✅ Recommandations
4. ✍️ Version safe proposée
"""

st.set_page_config(page_title="IA Safe", layout="centered")
st.title("IA Safe")
st.caption("Utilise l’IA au travail sans peur et sans te mettre en danger.")

text = st.text_area("Colle ici ton mail ou message généré avec l’IA", height=250)

if st.button("Analyser le risque"):
    if not text.strip():
        st.warning("Colle un texte pour analyse.")
    else:
        with st.spinner("Analyse en cours…"):
            res = client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": text}
                ]
            )
            st.markdown(res.choices[0].message.content)
