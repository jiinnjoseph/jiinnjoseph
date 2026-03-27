import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="EV Dashboard", layout="wide")

# ---------------- CUSTOM CSS ----------------
st.markdown("""
    <style>
    body {
        background-color: #0E1117;
        color: white;
    }
    .main {
        background-color: #0E1117;
    }
    .stMetric {
        background-color: #1E1E2F;
        padding: 15px;
        border-radius: 12px;
        box-shadow: 0px 0px 10px rgba(0,0,0,0.5);
    }
    h1, h2, h3 {
        color: #00FFD1;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.title("⚡ EV Charging Dashboard")
st.caption("Modern EV analytics dashboard")

# ---------------- LOAD DATA ----------------
@st.cache_data
def load_data():
    return pd.read_csv("Ev.csv")

data = load_data()

# ---------------- SIDEBAR ----------------
st.sidebar.header("⚙️ Filters")
zones = st.sidebar.multiselect(
    "Select Zones",
    options=data["city_zone"].unique(),
    default=data["city_zone"].unique()
)

filtered = data[data["city_zone"].isin(zones)]

# ---------------- GROUP ----------------
grouped = filtered.groupby("city_zone")["vehicles_charged"].mean()

# ---------------- METRICS ----------------
col1, col2, col3 = st.columns(3)

col1.metric("📊 Total Records", len(filtered))
col2.metric("📍 Zones", len(grouped))
col3.metric("⚡ Avg Vehicles", round(grouped.mean(), 2))

# ---------------- BAR CHART ----------------
st.subheader("📊 EV Usage by Zone")

fig, ax = plt.subplots()
ax.bar(grouped.index, grouped.values)
ax.set_facecolor("#1E1E2F")
fig.patch.set_facecolor("#0E1117")

ax.set_xlabel("Zones", color="white")
ax.set_ylabel("Vehicles", color="white")
ax.tick_params(colors='white')

st.pyplot(fig)

# ---------------- LINE CHART ----------------
st.subheader("📈 Trend Analysis")

fig2, ax2 = plt.subplots()
ax2.plot(grouped.index, grouped.values, marker='o')
ax2.set_facecolor("#1E1E2F")
fig2.patch.set_facecolor("#0E1117")

ax2.set_xlabel("Zones", color="white")
ax2.set_ylabel("Vehicles", color="white")
ax2.tick_params(colors='white')

st.pyplot(fig2)

# ---------------- DATA ----------------
with st.expander("🔍 View Data"):
    st.dataframe(filtered)

# ---------------- FOOTER ----------------
st.markdown("---")
st.caption("🚀 Built with Streamlit | EV Analytics Dashboard")
