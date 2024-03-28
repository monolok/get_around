import streamlit as st
import pandas as pd

# Load your data
@st.cache_data
def load_data():
    delay_df = pd.read_excel("/Users/antoinebertin/Documents/jedha/full_stack/projects_full_stack/deploy_ml/get_around_delay_analysis.xlsx")
    pricing_df = pd.read_csv("/Users/antoinebertin/Documents/jedha/full_stack/projects_full_stack/deploy_ml/get_around_pricing_project.csv")
    return delay_df, pricing_df

delay_df, pricing_df = load_data()

# Sidebar for user inputs
st.sidebar.header('User Input Parameters')

def user_input_features():
    # Slider for delay threshold
    delay_threshold = st.sidebar.slider('Delay Threshold', 0, 200, 60, step=1)  # min: 0, max: 200, default: 60
    rental_data_filtered = delay_df[delay_df['state'] == 'ended']
    # Filter out rentals with delay at checkout in minutes greater than or equal to threshold
    rentals_with_delay_threshold = rental_data_filtered[rental_data_filtered['time_delta_with_previous_rental_in_minutes'] >= delay_threshold]
    # Get unique car_id from rentals_with_delay_threshold
    affected_cars = rentals_with_delay_threshold['car_id'].unique()
    affected_cars_count = len(affected_cars)
    affected_cars_percentage = affected_cars_count / rental_data_filtered['car_id'].nunique() * 100

    # Filter the dataframe based on selected features to get mean price
    pricing_features = {
        #'engine_power': st.sidebar.slider('Engine Power', int(pricing_df["engine_power"].min()), int(pricing_df["engine_power"].max()), int(pricing_df["engine_power"].mean()), step=1),
        #'mileage': st.sidebar.slider('Mileage', 0, int(pricing_df["mileage"].max()), int(pricing_df["mileage"].mean()), step=1),
        'automatic_car': st.sidebar.checkbox('Automatic Car'),
        'has_getaround_connect': st.sidebar.checkbox('Has Getaround Connect'),
        'has_gps': st.sidebar.checkbox('Has GPS'),
        'private_parking_available': st.sidebar.checkbox('Private Parking Available'),
        #'car_type': st.sidebar.selectbox('Car Type', pricing_df["car_type"].unique()),
        'has_air_conditioning': st.sidebar.checkbox('Has Air Conditioning'),
        'has_speed_regulator': st.sidebar.checkbox('Has Speed Regulator')
    }

    filtered_princing_df = pricing_df[
                            #(pricing_df['engine_power'] < pricing_features['engine_power']) & 
                             #(pricing_df['mileage'] < pricing_features['mileage']) &
                             (pricing_df['automatic_car'] == pricing_features['automatic_car']) &
                             (pricing_df['has_getaround_connect'] == pricing_features['has_getaround_connect']) &
                             (pricing_df['has_gps'] == pricing_features['has_gps']) &
                             (pricing_df['private_parking_available'] == pricing_features['private_parking_available']) &
                             #(pricing_df['car_type'] == pricing_features['car_type']) &
                             (pricing_df['has_air_conditioning'] == pricing_features['has_air_conditioning']) &
                             (pricing_df['has_speed_regulator'] == pricing_features['has_speed_regulator'])
                             ]
    mean_price = filtered_princing_df["rental_price_per_day"].mean()
    revenue_loss = mean_price * affected_cars_count

    return affected_cars_count, affected_cars_percentage, revenue_loss

affected_cars_count, affected_cars_percentage, revenue_loss = user_input_features()

# Display the percentage of affected cars
st.header(f'Affected Cars by Delay threshold')
st.write(f'{affected_cars_count} cars affected ({round(affected_cars_percentage, 2)}%)')

# Display the potential revenue loss
st.header('Potential Revenue Loss')
st.write(f'{round(revenue_loss, 2)}$')