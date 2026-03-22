# YouTube Revenue Predictor

An end-to-end machine learning project that predicts YouTube ad revenue using regression models based on video performance and engagement metrics.

---

## Project Overview

This project aims to help content creators and media companies estimate potential revenue from YouTube videos. By analyzing performance metrics such as views, likes, comments, and engagement rates, the model predicts expected ad revenue.

---

## Features

* Exploratory Data Analysis (EDA)
* Data Cleaning and Preprocessing
* Feature Engineering (e.g., Engagement Rate)
* Multiple Regression Models
* Model Evaluation (R², RMSE, MAE)
* Streamlit Web Application for predictions

---

## Project Structure

```id="a1b2c3"
youtube-revenue-predictor/
│
├── data/                  # Dataset (CSV file)
├── notebooks/            # Jupyter notebooks (EDA & Model)
├── src/                  # Source code (optional)
├── app/                  # Streamlit application
├── models/               # Saved ML models
├── README.md             # Project documentation
└── requirements.txt      # Dependencies
```

---

## Dataset Information

* Name: YouTube Monetization Modeler
* Size: ~122,000 rows
* Target Variable: ad_revenue_usd

### Features:

* Video metrics: views, likes, comments
* Engagement metrics: watch time, video length
* Channel metrics: subscribers
* Contextual features: category, device, country

---

## Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* Matplotlib / Seaborn
* Streamlit

---

## Model Building

Multiple regression models were implemented and compared:

* Linear Regression
* Decision Tree Regressor
* Random Forest Regressor
* Gradient Boosting Regressor

The best model was selected based on evaluation metrics.

---

## Evaluation Metrics

* R² Score
* Root Mean Squared Error (RMSE)
* Mean Absolute Error (MAE)

---

## Streamlit Application

The application allows users to:

* Input video performance metrics
* Predict ad revenue
* View basic insights

(Currently under development)

---

## Installation

```bash id="install01"
git clone https://github.com/your-username/youtube-revenue-predictor.git
cd youtube-revenue-predictor
pip install -r requirements.txt
```

---

## Run the Application

```bash id="run01"
streamlit run app/app.py
```

---

## Project Status
The core components such as EDA and feature engineering have been completed. Model development and deployment using Streamlit are in progress.

## Future Improvements

* Hyperparameter tuning
* Advanced models such as XGBoost
* Improved UI/UX for Streamlit
* Deployment to cloud

---

## Author

Sangeetha S
