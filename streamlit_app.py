import streamlit as st
import random

st.set_page_config(page_title="Faviee Mini GH", page_icon="🇬🇭")

st.title("🇬🇭 Faviee Mini GH - Level 3")
st.subheader("Ghana Pidgin Hype Machine!")

name = st.text_input("Enter your name:", "Stephanie Oduro")
vibe = st.selectbox("Choose vibe:", ["Starboy Legend", "Slay Queen", "Big Boss", "Chale Wossop", "Soft Life"])

hypes = [
    f"Chale {name}! You be {vibe}! Ghana to the world! 🇬🇭",
    f"Ei {name}! You too fresh! Kasoa traffic no fit stop your shine!",
    f"{name} you be {vibe}! You dey burst my mind!",
    f"Chale {name}! {vibe} vibes only! Make Ghana proud!"
]

if st.button("Generate Hype!"):
    st.success(random.choice(hypes))
    st.balloons()

st.caption("Built in Accra GH 🇬🇭")
