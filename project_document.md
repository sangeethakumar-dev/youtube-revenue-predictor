# **MINI PROJECT REPORT**

## **Project Title**

**Content Monetization Modeler**

---

## **Domain**

Social Media Analytics

---

## **Abstract**

With the rapid growth of digital platforms, content creators increasingly rely on YouTube for revenue generation. Predicting ad revenue is crucial for optimizing content strategies and business planning. This project focuses on building a machine learning model using regression techniques to estimate YouTube ad revenue based on video performance and contextual features. The solution also includes an interactive Streamlit web application to demonstrate predictions and insights.

---

## **Problem Statement**

As video creators and media companies increasingly rely on platforms like YouTube for income, predicting potential ad revenue becomes essential for business planning and content strategy.

The objective of this project is to:

* Build a regression model to predict YouTube ad revenue.
* Use video performance metrics and contextual data as input features.
* Deploy the model through a simple and interactive Streamlit web application.

---

## **Business Use Cases**

* **Content Strategy Optimization:** Identify which content type generates higher revenue.
* **Revenue Forecasting:** Predict expected income from future uploads.
* **Creator Support Tools:** Provide insights for creators using analytics platforms.
* **Ad Campaign Planning:** Help advertisers estimate ROI based on performance data.

---

## **Dataset Description**

* **Dataset Name:** YouTube Monetization Modeler
* **Format:** CSV
* **Size:** ~122,000 rows
* **Source:** Synthetic dataset (created for learning purposes)

### **Target Variable**

* `ad_revenue_usd`

### **Features**

* `video_id`: Unique identifier
* `date`: Upload/report date
* `views, likes, comments`: Performance metrics
* `watch_time_minutes, video_length_minutes`: Engagement metrics
* `subscribers`: Channel size
* `category, device, country`: Contextual features

---

## **Data Preprocessing**

* Handled ~5% missing values using appropriate imputation techniques.
* Removed duplicate records (~2%).
* Encoded categorical variables (`category`, `device`, `country`).
* Scaled numerical features where required.
* Detected and treated outliers to improve model performance.

---

## **Exploratory Data Analysis (EDA)**

* Analyzed distribution of numerical features.
* Identified correlations between engagement metrics and revenue.
* Detected outliers and anomalies.
* Visualized trends using plots and charts.

---

## **Feature Engineering**

* Created multiple new features to enhance model performance:
* Engagement Rate = (likes + comments) / views
* Comment Rate = comments / views
* Watch Time per View = watch_time_minutes / views
* Performed feature evaluation and analysis:
* Identified that Comment Rate and Watch Time per View introduced noise and  reduced model performance.
* These features were dropped after experimentatin

Final feature used:
 Engagement Rate (retained due to strong relevance with revenue)
Transformed features where necessary to improve model learning.
---

## **Model Building**

Multiple regression models were experimented with:

Linear Regression
Ridge Regression
Lasso Regression
Random Forest Regressor
Gradient Boosting Regressor

The models were trained and compared to identify the best-performing one.

## **Final Model

* Linear Regression performed best with around 95% R² on both train and test data, and I selected it because it is highly interpretable, allowing me to understand which features influence ad revenue the most.

## **Model Evaluation**

The performance of models was evaluated using:

* **R² Score**
* **Root Mean Squared Error (RMSE)**
* **Mean Absolute Error (MAE)**

The final model was selected based on overall performance and generalization capability.

---

## **Streamlit Application**

A basic interactive web application is being developed to:

* Accept user inputs (video metrics)
* Predict ad revenue in real-time
* Display insights and visualizations

*(Note: Development in progress and will be completed before final evaluation.)*

---

## **Results**

* Built a regression model capable of predicting ad revenue.
* Processed and cleaned a large dataset.
* Generated insights on factors influencing YouTube revenue.
* Developed (in progress) a Streamlit application for real-time predictions.

---

## **Technical Stack**

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib / Seaborn
* Streamlit

---

## **Key Learnings**

* Regression modeling and evaluation
* Data preprocessing and feature engineering
* Handling missing values and outliers
* Exploratory Data Analysis (EDA)
* Building end-to-end ML pipelines
* Deploying models using Streamlit

---

## **Project Deliverables**

* Jupyter Notebook (EDA & Feature Engineering) ✅
* Model Building Notebook (In Progress)
* Streamlit Application (In Progress)
* Final Project Report
* README Documentation

---

## **Future Improvements**

* Hyperparameter tuning for better accuracy
* Use advanced models like XGBoost
* Improve Streamlit UI/UX
* Deploy application online

---

## **Conclusion**

This project successfully demonstrates how machine learning can be used to predict YouTube ad revenue using video performance data. It provides valuable insights for content creators and businesses, enabling better decision-making and strategy optimization.

---

## **Author**

**Sangeetha S**

---
