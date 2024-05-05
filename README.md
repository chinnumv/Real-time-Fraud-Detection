# Fraud Detection and Anomaly Detection Pipeline

## Overview
This Python code demonstrates a pipeline for fraud detection and anomaly detection using machine learning techniques. It combines multiple models including Isolation Forest for anomaly detection, Decision Tree Classifier, and KMeans clustering to identify fraudulent activities in a dataset.

## Requirements

- Python 3.x
- NumPy library
- pandas library
- scikit-learn library

## Usage

1. Data Preparation:
Replace "your_data.csv" with the path to your actual dataset containing features related to payments, user behavior, and course enrollments. Ensure that the dataset is loaded into a DataFrame named 'data' with columns representing features and a column 'is_fraudulent' indicating whether each observation is fraudulent or not.
2. Model Training:
Separate the data into features (X) and the target variable (y).
Train models for anomaly detection, decision tree classification, and KMeans clustering using the provided data.
3. Combining Results:
Combine the results from the anomaly detection, decision tree classification, and clustering models to identify potential fraudulent activities.
4. Evaluation:
Evaluate the combined model's performance using classification metrics such as precision, recall, and F1-score.
5. Sample Usage:
Predict fraud for new data by replacing "new_data.csv" with the path to the new dataset and using the combined model's predict method.

## Example

- The provided code assumes the existence of a DataFrame named 'data' containing features related to payments, user behavior, and course enrollments, as well as a column 'is_fraudulent' indicating whether each observation is fraudulent or not.
- It trains models for anomaly detection (Isolation Forest), decision tree classification, and KMeans clustering to identify potential fraudulent activities.
- The results from each model are combined, and the combined model's performance is evaluated using classification metrics.