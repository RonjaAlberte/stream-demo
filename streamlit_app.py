import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

col_1, col_2 = st.columns([1,10])

with col_1:
    st.markdown("Hi!")

with col_2:
    st.title("Hello??")