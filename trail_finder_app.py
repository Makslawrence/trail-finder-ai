import streamlit as st
import pandas as pd

# Load the dataset
df = pd.read_csv("australian_4x4_trails.csv")

# Streamlit app layout
st.title("🇦🇺 Trail Finder AI – Australia Edition")
st.markdown("Find off-road trails tailored to your 4x4 setup and skill level.")

# User inputs
location_input = st.text_input("Enter your location (e.g., Victoria, NSW, QLD):")
vehicle_type_input = st.selectbox("Select your vehicle type:", ["Stock", "Lifted", "Dual Cab", "Any"])
skill_level_input = st.selectbox("Select your skill level:", ["Beginner", "Intermediate", "Advanced"])

# Filter and recommend trails
if st.button("Find Trails"):
    filtered = df.copy()

    if location_input:
        filtered = filtered[filtered['Location'].str.contains(location_input, case=False, na=False)]

    if vehicle_type_input != "Any":
        filtered = filtered[filtered['Vehicle Type'].str.contains(vehicle_type_input, case=False, na=False)]

    filtered = filtered[filtered['Skill Level'].str.contains(skill_level_input, case=False, na=False)]

    if filtered.empty:
        st.warning("No matching trails found. Try adjusting your filters.")
    else:
        st.success(f"Found {min(5, len(filtered))} matching trail(s):")
        for _, row in filtered.head(5).iterrows():
            st.markdown(f"### {row['Trail Name']}")
            st.markdown(f"**Location:** {row['Location']}")
            st.markdown(f"**Difficulty:** {row['Difficulty']}")
            st.markdown(f"**Terrain:** {row['Terrain']}")
            st.markdown(f"More Info")
            st.markdown("---")
