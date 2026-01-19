# 🇮🇳 Project Drishti: AI-Driven Service Triage for Aadhaar

![Status](https://img.shields.io/badge/Status-Prototype_Ready-success)
![Focus](https://img.shields.io/badge/Focus-GovTech_|_AI_Governance-blue)
![Privacy](https://img.shields.io/badge/Privacy-100%25_Compliant_(No_PII)-orange)

### The Problem
Currently, UIDAI's grievance redressal is **Reactive**. Problems in service delivery (e.g., high rejection rates in a specific district) are often identified only *after* citizens complain.

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
*(Upload a screenshot of your dashboard here showing Red/Green zones)*

### How to Run
```bash
git clone https://github.com/Codingflower20/Project-Drishti-UIDAI.git
pip install -r requirements.txt
python app.py
