# 🇮🇳 Project Drishti: AI-Driven Service Triage for Aadhaar

![Status](https://img.shields.io/badge/Status-Prototype_Ready-success)
![Focus](https://img.shields.io/badge/Focus-GovTech_|_AI_Governance-blue)
![Privacy](https://img.shields.io/badge/Privacy-100%25_Compliant_(No_PII)-orange)

## The Challenge: "Invisible Friction"
Currently, the grievance redressal mechanism is **Reactive**.
1.  **Latency:** Operational issues (e.g., a specific district having high biometric rejection rates) are often detected only *after* thousands of citizens file complaints.
2.  **Blind Spots:** Regional Offices (ROs) lack a real-time, consolidated view of "Operational Stress" across their 700+ districts.
### The Solution
**Project Drishti** is a proactive triage framework. It uses **Unsupervised Learning (K-Means)** to analyze operational logs and flag high-stress districts *before* they become hotspots for grievances.

---

### Key Innovations
1.  **Update Stress Ratio (USR):** A proprietary metric that detects "Citizen Loops" (repeated failed updates).
2.  **Dynamic Risk Zoning:** Automatically classifies districts into **Stable**, **Watchlist**, or **Critical**.
3.  **Privacy-First Architecture:** The model runs entirely on aggregated district-level metadata. No resident PII is touched.

### Tech Stack
-   **Core Logic:** Python, Scikit-Learn (K-Means Clustering)
-   **Data Processing:** Pandas, NumPy
-   **Visualization:** Streamlit (Dashboard), Matplotlib
-   **Deployment:** Dockerized container (Ready for UIDAI Private Cloud)

### Snapshots
![](/assets/LoginPage)
![](/assets/Screenshot)

### How to Run
```bash
git clone https://github.com/Codingflower20/Project-Drishti-UIDAI.git
pip install -r requirements.txt
python app.py
