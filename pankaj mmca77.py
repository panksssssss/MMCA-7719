import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Simulation Function
def simulate_storage(initial_storage, growth_rate, max_capacity, days):
    storage = initial_storage
    storage_list = []

    for t in range(days):
        growth = growth_rate * storage * (1 - storage / max_capacity)  # Logistic Growth
        storage += growth
        storage_list.append(storage)

    return storage_list


st.set_page_config(page_title="Cloud Storage Growth Model", layout="centered")

st.title("☁️ Corporate Cloud Storage Growth Simulator")
st.write("Model: Exponential + Logistic Growth")

# Sidebar Inputs
st.sidebar.header("⚙️ Input Parameters")

initial_storage = st.sidebar.slider("Initial Storage Used (TB)", 10, 500, 50)
growth_rate = st.sidebar.slider("Growth Rate", 0.01, 0.5, 0.1)
max_capacity = st.sidebar.slider("Maximum Storage Capacity (TB)", 500, 5000, 1000)
days = st.sidebar.slider("Simulation Days", 30, 365, 180)

# Overview
st.markdown("""
## 📌 Project Overview

This model predicts **corporate cloud storage usage** over time using:

- 📈 Exponential Growth (initial phase)
- 📊 Logistic Growth (capacity-limited phase)

It helps in:

- Forecasting storage needs  
- Planning infrastructure expansion  
- Avoiding over-utilization  
""")

# Simulation
storage_data = simulate_storage(initial_storage, growth_rate, max_capacity, days)

# Graph
st.subheader("📈 Storage Growth Over Time")

fig, ax = plt.subplots()
ax.plot(range(days), storage_data)
ax.set_xlabel("Days")
ax.set_ylabel("Storage Used (TB)")
st.pyplot(fig)

# Data Table
st.subheader("📊 Storage Data Table")

df = pd.DataFrame({
    "Day": list(range(days)),
    "Storage Used (TB)": np.round(storage_data, 2)
})

st.dataframe(df, use_container_width=True)

# Insights
current_storage = storage_data[-1]
utilization = current_storage / max_capacity

st.subheader("🔍 Key Insights")

col1, col2 = st.columns(2)

with col1:
    st.info(f"""
📊 Current Storage Used  
{current_storage:.2f} TB
""")

with col2:
    st.info(f"""
⚙️ Utilization Ratio  
{utilization:.2f}
""")

# Interpretation
if utilization < 0.5:
    status = "Low Usage"
elif utilization < 0.8:
    status = "Optimal Usage"
elif utilization < 1:
    status = "High Usage"
else:
    status = "Overloaded"

st.success(f"""
💡 Interpretation:

• Utilization < 0.5 → Low usage  
• 0.5 - 0.8 → Optimal  
• 0.8 - 1 → High load  
• >1 → Capacity exceeded  

Current status: **{status}**
""")

# Expansion Suggestion
st.subheader("🚀 Expansion Planning")

if utilization > 0.8:
    st.warning("⚠️ Storage nearing capacity. Consider upgrading infrastructure.")
elif utilization > 1:
    st.error("🚨 Storage exceeded capacity! Immediate expansion required.")
else:
    st.success("✅ Storage capacity is sufficient.")

# Mathematical Model
st.subheader("📘 Mathematical Model")

st.latex(r"S(t+1) = S(t) + r \cdot S(t) \cdot \left(1 - \frac{S(t)}{K} \right)")

st.markdown("""
**Where:**

• S(t) = Storage at time t  
• r = Growth rate  
• K = Maximum storage capacity  
""")

# Conclusion
st.subheader("📌 Conclusion")

st.write(f"""
🔹 Storage grows rapidly initially (Exponential phase)  

🔹 Growth slows as it approaches capacity (Logistic phase)  

🔹 Final Storage: **{current_storage:.2f} TB**  

🔹 Capacity Limit: **{max_capacity} TB**  

🔹 System Status: **{status}**

👉 This model helps organizations plan storage upgrades efficiently.
""")