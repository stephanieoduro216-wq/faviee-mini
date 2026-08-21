
import streamlit as st
import random

st.set_page_config(page_title="Faviee GH Level 2", page_icon="🇬🇭")

st.markdown("""
<style>
.stApp { background: #FFFDE7; }
h1 { color: #CE1126; }
</style>
""", unsafe_allow_html=True)

st.title("🇬🇭 Faviee Mini GH - Level 2")
st.subheader("Ghana Pidgin Hype Machine!")

name = st.text_input("Enter your name:", placeholder="Stephanie Oduro")
vibe = st.selectbox("Choose vibe:", ["Starboy Legend", "Shatta Movement", "Black Stars Energy", "Jollof Boss"])

hypes = [
    f"Chale {name}! You be {vibe}! Ghana to the world! 🌍",
    f"Ei {name}! You too fresh! Kasoa traffic can't stop you! 🔥",
    f"{name}! You be correct correct! Even Makola women dey holla! 💃",
    f"Chale {name}! You be 10/10! No size! 🇬🇭✨",
    f"{name}!! Accra to Kumasi, everybody dey feel you! You be {vibe}!",
    f"Herh {name}! You dey shine like Black Star! ⭐"
]

if st.button("Generate Hype! 🚀", type="primary"):
    if name:
        hype = random.choice(hypes)
        st.success(f"### {hype}")
        st.balloons()
        st.snow()
        st.caption("Copy am and post for WhatsApp Status!")
    else:
        st.warning("Enter your name first, Bossu!")

st.divider()
st.caption("Built in Accra GH with ❤️ | Level 2 - Upgraded by Stephanie")
