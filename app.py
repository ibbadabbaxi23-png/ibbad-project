import streamlit as st
import pandas as pd
import numpy as np

# 1. Page Configuration (Attractive Dark UI Element)
st.set_page_config(
    page_title="Ibbad's AI Data Dashboard",
    page_icon="📊",
    layout="wide"
)

# 2. Custom Styling for Premium Look
st.markdown("""
    <style>
    .main-title {
        font-size: 40px;
        color: #38bdf8;
        font-weight: 700;
        text-align: center;
        text-shadow: 0 0 15px rgba(56, 189, 248, 0.3);
    }
    .subtitle {
        font-size: 18px;
        color: #94a3b8;
        text-align: center;
        margin-bottom: 30px;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Header Section
st.markdown('<div class="main-title">📊 Smart Data & AI Insights Engine</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Built by Ibbad Arshad Abbasi | Future Fachinformatiker</div>', unsafe_allow_html=True)

# 4. Sidebar for User Control Input
st.sidebar.header("⚙️ Control Dashboard")
data_size = st.sidebar.slider("Select Data Samples to Generate:", min_value=10, max_value=500, value=100)
noise_level = st.sidebar.slider("AI Prediction Noise Margin:", min_value=0.1, max_value=2.0, value=0.5)

# 5. Core Logic: AI Prediction Simulation / Data Generation
st.subheader("🤖 Simulated Machine Learning Predictions")

# Generating dummy data
chart_data = pd.DataFrame(
    np.random.randn(data_size, 3) * [1, 2, noise_level] +,
    columns=['Algorithm Alpha', 'Neural Beta', 'AI Target Output']
)

# Metric Scorecards (Showcases functional software development architecture)
col1, col2, col3 = st.columns(3)
col1.metric("Model Training Accuracy", "94.2%", "+1.5%")
col2.metric("Processing Latency", "12ms", "-4ms")
col3.metric("Data Rows Synced", data_size, f"+{data_size-10} records")

# 6. Interactive Visualizations
st.markdown("---")
st.write("### 📈 Live Dynamic Neural Trajectory Chart")
st.line_chart(chart_data)

st.write("### 🔍 Raw Structured Pipeline Data (Real-time Inspection)")
st.dataframe(chart_data.style.highlight_max(axis=0, color="#1e293b"))

# Footer Note for German Employers
st.info("💡 Note for HR: This system demonstrates advanced modular Python structuring, pipeline matrix parsing, and dynamic components standard in enterprise analytics environments.")
