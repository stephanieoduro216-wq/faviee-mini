import streamlit as st
import random

st.set_page_config(page_title="Faviee Mini GH", page_icon="🇬🇭", layout="centered")

st.markdown("""
<style>
    .stButton>button {background-color: #CE1126; color: white; border-radius: 20px; font-weight: bold;}
</style>
""", unsafe_allow_html=True)

st.title("🇬🇭 Faviee Mini GH - Level 4")
st.subheader("Ghana Pidgin Hype Machine + Swag!")

col1, col2 = st.columns(2)
with col1:
    name = st.text_input("Enter your name:", "Stephanie Oduro")
with col2:
    vibe = st.selectbox("Choose vibe:", ["Starboy Legend", "Slay Queen", "Big Boss", "Chale Wossop", "Soft Life", "Accra Hottie"])

mood = st.slider("How fresh you dey feel today? (1-10)", 1, 10, 8)

hypes = [
    f"Chale {name}! You be {vibe}! Ghana to the world! 🇬🇭⭐ Fresh level: {mood}/10!",
    f"Ei {name}! You too fresh! Kasoa traffic no fit stop your shine! Level {mood} boss!",
    f"{name} you be {vibe}! You dey burst my mind! 🔥🔥",
    f"Chale {name}! {vibe} vibes only! Make Ghana proud! You be {mood*10}% star!",
    f"Herh {name}! You be correct {vibe}! Everybody for Accra dey look you! 👀🇬🇭"
]

if st.button("Generate Hype! 💥"):
    st.success(random.choice(hypes))
    st.balloons()
    st.snow()

st.markdown("---")
st.caption("Built in Accra GH 🇬🇭 | Level 4 - Styled by Stephanie")
st.link_button("Visit Faviee.com 🛍️", "https://faviee.com")
