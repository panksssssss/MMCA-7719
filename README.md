# ☁️ Cloud Storage Growth Model

A Streamlit-based simulation project to **predict corporate cloud storage usage** using a combination of **Exponential Growth** and **Logistic Growth** models.

---

## 🚀 Project Overview

This project helps organizations forecast how their cloud storage will grow over time and plan infrastructure accordingly.

### 🔍 Key Features

- 📈 Simulates storage growth over time  
- ⚙️ Adjustable parameters (growth rate, capacity, etc.)  
- 📊 Interactive graphs and data tables  
- 🚨 Storage utilization insights  
- 🚀 Expansion planning suggestions  

---

## 🧠 Model Used

The model combines:

- **Exponential Growth** → Rapid increase in early stage  
- **Logistic Growth** → Slows down as it reaches capacity  

### 📘 Formula

\[
S(t+1) = S(t) + r \cdot S(t) \cdot \left(1 - \frac{S(t)}{K} \right)
\]

Where:

- `S(t)` = Storage at time t  
- `r` = Growth rate  
- `K` = Maximum storage capacity  

---

## 🛠️ Tech Stack

- Python 🐍  
- Streamlit 🎈  
- NumPy  
- Pandas  
- Matplotlib  

---

## 📦 Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/cloud-storage-growth-model.git
cd cloud-storage-growth-model
