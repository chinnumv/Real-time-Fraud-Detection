import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest, RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.cluster import KMeans
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report

# Sample data (replace with your actual data)
# Assume you have a DataFrame named 'data' containing features related to payments, user behavior, and course enrollments
# and a column 'is_fraudulent' indicating whether each observation is fraudulent or not
data = pd.read_csv("data.csv")

# Separate features and target variable
X = data.drop(columns=['is_fraudulent'])
y = data['is_fraudulent']

# Anomaly Detection using Isolation Forest
anomaly_detector = IsolationForest(contamination=0.05)
anomaly_detector.fit(X)

# Decision Tree Classifier
decision_tree = DecisionTreeClassifier()
decision_tree.fit(X, y)

# Clustering using KMeans
kmeans = KMeans(n_clusters=2)
kmeans.fit(X)
clusters = kmeans.predict(X)

# Combine results from Anomaly Detection, Decision Tree, and Clustering
combined_predictions = (anomalies == -1) | (decision_tree.predict(X) == 1) | (clusters == 1)

# Evaluate the combined model
print("Classification Report:")
print(classification_report(y, combined_predictions))

# Sample usage: Predict fraud for new data
# new_data = pd.read_csv("new_data.csv")
# new_predictions = combined_model.predict(new_data)
