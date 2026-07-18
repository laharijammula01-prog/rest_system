import streamlit as st
import pandas as pd

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Restaurant Recommendation System",
    page_icon="🍽️",
    layout="wide"
)

st.title("🍽️ Restaurant Recommendation System")
st.write("Find restaurants based on your preferences.")

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("restaurants.csv")

# -----------------------------
# Sidebar Filters
# -----------------------------
st.sidebar.header("Filter Restaurants")

city = st.sidebar.selectbox(
    "Select City",
    ["All"] + sorted(df["City"].unique().tolist())
)

cuisine = st.sidebar.selectbox(
    "Select Cuisine",
    ["All"] + sorted(df["Cuisine"].unique().tolist())
)

budget = st.sidebar.slider(
    "Maximum Budget (₹)",
    int(df["Budget"].min()),
    int(df["Budget"].max()),
    int(df["Budget"].max())
)

rating = st.sidebar.slider(
    "Minimum Rating",
    float(df["Rating"].min()),
    float(df["Rating"].max()),
    float(df["Rating"].min()),
    step=0.1
)

# -----------------------------
# Recommend Button
# -----------------------------
if st.button("🍴 Recommend Restaurants"):

    result = df.copy()

    # Filter by City
    if city != "All":
        city_result = result[result["City"] == city]
        if not city_result.empty:
            result = city_result

    # Filter by Cuisine
    if cuisine != "All":
        cuisine_result = result[result["Cuisine"] == cuisine]
        if not cuisine_result.empty:
            result = cuisine_result

    # Filter by Budget
    budget_result = result[result["Budget"] <= budget]
    if not budget_result.empty:
        result = budget_result

    # Filter by Rating
    rating_result = result[result["Rating"] >= rating]
    if not rating_result.empty:
        result = rating_result

    result = result.sort_values(
        by=["Rating", "Budget"],
        ascending=[False, True]
    )

    st.success(f"Showing {len(result)} Restaurant(s)")

    st.dataframe(result, use_container_width=True)

# -----------------------------
# Show All Restaurants
# -----------------------------
st.markdown("---")

if st.checkbox("📋 Show Complete Restaurant List"):
    st.dataframe(
        df.sort_values(
            by=["City", "Rating"],
            ascending=[True, False]
        ),
        use_container_width=True
    )