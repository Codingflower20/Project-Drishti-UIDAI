import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans

class DrishtiEngine:
    """
    Core Intelligence Engine for Project Drishti.
    Handles Data Ingestion, Feature Engineering (USR), and K-Means Clustering.
    """

    def __init__(self):
        # DOUBLE UNDERSCORES before and after 'init' are critical!
        self.scaler = MinMaxScaler()
        
        # EXPLAINABLE AI NOTE:
        # We use K-Means (k=3) instead of Neural Networks because government governance
        # requires interpretability. ROs need to know *why* a district is flagged.
        self.kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)

    def generate_synthetic_data(self, num_districts=750):
        """
        Generates DUMMY operational logs for demonstration purposes.
        Ensures strict privacy compliance (No PII).
        """
        np.random.seed(42)
        districts = [f"District_{i:03d}" for i in range(1, num_districts + 1)]
        
        data = {
            'District_ID': districts,
            'Total_Update_Requests': np.random.randint(1000, 50000, num_districts),
            'Successful_Updates': np.random.randint(500, 48000, num_districts),
            'Avg_Rejection_Rate': np.random.uniform(0.01, 0.35, num_districts), # 1% to 35%
            'Packet_Upload_Delay_Hrs': np.random.uniform(2, 72, num_districts)
        }
        
        df = pd.DataFrame(data)
        
        # Ensure Successful updates are never more than Total requests
        df['Successful_Updates'] = df.apply(
            lambda x: min(x['Successful_Updates'], x['Total_Update_Requests']), axis=1
        )
        return df

    def calculate_usr(self, df):
        """
        Calculates the UPDATE STRESS RATIO (USR).
        USR = (Total Requests / Success) * Rejection Velocity
        High USR = High Friction (Citizens stuck in loops).
        """
        # Avoid division by zero
        df['Success_Ratio'] = df['Successful_Updates'] / df['Total_Update_Requests'].replace(0, 1)
        
        # INVERT Success Ratio (Lower success = Higher stress)
        df['USR_Score'] = (1 / df['Success_Ratio']) * (1 + df['Avg_Rejection_Rate'])
        
        return df

    def run_triage_clustering(self, df):
        """
        Performs Unsupervised Learning to categorize districts.
        """
        # Features to cluster on
        features = ['USR_Score', 'Avg_Rejection_Rate', 'Packet_Upload_Delay_Hrs']
        
        # Normalize Data
        X_scaled = self.scaler.fit_transform(df[features])
        
        # Fit K-Means
        df['Cluster_Label'] = self.kmeans.fit_predict(X_scaled)
        
        # DYNAMIC LABELING (Critical vs Stable)
        # We cannot assume Cluster 0 is always "Good". We must check the mean USR.
        cluster_means = df.groupby('Cluster_Label')['USR_Score'].mean().sort_values()
        
        # Map clusters: Lowest Mean USR = Stable, Highest = Critical
        mapping = {}
        sorted_clusters = cluster_means.index.tolist()
        
        mapping[sorted_clusters[0]] = 'Stable'     # Green
        mapping[sorted_clusters[1]] = 'Watchlist'  # Orange
        mapping[sorted_clusters[2]] = 'Critical'   # Red
        
        df['Risk_Category'] = df['Cluster_Label'].map(mapping)
        return df