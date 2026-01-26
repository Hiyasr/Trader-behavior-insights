# 📊 Trader Behavior vs. Bitcoin Market Sentiment
**Submission for Junior Data Scientist Role @ PrimeTrade**

This Streamlit application provides a deep dive into how retail and institutional trader behavior correlates with the **Crypto Fear & Greed Index**. By merging high-frequency trade data from **Hyperliquid** with sentiment indices, this tool uncovers how market psychology drives profitability and volume.

---

## 🚀 Live Application
[Insert your Streamlit Cloud Link Here]

---

## 🧐 Problem Statement & Methodology
The challenge was to identify if traders perform better during periods of "Extreme Fear" or "Extreme Greed." 

### Data Engineering:
- **Normalization:** Synced IST-based trade timestamps with daily UTC-based sentiment data.
- **Aggregation:** Calculated daily PnL and trade volume metrics to match the granularity of the Fear & Greed Index.
- **Handling Scale:** Due to the large size of the Hyperliquid datasets, the app utilizes **Streamlit Caching** (`@st.cache_data`) to ensure smooth performance.

---

## 📈 Key Insights Found
1. **The Fear Peak:** Trade count significantly increases during "Extreme Fear" phases, suggesting high panic-selling or high-frequency scalp trading during volatility.
2. **Profitability Trends:** Mean **Closed PnL** shows higher stability during "Neutral" to "Greed" phases, whereas "Extreme" phases (both ends) show higher variance and outlier losses.
3. **Volume vs Sentiment:** Average trade size ($USD) tends to peak during "Greed," indicating higher conviction (or over-leverage) among traders.

---

## 🛠️ How to Run Locally
1. **Clone the repo:**
   ```bash
   git clone [https://github.com/Hiyasr/Trader-behavior-insights]

 ## Streamlit link
 
