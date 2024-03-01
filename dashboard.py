import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
sns.set(style='dark')

data_df = pd.read_csv("main_data.csv")
year_and_month = data_df.groupby(by="year_month").cnt.sum()

st.header('Rental Bikes Dashboard :sparkles:')

st.subheader('Number of Rental Bikes per Month (2011-2012)')
data_df.sort_values("yr", ascending=True)
plt.figure(figsize=(10, 5))
plt.plot(year_and_month, marker='o', linewidth=2, color="#72BCD4")
plt.title("Number of Rental Bikes per Month (2011-2012)", loc="center", fontsize=20)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.show()

fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(
    year_and_month,
    marker='o',
    linewidth=2,
    color="#90CAF9"
)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=10, labelrotation=45)

st.pyplot(fig)

st.subheader('Number of Rental Bikes with humidity, temperature, and working day')
col1, col2, col3 = st.columns(3)

with col1:
    st.write("Humidity")
    data_df.hum.hist()
    fig, ax = plt.subplots()
    ax.hist(x=data_df.hum, bins=15)
    st.pyplot(fig)

with col2:
    st.write("Temperature")
    data_df.temp.hist()
    fig, ax = plt.subplots()
    ax.hist(x=data_df.temp, bins=15)
    st.pyplot(fig)

with col3:
    st.write("Working day")
    data_df.workingday.hist()
    fig, ax = plt.subplots()
    ax.hist(x=data_df.workingday, bins=15)
    st.pyplot(fig)
