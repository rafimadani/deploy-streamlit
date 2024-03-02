import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')


def get_data_byweather(df):
    byweather_df = df.groupby(by="weathersit").agg({
        "cnt": "sum"
    })
    byweather_df.rename(columns={
        "cnt": "customer_count"
    }, inplace=True)
    return byweather_df

def get_data_season(df):
    byseason_df = hour_df.groupby(by="season").agg({
        "cnt": "sum"
    })
    byseason_df.rename(columns={
        "cnt": "customer_count"
    }, inplace=True)
    return byseason_df

hour_df = pd.read_csv('hour.csv')

byweather_df = get_data_byweather(hour_df)
byseason_df = get_data_season(hour_df)

st.header("Hubungan Cuaca dan Musim terhadap peminjaman sepeda :star:")

st.subheader("by Rafi Madani")

# Graph Total Rent Count By Weather
plt.figure(figsize=(10, 5))

top = byweather_df.nlargest(1, 'customer_count') # Mencari tahu siapa rent tertinggi

palette = ['#FFA500' if index in top.index else '#0000FF' for index in byseason_df.index]
 
sns.barplot(
    y=byweather_df['customer_count'], 
    x=byweather_df.index,
    data=byweather_df.sort_values(by="customer_count", ascending=False),
    palette= palette
)
plt.title("Total Rent Count by Weather", loc="center", fontsize=15)
plt.ylabel("Number of Customer")
plt.xlabel("Weather")
plt.tick_params(axis='x', labelsize=12)

labels = ["1: Clear, Few clouds, Partly cloudy, Partly cloudy", "2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist", "3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds", "4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog"]
colors = palette

for i, label in enumerate(labels):
    plt.plot([], [], color=colors[i], label=label)
    
plt.legend()

st.pyplot(plt)

# Graph Total Rent Count By Season

plt.figure(figsize=(10, 5))

top = byseason_df.nlargest(1, 'customer_count') 

palette = ['#FFA500' if index in top.index else '#0000FF' for index in byseason_df.index]

sns.barplot(
    y=byseason_df['customer_count'], 
    x=byseason_df.index,
    data=byseason_df.sort_values(by="customer_count", ascending=False),
    palette= palette
)
plt.title("Total Rent Count by Season", loc="center", fontsize=15)
plt.ylabel("Number of Customer")
plt.xlabel("Season")
plt.tick_params(axis='x', labelsize=12)

labels = ["1: Spring", "2: Summer","3: Fall", "4: Winter"]
colors = palette

for i, label in enumerate(labels):
    plt.plot([], [], color=colors[i], label=label)
    
plt.legend()

st.pyplot(plt)

st.text("""- Conclusion Number Of Customer By Weather

Di cuaca yang "Clear", terjadi paling banyak peminjaman sepeda dibanding cuaca lain.
        
- Conclusion Number Of Customer By Season

Di musim "Fall", terjadi paling banyak peminjaman sepeda dibanding cuaca lain. """)

