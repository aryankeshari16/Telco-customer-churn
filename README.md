# 📊 Customer Churn Prediction — Telecom Industry

Welcome to my **Customer Churn Prediction** project, where I tackled a real-world business challenge using **Machine Learning**. The goal was to predict whether a customer will **stay or leave (churn)** based on their usage behavior and service-related features.

---

## 📁 Project Overview

- **Domain**: Telecom Industry  
- **Problem Statement**: Predict if a customer will churn based on their profile and service usage.  
- **Type**: Binary Classification  
- **Toolkits Used**: Python, Pandas, Scikit-learn, Matplotlib, Seaborn  

---

## 🧠 Approach

1. **Data Exploration & Cleaning**  
   - Handled missing values  
   - Discovered major churn contributors (e.g., high monthly bills, service dissatisfaction)

2. **Feature Engineering**  
   - Applied **One-Hot Encoding** to handle categorical variables  
   - Visualized churn impact using heatmaps and bar charts  

3. **Data Splitting**  
   - Used `train_test_split()` to split data for training and evaluation

4. **Modeling with Decision Tree**  
   - Chose **Decision Tree Classifier** for interpretability  
   - Applied **Pre-Pruning Techniques**  
     - `max_depth`, to avoid overfitting

5. **Evaluation**  
   - Used **Confusion Matrix**, **Accuracy**, **Precision**, and **Recall** for performance check  
   - Insights: High accuracy achieved with balanced precision and recall

6. **Prediction**  
   - Created a simple interface for predicting churn from input features  

---

## 📌 Key Findings

- Customers with **high monthly charges** and **multiple services** tend to churn more  
- **Tenure** plays a vital role — newer customers churn more  
- **Contract type** and **Paperless Billing** strongly influence churn  

---

## 🛠️ Tech Stack

| Tool | Description |
|------|-------------|
| Python | Main programming language |
| Pandas | Data manipulation |
| Scikit-learn | ML algorithms and preprocessing |
| Matplotlib & Seaborn | Data visualization |
| Jupyter Notebook | Interactive development |

---

## 📈 Confusion Matrix Snapshot
Confusion matrix:
[[939  97]
 [180 193]]

Classification Report:
              precision    recall  f1-score   support

       False       0.84      0.91      0.87      1036
        True       0.67      0.52      0.58       373

    accuracy                           0.80      1409
   macro avg       0.75      0.71      0.73      1409
weighted avg       0.79      0.80      0.79      1409

---
