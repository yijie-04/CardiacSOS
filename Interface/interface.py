import serial
import streamlit as st
import time
import pandas as pd
import plotly.express as px
import numpy as np
import plotly.graph_objects as go
from arduino_to_py import read

def display_part(cur, df):
    st.write(cur)
    st.write(df.iloc[cur-1])
    return df.iloc[cur-1]


def plot_graph(cur, time, placeholder, t, wl, ml, w):
    fig1 = go.Figure()
    if t: fig1.add_trace(go.Line(x=time, y=cur['Heart_Value'], name = 'Heart_Value'))
    if wl: fig1.add_trace(go.Line(x=time, y=cur['Noise'], name = 'Noise'))
    if ml: fig1.add_trace(go.Line(x=time, y=cur['Temperature'], name = 'Temperature'))
    if w: fig1.add_trace(go.Line(x=time, y=cur['Humidity'], name = 'Humidity'))
    placeholder.write(fig1)

# fishmiller chemical river
# rofarts community

st.title('Bahen City of Information and Technology - weather & energy source monitoring')

d = [{'Heart_Value':0, 'Noise': 0, 'Temperature': 0, 'Humidity': 0}]
df = pd.DataFrame(d)
speed = 0.05
real_time = np.linspace(0, 60, 300)

st.subheader('Instant Monitor Graph')
options = df.columns
weather = st.multiselect('Which info would you like to see?', options, ['Temperature'])
t, wl, ml, w = 0, 0, 0, 0
if 'Heart_Value' in weather: t = 1
if 'Noise' in weather: wl = 1
if 'Temperature' in weather: ml = 1
if 'Humidity' in weather: w = 1
placeholder = st.empty()

num = 50

if st.button("START!", key="1"):
    for i in range(num):
        cur = read()
        df = pd.concat([df, pd.DataFrame(cur)])
        plot_graph(df, real_time, placeholder, t, wl, ml, w)
        time.sleep(speed)
        #react(df)


st.subheader('Further Analysis of Specific Time')
cur = st.slider('', 0, num, num)
cur = display_part(cur, df).values.tolist

st.subheader('Suggestions for power source')

st.write(cur)

# col1, col2, col3 = st.columns(3)
# with col1:
#     if cur[1] >= 400 or cur[1] <= 80:
#         st.error("WARNING: HydroPower >50%% failure")
#     elif cur[1] >= 380:
#         st.warning("WARNING: HydroPower >20%% failure")
#     elif cur[1] >= 80:
#         st.success("WARNING: HydroPower <0.2%% failure")
# col4, col5, col6 = st.columns(3)



# alerts
# energy consumption level
        


# streamlit run interface1.py
#Temperature
#Water_Level
#Moisture_Level
#Wind
#Light_In



