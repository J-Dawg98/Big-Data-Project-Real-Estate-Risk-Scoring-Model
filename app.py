import streamlit as st
import pandas as pd
import plotly.express as px

st.title('Real Estate Market Risk Analyzer')

#df = pd.read_csv("housing_risk.csv", low_memory=False)
df = pd.read_csv("housing_risk.csv")

city = st.selectbox('Select a City', df['Town'].unique())
filtered = df[df['Town'] == city]

st.metric(label='Current Risk Score', value = round(filtered['risk_score'].mean(), 2))

fig = px.line(filtered, x = 'Transaction Date', y='risk_score', title='Risk over Time')
st.plotly_chart(fig)