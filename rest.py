import streamlit as st
import pandas as pd

st.set_page_config(page_title="Restaurant Recommendation", page_icon="🍽️")

st.title("🍽️ Restaurant Recommendation System")

# Load dataset
df = pd.read_csv("restaurants.csv")

# User Inputs
city = st.selectbox("Select City", sorted(df["City"].unique()))
cuisine = st.selectbox("Select Cuisine", sorted(df["Cuisine"].unique()))
budget = st.slider("Maximum Budget (₹)", 100, 2000, 500)
rating = st.slider("Minimum Rating", 1.0, 5.0, 4.0)

if st.button("Recommend Restaurants"):

    result = df[
        (df["City"] == city) &
        (df["Cuisine"] == cuisine) &
        (df["Budget"] <= budget) &
        (df["Rating"] >= rating)
    ]

    if len(result) > 0:
        st.success("Recommended Restaurants")

        st.dataframe(result)

    else:
        st.error("No restaurants found. Try changing your filters.")