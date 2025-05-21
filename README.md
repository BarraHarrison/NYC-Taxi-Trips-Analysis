# 🚖 NYC Yellow Taxi Trips Analysis Dashboard

This project is an **interactive Streamlit dashboard** that explores and visualizes trends in NYC Yellow Taxi trip data using exploratory data analysis (EDA) techniques. The data is sourced from [Kaggle's NYC Yellow Taxi Dataset](https://www.kaggle.com/datasets/elemento/nyc-yellow-taxi-trip-data) and includes millions of taxi rides across several months.

The goal of this project is to uncover insights into **trip behavior, payment trends, time-based usage patterns, and spatial distributions** of pickups and drop-offs.

---

## 📊 Dashboard Features

The Streamlit app includes the following interactive tabs:

### 🕓 Peak Usage

* Visualizes taxi trip frequency by **hour of the day**
* Helps identify rush hour spikes and late-night demand patterns

### 📋 Payment Types

* Displays distribution of payment methods (credit card, cash, dispute, etc.)
* Useful for understanding consumer behavior and vendor operations

### 📘 Pickup & Dropoff Maps

* Interactive **Folium heatmaps** of high-fare pickup and dropoff zones
* Focuses on trips with **total fares above \$100**
* Geospatial patterns highlight hotspots like **airports**, **downtown Manhattan**, and **outer borough destinations**

---

## 🧪 Dataset Overview

The original dataset includes:

* **Pickup/dropoff timestamps and locations**
* **Trip distance and duration**
* **Passenger count**
* **Fare breakdown (base fare, tips, tolls, surcharges)**
* **Payment type and vendor ID**

---

## 💻 How to Run the Dashboard

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Launch the dashboard:

   ```bash
   streamlit run dashboard.py
   ```

3. View it in your browser at `http://localhost:8501`

---

## 📁 Project Structure

```
NYC-Taxi-Trips-Analysis/
├── yellow_taxi_datasets/           # Raw monthly CSVs
├── cleaned_taxi_data.parquet       # Preprocessed and optimized data file
├── main.ipynb                      # Jupyter notebook with full EDA workflow
├── dashboard.py                    # Streamlit dashboard app
└── requirements.txt                # Dependencies
```
