import streamlit as st
from utils.data_processing import data
import plotly.express as px

st.title("🎈 Ronja's app")
st.write(
    "Let's start building!"
)

col_1, col_2 = st.columns([2,8])

with col_1:
    st.markdown("Hi!")
    st.divider()

with col_2:
    st.title("Hello??")

state = st.selectbox("Choose state", data["State"].unique())
state_df = data[data["State"] == state]

state_df = state_df.set_index("Year")

fig = px.line(
    state_df,
    x=state_df.index,
    y=["Rape", "Kidnap and assault", "Dowry deaths", "Assault on women", "Assault on modesty", "Domestic violence", "Women trafficking"],
    labels={"value": "Number of cases", "Year": "Year"},
)

st.plotly_chart(fig)

