import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import folium
from folium.plugins import HeatMap
from streamlit_folium import st_folium

st.set_page_config(layout="wide")
st.title("🚖 NYC Yellow Taxi Trips EDA Dashboard")

@st.cache_data
def load_data():
    return pd.read_parquet("cleaned_taxi_data.parquet")

df = load_data()

df['payment_label'] = df['payment_type'].map({
    1: "Credit Card",
    2: "Cash",
    3: "No Charge",
    4: "Dispute",
    5: "Unknown",
    6: "Voided Trip"
})

st.markdown("Dataset loaded with **{} rows**.".format(len(df)))

st.sidebar.header("Filters")
fare_threshold = st.sidebar.slider("Minimum Total Fare ($)", 0, 200, 100)

filtered_df = df[df['total_amount'] >= fare_threshold]

tab1, tab2, tab3 = st.tabs(["🕓 Peak Usage", "📊 Payment Types", "🗺️ Pickup/Dropoff Maps"])

with tab1:
    fig, ax = plt.subplots()
    sns.countplot(data=df, x='hour', ax=ax, palette="viridis")
    ax.set_title("Trips by Hour of Day")
    st.pyplot(fig)

with tab2:
    fig, ax = plt.subplots()
    sns.countplot(data=df, x='payment_label', order=df['payment_label'].value_counts().index, palette='pastel', ax=ax)
    ax.set_title("Payment Method Distribution")
    st.pyplot(fig)

with tab3:
    st.subheader(f"High-Fare Dropoffs (Over ${fare_threshold})")

    high_fare_sample = filtered_df[['dropoff_lat', 'dropoff_lon']].dropna().sample(5000)

    m = folium.Map(location=[40.75, -73.97], zoom_start=11)
    HeatMap(high_fare_sample.values, radius=6).add_to(m)

    st_folium(m, width=700, height=500)
