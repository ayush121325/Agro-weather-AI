import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Agro-weather-AI",
    layout="wide"
)

st.markdown("""
<style>

.stApp{
    background-color : #f7faf7;}

[data-testid="stSidebar"] {
    background-color: #123b2a}

[data-testid="stSidebar"] * {
    color : white;}

.main-title {
    color: #174b32;
    font-size: 38px;
    font-weight: 800;}

.subtitle {
    color: #647568;
    font-size: 15px;}

div[data-testid="stMetric"] {
    background-color: white;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #e5eee5;}

</style>
""", unsafe_allow_html=True)

#sidebar navigation

st.sidebar.title("Agro-weather-AI")
st.sidebar.caption("Smart Agricultural Platform")

page = st.sidebar.radio(
    "NAVIGATION",
    [
        "Overview",
        "Crop Yield Prediction",
        "Irrigation Advisory",
        "Rainfall Analytics",
        "Model Performance"
    ]
)

st.sidebar.divider()

st.sidebar.caption("AI-powered agricultural insights")

#Overview PAGE


if page=="Overview":

    st.markdown(
        '<p class="main-title"> Agriculture Dashboard </p>',
            unsafe_allow_html=True)


    st.markdown(
        '<p class="subtitle"> Monitor crop productivity and irrigation insights.</p>',
        unsafe_allow_html=True
    )

    st.info(
        "Prototype dashboard:displayed sample statistics"
        "are illustrative , not live model results." 
         
    )

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Crop Yield", "4.2 t/ha", "+8%")
    col2.metric("Rainfall", "820 mm", "-5%")
    col3.metric("Water Status", "Monitor")
    col4.metric("Model Status", "Pending")

    st.divider()

    left, right = st.columns(2)

    with left:
        st.subheader("Monthly Rainfall")

        rainfall_data = pd.DataFrame({
            "Rainfall (mm)": [40, 65, 90, 120, 180, 210,
                              190, 150, 100, 70, 45, 30]
        }, index=[
            "Jan", "Feb", "Mar", "Apr", "May", "Jun",
            "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
        ])

        st.bar_chart(rainfall_data)

    with right:
        st.subheader("Crop Yield Trend")

        yield_data = pd.DataFrame({
            "Yield (t/ha)": [2.8, 3.1, 3.4, 3.7, 4.0, 4.2]
        }, index=["2016", "2017", "2018",
                  "2019", "2020", "2021"])

        st.line_chart(yield_data)


# -----------------------------
# CROP YIELD PREDICTION PAGE
# -----------------------------

elif page == "Crop Yield Prediction":

    st.title("🌾 Crop Yield Prediction")

    st.write(
        "Enter agricultural information to prepare a yield prediction."
    )

    with st.form("yield_form"):

        col1, col2 = st.columns(2)

        with col1:

            state = st.selectbox(
                "Select State",
                ["Bihar", "Uttar Pradesh", "Punjab",
                 "Haryana", "Madhya Pradesh"]
            )

            crop = st.selectbox(
                "Select Crop",
                ["Rice", "Wheat", "Maize",
                 "Potato", "Sugarcane"]
            )

            season = st.selectbox(
                "Select Season",
                ["Kharif", "Rabi", "Summer",
                 "Autumn", "Winter"]
            )

            area = st.number_input(
                "Cultivated Area (hectares)",
                min_value=0.1,
                value=2.0
            )

        with col2:

            rainfall = st.number_input(
                "Annual Rainfall (mm)",
                min_value=0.0,
                value=800.0
            )

            fertilizer = st.number_input(
                "Fertilizer Usage (kg)",
                min_value=0.0,
                value=100.0
            )

            pesticide = st.number_input(
                "Pesticide Usage (kg)",
                min_value=0.0,
                value=10.0
            )

            year = st.number_input(
                "Crop Year",
                min_value=1997,
                max_value=2030,
                value=2026
            )

        submitted = st.form_submit_button(
            "Prepare Yield Prediction",
            use_container_width=True
        )

    if submitted:

        st.success("Agricultural information captured!")

        st.subheader("Submitted Information")

        st.write({
            "State": state,
            "Crop": crop,
            "Season": season,
            "Area": area,
            "Rainfall": rainfall,
            "Fertilizer": fertilizer,
            "Pesticide": pesticide,
            "Year": year
        })

        st.warning(
            "ML model integration is pending. "
            "A real yield prediction will appear after "
            "the trained model is connected."
        )


# -----------------------------
# IRRIGATION ADVISORY PAGE
# -----------------------------

elif page == "Irrigation Advisory":

    st.title("💧 Irrigation Advisory")

    st.write(
        "Explore the prototype rainfall-deficit monitoring interface."
    )

    with st.form("irrigation_form"):

        deviation = st.number_input(
            "Rainfall Deviation (%)",
            min_value=-100.0,
            max_value=200.0,
            value=-20.0
        )

        dry_days = st.number_input(
            "Days Since Last Rainfall",
            min_value=0,
            max_value=120,
            value=5
        )

        check = st.form_submit_button(
            "Check Prototype Status",
            use_container_width=True
        )

    if check:

        # Demonstration thresholds only.
        # These are not validated agronomic recommendations.

        if deviation <= -30 and dry_days >= 10:
            st.error("IRRIGATE NOW - Prototype high-risk flag")

        elif deviation <= -15 or dry_days >= 5:
            st.warning("MONITOR - Prototype monitoring flag")

        else:
            st.success("SAFE - No prototype warning triggered")

        st.caption(
            "Demonstration rule only. Actual irrigation decisions "
            "require crop stage, soil moisture, local conditions "
            "and agronomic validation."
        )


# -----------------------------
# RAINFALL ANALYTICS PAGE
# -----------------------------

elif page == "Rainfall Analytics":

    st.title("🌧️ Rainfall Analytics")

    st.write(
        "Visualise historical rainfall information."
    )

    st.info(
        "Historical rainfall dataset integration is pending."
    )


# -----------------------------
# MODEL PERFORMANCE PAGE
# -----------------------------

elif page == "Model Performance":

    st.title("📊 Model Performance")

    st.write(
        "Monitor the performance of our trained ML models."
    )

    st.info(
        "Model evaluation results will appear after "
        "training and validation are completed."
    )

    col1, col2, col3, col4 = st.columns(4)

    st.metric("RMSE", "Pending")
    st.metric("MAPE", "Pending") 

    col1.metric("Crop Yield", "4.2 t/ha", "+8%")
    col2.metric("Rainfall", "820 mm", "-5%")
    col3.metric("Water Status", "Monitor")
    col4.metric("Model Status", "Pending")

    st.divider()

    left, right = st.columns(2)

    with left:
        st.subheader("Monthly Rainfall")

        rainfall_data = pd.DataFrame({
            "Rainfall (mm)": [40, 65, 90, 120, 180, 210,
                              190, 150, 100, 70, 45, 30]
        }, index=[
            "Jan", "Feb", "Mar", "Apr", "May", "Jun",
            "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
        ])

        st.bar_chart(rainfall_data)

    with right:
        st.subheader("Crop Yield Trend")

        yield_data = pd.DataFrame({
            "Yield (t/ha)": [2.8, 3.1, 3.4, 3.7, 4.0, 4.2]
        }, index=["2016", "2017", "2018",
                  "2019", "2020", "2021"])

        st.line_chart(yield_data)









