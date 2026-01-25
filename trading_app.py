import streamlit as st
import pandas as pd
import plotly.express as px

# Set page configuration
st.set_page_config(page_title="Trader Behavior vs. Sentiment", layout="wide")

st.title("Trader Behavior Insights vs. Bitcoin Sentiment")
st.markdown("Exploring how Fear & Greed indices influence trader performance and volume.")

# Data Loading 
@st.cache_data
def load_data():
    # Load the datasets
    sentiment_df = pd.read_csv(r"C:\Users\hiyas\OneDrive\Desktop\CODING\fear_greed_index.csv")
    trades_df = pd.read_csv(r"C:\Users\hiyas\OneDrive\Desktop\CODING\historical_data.csv")
    
    # Preprocessing: Convert dates to standard format
    # Trades data uses Timestamp IST: 'dd-mm-yyyy HH:MM'
    trades_df['date_only'] = pd.to_datetime(trades_df['Timestamp IST'], format='%d-%m-%Y %H:%M').dt.date
    
    # Sentiment data uses date: 'YYYY-MM-DD'
    sentiment_df['date_only'] = pd.to_datetime(sentiment_df['date']).dt.date
    
    # Ensure numeric columns are clean
    trades_df['Closed PnL'] = pd.to_numeric(trades_df['Closed PnL'], errors='coerce').fillna(0)
    trades_df['Size USD'] = pd.to_numeric(trades_df['Size USD'], errors='coerce').fillna(0)
    
    # Merge datasets on date
    merged_df = pd.merge(trades_df, sentiment_df[['date_only', 'classification', 'value']], 
                         on='date_only', how='inner')
    
    return merged_df

# Load the merged data
try:
    df = load_data()
    
    # Key Metrics Sidebar
    st.sidebar.header("Filter Data")
    coins = st.sidebar.multiselect("Select Coins", options=df['Coin'].unique(), default=df['Coin'].unique()[:5])
    filtered_df = df[df['Coin'].isin(coins)] if coins else df

    # High-Level Insights
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Trades", f"{len(filtered_df):,}")
    col2.metric("Total PnL (USD)", f"${filtered_df['Closed PnL'].sum():,.2f}")
    col3.metric("Avg Trade Size", f"${filtered_df['Size USD'].mean():,.2f}")

    # Visualizations
    st.divider()
    
    # Trade Count by Sentiment
    st.subheader("Activity: Trade Count by Market Sentiment")
    sentiment_counts = filtered_df['classification'].value_counts().reset_index()
    sentiment_counts.columns = ['Sentiment', 'Trade Count']
    fig1 = px.bar(sentiment_counts, x='Sentiment', y='Trade Count', 
                 color='Sentiment', template="plotly_white")
    st.plotly_chart(fig1, use_container_width=True)

    # Profitability by Sentiment
    st.subheader("Performance: Average PnL across Sentiment")
    pnl_by_sentiment = filtered_df.groupby('classification')['Closed PnL'].mean().reset_index()
    fig2 = px.box(filtered_df, x='classification', y='Closed PnL', 
                 color='classification', title="PnL Distribution (Whiskers: Outliers removed for clarity)")
    fig2.update_yaxes(range=[-500, 500]) # Zoom in on the bulk of the data
    st.plotly_chart(fig2, use_container_width=True)

    # Trade Size vs Sentiment
    st.subheader("Risk: Average Trade Size (USD)")
    size_by_sentiment = filtered_df.groupby('classification')['Size USD'].mean().reset_index()
    fig3 = px.line(size_by_sentiment, x='classification', y='Size USD', markers=True)
    st.plotly_chart(fig3, use_container_width=True)

    # Raw Data Preview
    if st.checkbox("Show Raw Merged Data"):
        st.write(filtered_df.head(100))

except Exception as e:
    st.error(f"Error loading files: {e}")
    st.info("Please ensure 'fear_greed_index.csv' and 'historical_data.csv' are in the same folder as this script.")