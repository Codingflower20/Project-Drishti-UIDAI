import streamlit as st
import pandas as pd
import plotly.express as px
from triage_engine import DrishtiEngine

# --- PAGE CONFIGURATION (Must be first) ---
st.set_page_config(
    page_title="Project Drishti | UIDAI Triage",
    page_icon="🇮🇳",
    layout="wide"
)

# --- CUSTOM CSS FOR GOVERNMENT BRANDING ---
st.markdown("""
    <style>
    .main {
        background-color: #F5F7FA;
    }
    .metric-card {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #003366;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
    }
    h1, h2, h3 {
        color: #003366;
        font-family: 'Helvetica', sans-serif;
    }
    .stAlert {
        border-radius: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- INITIALIZE ENGINE ---
@st.cache_data
def load_data():
    engine = DrishtiEngine()
    df = engine.generate_synthetic_data()
    df = engine.calculate_usr(df)
    df = engine.run_triage_clustering(df)
    return df

data = load_data()

# --- SIDEBAR ---
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/en/thumb/c/cf/Aadhaar_Logo.svg/1200px-Aadhaar_Logo.svg.png", width=150)
    st.header("Control Panel")
    st.info("*Project Drishti* uses Unsupervised AI to detect operational friction before grievances escalate.")
    
    st.markdown("---")
    region_filter = st.selectbox("Select Region (RO)", ["All India", "RO Delhi", "RO Bangalore", "RO Mumbai"])
    
    st.markdown("### 🔒 Privacy Mode")
    st.caption("All data processed is aggregated metadata. No PII used.")

# --- MAIN DASHBOARD ---
st.title("🇮🇳 Project Drishti: Service Triage Dashboard")
st.markdown("### Real-time Operational Stress Detection Framework")

# KPI ROW
col1, col2, col3, col4 = st.columns(4)

total_districts = len(data)
critical_count = len(data[data['Risk_Category'] == 'Critical'])
watchlist_count = len(data[data['Risk_Category'] == 'Watchlist'])
avg_usr = round(data['USR_Score'].mean(), 2)

with col1:
    st.metric("Total Districts Monitored", total_districts)
with col2:
    st.metric("CRITICAL ZONES (Action Req)", critical_count, delta_color="inverse")
with col3:
    st.metric("Watchlist Zones", watchlist_count)
with col4:
    st.metric("Avg. Update Stress Ratio", avg_usr)

st.markdown("---")

# --- THE KILLER GRAPH (Visual Proof of Concept) ---
col_graph, col_list = st.columns([2, 1])

with col_graph:
    st.subheader("🔍 AI Risk Clustering (K-Means)")
    st.markdown("Visualizing the correlation between *Rejection Rate* and *Update Stress Ratio*.")
    
    # Define Color Map
    color_map = {
        'Stable': '#00CC96',     # Green
        'Watchlist': '#FFA15A',  # Orange
        'Critical': '#EF553B'    # Red
    }
    
    fig = px.scatter(
        data, 
        x="Avg_Rejection_Rate", 
        y="USR_Score", 
        color="Risk_Category",
        color_discrete_map=color_map,
        hover_data=["District_ID", "Packet_Upload_Delay_Hrs"],
        size="Total_Update_Requests", # Bubble size = Volume
        size_max=20,
        title="District Risk Stratification (Bubble Size = Update Volume)"
    )
    fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
    st.plotly_chart(fig, use_container_width=True)

with col_list:
    st.subheader("🚨 Priority Action List")
    st.markdown("Top 10 High-Friction Districts")
    
    critical_df = data[data['Risk_Category'] == 'Critical'].sort_values(by='USR_Score', ascending=False).head(10)
    
    st.dataframe(
        critical_df[['District_ID', 'USR_Score', 'Avg_Rejection_Rate']],
        hide_index=True,
        column_config={
            "USR_Score": st.column_config.ProgressColumn("Stress Level", format="%.2f", min_value=0, max_value=4),
            "Avg_Rejection_Rate": st.column_config.NumberColumn("Rejection %", format="%.2f")
        }
    )
