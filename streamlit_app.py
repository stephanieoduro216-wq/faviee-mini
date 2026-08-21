import streamlit as st

st.set_page_config(page_title="Faviee GH", page_icon="🇬🇭")

st.markdown("<h1 style='text-align:center'>🇬🇭 Faviee Mini GH - Level 5</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center;color:#CE1126'>Ghana Pidgin Hype Machine + SWAG! ✨</h3>", unsafe_allow_html=True)

col1, col2 = st.columns([1,3])
with col1:
    st.image("https://flagcdn.com/w320/gh.png", width=80)
with col2:
    st.link_button("🛍️ Shop on Faviee.com", "https://faviee.com", use_container_width=True)

name = st.text_input("Enter your name:", "Stephanie Oduro")
vibe = st.selectbox("Choose vibe:", ["Big Boss", "Starboy Legend", "Slay Queen", "Chalewote Fresh"])
fresh = st.slider("How fresh you dey feel today? (1-10)", 1, 10, 8)

if st.button("Generate Hype! 🎉", type="primary", use_container_width=True):
    st.balloons()
    st.snow()
    hype = f"Chale {name}! You be {vibe}! Ghana to the world! 🇬🇭 Fresh level: {fresh}/10! No size!"
    st.success(hype)
    st.markdown(f"**Share your hype:**")
    wa_text = f"Chale I be {vibe}! Fresh level {fresh}/10 on Faviee Mini GH! 🇬🇭 Check am: https://faviee.com"
    st.link_button(f"Share '{vibe}' to WhatsApp 💬", f"https://wa.me/?text={wa_text}", use_container_width=True)
    st.image("https://images.unsplash.com/photo-1529139574466-a303027c1d8b?w=500", caption="Faviee Drip - Ghana Made 🇬🇭")

st.divider()
st.caption("Built in Accra GH 🇬🇭 | Powered by Faviee | Level 5 - Final Boss Complete 👑")
