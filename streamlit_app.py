import streamlit as st
import json
import pandas as pd
import os
import time

st.set_page_config(page_title="AI Gateway Dashboard", layout="wide")

st.title("🚀 AI Gateway Dashboard")

LOG_FILE = "logs.json"

# Auto refresh every 3 seconds
st.caption("Auto-refreshing every 3 seconds...")
time.sleep(1)

# Check if logs file exists
if not os.path.exists(LOG_FILE):
    st.warning("⚠️ logs.json not found. Run API first!")
    st.stop()

# Load logs
with open(LOG_FILE, "r") as f:
    logs = json.load(f)

if len(logs) == 0:
    st.warning("⚠️ No logs available yet!")
    st.stop()

# Convert to DataFrame
df = pd.DataFrame(logs)

# Reverse (latest first)
df = df[::-1]

# ===== METRICS =====
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Requests", len(df))
col2.metric("Cache Hits", len(df[df["cache"] == "hit"]))
col3.metric("Fast Model", len(df[df["model"] == "fast"]))
col4.metric("Capable Model", len(df[df["model"] == "capable"]))

st.divider()

# ===== FILTER =====
model_filter = st.selectbox(
    "Filter by Model",
    ["All", "fast", "capable", "cache"]
)

if model_filter != "All":
    df = df[df["model"] == model_filter]

# ===== TABLE =====
st.subheader("📜 Logs Table")
st.dataframe(df, use_container_width=True)

st.divider()

# ===== LATENCY GRAPH =====
st.subheader("⏱️ Latency Over Time")
st.line_chart(df["latency"])

# ===== CACHE GRAPH =====
st.subheader("🔁 Cache Usage")
st.bar_chart(df["cache"].value_counts())

# ===== MODEL USAGE =====
st.subheader("🤖 Model Distribution")
st.bar_chart(df["model"].value_counts())

st.success("✅ Dashboard running successfully!")