import streamlit as st
import pandas as pd

# Load your data
@st.cache
def load_data():
    pricing_df = pd.read_csv("/Users/antoinebertin/Documents/jedha/full_stack/projects_full_stack/deploy_ml/get_around_pricing_project.csv")
    return pricing_df

df = load_data()

# Sidebar for user inputs
st.sidebar.header('User Input Parameters')

def user_input_features():
    # Slider for delay threshold
    delay_threshold = st.sidebar.slider('Delay Threshold', 0, 100, 60)  # min: 0, max: 100, default: 60

    # Checkboxes for features
    features = {
        'model_key': st.sidebar.checkbox('Model Key'),
        'mileage': st.sidebar.checkbox('Mileage'),
        'engine_power': st.sidebar.checkbox('Engine Power'),
        'fuel': st.sidebar.checkbox('Fuel'),
        'paint_color': st.sidebar.checkbox('Paint Color'),
        'car_type': st.sidebar.checkbox('Car Type'),
        'private_parking_available': st.sidebar.checkbox('Private Parking Available'),
        'has_gps': st.sidebar.checkbox('Has GPS'),
        'has_air_conditioning': st.sidebar.checkbox('Has Air Conditioning'),
        'automatic_car': st.sidebar.checkbox('Automatic Car'),
        'has_getaround_connect': st.sidebar.checkbox('Has Getaround Connect'),
        'has_speed_regulator': st.sidebar.checkbox('Has Speed Regulator'),
        'winter_tires': st.sidebar.checkbox('Winter Tires'),
    }

    # Filter the dataframe based on selected features
    selected_features = [feature for feature, selected in features.items() if selected]
    filtered_df = df[selected_features]

    return delay_threshold, filtered_df

delay_threshold, df = user_input_features()

# Display the selected features
st.header('Selected Features')
st.write(df)

# Display the delay threshold
st.header('Delay Threshold')
st.write(delay_threshold)