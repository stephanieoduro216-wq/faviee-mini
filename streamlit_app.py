import streamlit as st
st.set_page_config(page_title="Faviee Mini")
st.title("Faviee Mini GH")
st.subheader("Ghana Pidgin Hype!")
name = st.text_input("Enter your name:")
if st.button("Generate Hype!"):
  if name:
    st.success(f"Chale {name}! You be Starboy Legend!")
    st.balloons()
  else:
    st.warning("Enter name first!")
st.caption("Built in Accra GH")
