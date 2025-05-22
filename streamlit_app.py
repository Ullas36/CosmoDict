### streamlit_app.py

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from redshift_calculator import relativistic_velocity, hubble_distance, light_travel_time

st.set_page_config(page_title="CosmoDist: Redshift Explorer", layout="centered")
st.title("🌌 CosmoDist: Explore the Expanding Universe")

st.markdown("""
Enter a **redshift (z)** value to calculate the distance, velocity, and time the light has taken to reach us. This uses:
- **Relativistic Doppler formula** for recession velocity
- **Hubble's Law** for distance
- **Speed of light** for time
""")

# --- Input ---
z = st.slider("Redshift (z)", min_value=0.0, max_value=10.0, value=0.5, step=0.01)

# --- Calculations ---
velocity = relativistic_velocity(z)
distance = hubble_distance(velocity)
time_billion_years = light_travel_time(distance)

# --- Output Results ---
st.subheader("📊 Results")
st.write(f"**Recession velocity:** {velocity:,.0f} km/s")
st.write(f"**Distance:** {distance:.2f} Mpc (~{distance * 3.26:.2f} million light-years)")
st.write(f"**Light travel time:** {time_billion_years:.2f} billion years")

# --- Graphs ---
z_vals = np.linspace(0.01, 10, 500)
velocities = [relativistic_velocity(z_) for z_ in z_vals]
distances = [hubble_distance(v) for v in velocities]
times = [light_travel_time(d) for d in distances]

fig, ax = plt.subplots()
ax.plot(z_vals, times, color='orange')
ax.set_xlabel("Redshift (z)")
ax.set_ylabel("Light Travel Time (billion years)")
ax.set_title("Redshift vs Light Travel Time")
st.pyplot(fig)

fig2, ax2 = plt.subplots()
ax2.plot(z_vals, distances, color='blue')
ax2.set_xlabel("Redshift (z)")
ax2.set_ylabel("Distance (Mpc)")
ax2.set_title("Redshift vs Distance")
st.pyplot(fig2)

st.markdown("---")
st.caption("Created with 🔭 by CosmoDist")
