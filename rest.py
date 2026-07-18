import streamlit as st
import pandas as pd

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="Restaurant Recommendation System",
    page_icon="🍽️",
    layout="wide"
)

st.title("🍽️ Restaurant Recommendation System")
st.write("Find the best restaurants based on your preferences.")

# ----------------------------
# Load Dataset
# ----------------------------
df = pd.read_csv("restaurants.csv")

# ----------------------------
# User Inputs
# ----------------------------
city = st.selectbox(
    "Select City",
    ["All"] + sorted(df["City"].unique().tolist())
)

cuisine = st.selectbox(
    "Select Cuisine",
    ["All"] + sorted(df["Cuisine"].unique().tolist())
)

budget = st.slider(
    "Maximum Budget (₹)",
    min_value=int(df["Budget"].min()),
    max_value=int(df["Budget"].max()),
    value=int(df["Budget"].max())
)

rating = st.slider(
    "Minimum Rating",
    min_value=float(df["Rating"].min()),
    max_value=float(df["Rating"].max()),
    value=float(df["Rating"].min()),
    step=0.1
)

# ----------------------------
# Recommendation Button
# ----------------------------
if st.button("🍴 Recommend Restaurants"):

    result = df.copy()

    # Filter by City
    if city != "All":
        result = result[result["City"] == city]

    # Filter by Cuisine
    if cuisine != "All":
        result = result[result["Cuisine"] == cuisine]

    # Filter by Budget
    result = result[result["Budget"] <= budget]

    # Filter by Rating
    result = result[result["Rating"] >= rating]

    # Display Results
    if not result.empty:

        result = result.sort_values(
            by=["Rating", "Budget"],
            ascending=[False, True]
        )

        st.success(f"✅ {len(result)} Restaurant(s) Found")

        st.dataframe(result, use_container_width=True)

    else:
        st.warning("No restaurants found for the selected filters.")

# ----------------------------
# Show Complete Dataset
# ----------------------------
st.markdown("---")

if st.checkbox("📋 Show All Restaurants"):
    st.dataframe(df, use_container_width=True)