# Telecom-Churn-Analysis

## 📌 Project Overview
This project focuses on predicting customer churn in the telecom industry using **machine learning**. The goal is to analyze key factors contributing to churn and develop a model for proactive customer retention strategies.

## 📑 Contents
1. **Business Problem Statement**
2. **Objective**
3. **Data Summary**
4. **Exploratory Data Analysis (EDA)**
5. **Feature Engineering & Model Building**
6. **Model Evaluation & Deployment**
7. **Recommendations & Conclusion**

## 🎯 Business Problem Statement
Customer churn impacts revenue and retention in telecom services. This project aims to identify potential churners and mitigate risks with actionable insights.

## 🔍 Objective
- **Maximize** customer retention.
- **Minimize** churn by identifying root causes.
- **Provide actionable insights** for business improvements.

## 📊 Data Summary
The dataset consists of telecom customer records with features such as:
- **Demographics** (e.g., state, area code)
- **Subscription details** (e.g., international plan, voicemail plan)
- **Usage metrics** (e.g., call minutes, charges, customer service calls)
- **Target Variable:** **‘Churn’** (Yes/No)

### Data Preprocessing
- Handled **missing values** (e.g., mean imputation for numerical columns).
- Checked **duplicates** and adjusted data types.

## 📈 Exploratory Data Analysis (EDA)
### Key Findings:
- **42% churn rate** among **international plan users**.
- **Higher churn when voicemail messages > 20**.
- **60% churn rate** for customers with **>5 service calls**.
- **High churn in 10 states** due to poor network coverage.
- **International call charges significantly impact churn**.

## 🛠 Feature Engineering & Model Building
- **Outlier Handling:** Used **IQR method**.
- **Feature Selection:** Used **Random Forest feature importance**.
- **Data Balancing:** Applied **SMOTE & Under-sampling**.
- **Model Training:** Evaluated multiple models, including:
  - Logistic Regression
  - Decision Trees
  - Random Forest
  - Gradient Boosting (XGBoost, LightGBM)

## 📊 Model Evaluation & Deployment
- **Best Model:** Selected based on **accuracy, precision, recall, and F1-score**.
- **Deployment:** Implemented using **Streamlit** for real-time predictions.

## 🏆 Recommendations
1. Improve network coverage in high-churn states.
2. Offer tailored discounts for **international plan users**.
3. Enhance voicemail quality & gather user feedback.
4. Prioritize customer service improvements to reduce excessive calls.
5. Provide better plans for high-usage customers.

## 📜 Conclusion
- High churn among **international plan users and frequent service callers**.
- **Expensive international charges** contribute to customer loss.
- The predictive model helps **identify potential churners early**, allowing telecom providers to act proactively.

---
📌 **Star this repository if you find it useful!**

