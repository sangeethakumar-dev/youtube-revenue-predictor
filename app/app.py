import streamlit as st
import pandas as pd
import joblib
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.markdown("""
<style>

/* 🌈 Background for all pages */
.stApp {
    background: linear-gradient(to bottom right, #fff5f5, #ffecec);
}

/* 🧠 Main font */
html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

/* 🔥 Title - Mini Project */
.main-title {
    font-family: 'Montserrat', sans-serif;
    font-size: 52px;
    text-align: center;
    font-weight: 800;
    color: #111;
}

/* 🎯 Subtitle */
.sub-title {
    text-align: center;
    font-size: 26px;
    color: #555;
    margin-bottom: 20px;
}

/* 🔽 Dropdown center */
div[data-baseweb="select"] {
    max-width: 300px;
    margin: auto;
}

/* 💳 Cards */
.card {
    background-color: white;
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0px 6px 18px rgba(0,0,0,0.1);
}

/* 🔴 Button */
.stButton>button {
    background-color: #FF0000;
    color: white;
    border-radius: 10px;
    height: 50px;
    font-size: 18px;
}

</style>
""", unsafe_allow_html=True)

# =======================
# CONFIG
# =======================
st.set_page_config(page_title="YouTube Revenue Predictor", layout="centered")

model = joblib.load('model_pipeline.pkl')

# =======================
# 🎨 PREMIUM FONT + STYLE
# =======================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;500;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

.title {
    text-align: center;
    font-size: 42px;
    font-weight: 700;
}

.subtitle {
    text-align: center;
    font-size: 22px;
    color: gray;
}

.card {
    background-color: #f9f9f9;
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0px 5px 15px rgba(0,0,0,0.1);
    margin-top: 20px;
}

.stButton>button {
    background-color: #FF0000;
    color: white;
    border-radius: 10px;
    height: 50px;
    width: 100%;
    font-size: 18px;
}
</style>
""", unsafe_allow_html=True)

# =======================
# 🧭 PAGE NAVIGATION
# =======================
if "page" not in st.session_state:
    st.session_state.page = "home"

# =======================
# 🏠 HOME PAGE
# =======================
if st.session_state.page == "home":

    st.markdown('<div class="main-title">Mini Project - 3</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">Content Monetization Modeler</div>', unsafe_allow_html=True)

    # 🔽 Dropdown BEFORE logo
    option = st.selectbox("", ["Select", "EDA Visualization", "Prediction"])

    if option == "EDA Visualization":
        st.session_state.page = "eda"
        st.rerun()

    elif option == "Prediction":
        st.session_state.page = "predict"
        st.rerun()

    st.markdown("<br><br><br>", unsafe_allow_html=True)

    # 📺 BIG LOGO (FULL WIDTH)
    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/b/b8/YouTube_Logo_2017.svg",
        use_container_width=True
    )
# =======================
# 📊 EDA PAGE
# =======================
elif st.session_state.page == "eda":

    col1, col2, col3 = st.columns([2, 6, 1])

# LEFT → Back button
    with col1:
        st.button("⬅ Back", on_click=lambda: st.session_state.update(page="home"))

# CENTER → YouTube logo
    with col2:
        st.markdown(
        """
        <div style='text-align: center;'>
            <img src="https://upload.wikimedia.org/wikipedia/commons/b/b8/YouTube_Logo_2017.svg" width="200">
        </div>
        """,
        unsafe_allow_html=True
        )

# RIGHT → empty (just for spacing)
    with col3:
        st.write("")

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
    "<h1 style='text-align: center;'>Data Analysis Dashboard</h1>",
    unsafe_allow_html=True
    )

    df = pd.read_csv('../data/youtube_df_cleaned (3).csv')

    eda_type = st.radio("Choose Analysis Type", ["Univariate", "Bivariate"])

    # =======================
    # UNIVARIATE
    # =======================
    if eda_type == "Univariate":

        st.subheader("Distribution of Revenue")
        fig, ax = plt.subplots()
        sns.histplot(df['ad_revenue_usd'], bins=30, kde=True, ax=ax)
        st.pyplot(fig)

        st.subheader("Watch Time Boxplot")
        fig, ax = plt.subplots()
        sns.boxplot(x=df['watch_time_minutes'], ax=ax)
        st.pyplot(fig)

        st.subheader("Feature Distributions")
        for col in ['views', 'watch_time_minutes', 'engagement_rate']:
            fig, ax = plt.subplots()
            sns.histplot(df[col], kde=True, ax=ax)
            st.pyplot(fig)

    # =======================
    # BIVARIATE
    # =======================
    elif eda_type == "Bivariate":

        st.subheader("Correlation Heatmap")
        fig, ax = plt.subplots(figsize=(8,5))
        sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm", ax=ax)
        st.pyplot(fig)

        st.subheader("Views vs Revenue")
        fig, ax = plt.subplots()
        sns.scatterplot(x='views', y='ad_revenue_usd', data=df, ax=ax)
        st.pyplot(fig)

        st.subheader("Watch Time vs Revenue")
        fig, ax = plt.subplots()
        sns.scatterplot(x='watch_time_minutes', y='ad_revenue_usd', data=df, ax=ax)
        st.pyplot(fig)

        st.subheader("Engagement Rate vs Revenue")
        fig, ax = plt.subplots()
        sns.scatterplot(x='engagement_rate', y='ad_revenue_usd', data=df, ax=ax)
        st.pyplot(fig)

# =======================
# 🎯 PREDICTION PAGE
# =======================
elif st.session_state.page == "predict":

    col1, col2, col3 = st.columns([2, 6, 1])

# LEFT → Back button
    with col1:
        st.button("⬅ Back", on_click=lambda: st.session_state.update(page="home"))

# CENTER → YouTube logo
    with col2:
        st.markdown(
        """
        <div style='text-align: center;'>
            <img src="https://upload.wikimedia.org/wikipedia/commons/b/b8/YouTube_Logo_2017.svg" width="200">
        </div>
        """,
        unsafe_allow_html=True
        )

# RIGHT → empty (just for spacing)
    with col3:
        st.write("")

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
    "<h1 style='text-align: center;'>Data Analysis Dashboard</h1>",
    unsafe_allow_html=True
    )


    views = st.text_input("Views")
    likes = st.text_input("Likes")
    comments = st.text_input("Comments")

    if st.button("Predict Revenue"):

        if views and likes and comments:

            views = float(views)
            likes = float(likes)
            comments = float(comments)

            # ⚠️ Validation
            if comments > views:
                st.warning("⚠️ Comments exceed views (rare case)")

            # Feature Engineering
            engagement_rate = (likes + comments) / views if views > 0 else 0
            watch_time = views * 3

            # Explanation
            st.info(f"""
            Engagement Rate = (Likes + Comments) / Views = {engagement_rate:.4f}  
            Watch Time = Views × Avg Duration (3 min) = {watch_time:.0f}
            """)

            input_data = pd.DataFrame({
                'views': [views],
                'likes': [likes],
                'comments': [comments],
                'watch_time_minutes': [watch_time],
                'video_length_minutes': [5],
                'subscribers': [views * 2],
                'engagement_rate': [engagement_rate],
                'category': ["Entertainment"],
                'country': ["IN"],
                'device': ["Mobile"]
            })

            pred_usd = model.predict(input_data)[0]

            if (likes + comments) > views:
                st.warning("⚠️ Engagement too high (unrealistic)")

            if pred_usd < 0:
                st.warning("⚠️ Model output invalid due to unusual input")
                pred_usd = 0

            pred_inr = pred_usd * 83

            with st.expander("ℹ️ About Model Limitations"):
                 st.write("""
                This model predicts revenue based on patterns learned from historical data.

                ⚠️ Important:
                - Predictions are reliable only within normal data ranges
                - Unusual inputs (very high engagement, etc.) may produce unrealistic results
                - This is because ML models cannot generalize beyond their training distribution

                We handle this by:
                ✔ Input validation  
                ✔ Warning messages  
                ✔ Output correction
                """)


            # 💰 RESULT CARDS
            col1, col2 = st.columns(2)

            with col1:
                st.markdown(f"""
                <div class="card">
                <h3 style="text-align:center;">💵 USD</h3>
                <h2 style="text-align:center;">${pred_usd:,.2f}</h2>
                </div>
                """, unsafe_allow_html=True)

            with col2:
                st.markdown(f"""
                <div class="card">
                <h3 style="text-align:center;">🇮🇳 INR</h3>
                <h2 style="text-align:center; color:red;">₹ {pred_inr:,.2f}</h2>
                </div>
                """, unsafe_allow_html=True)

        else:
            st.warning("Please enter all values")