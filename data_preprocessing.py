# data_preprocessing.py
import pandas as pd

def load_and_preprocess_data(file_path):
    # Load the dataset
    data = pd.read_csv(file_path)
    
    # Handle missing values
    data = data.dropna()
    
    # Convert date column to datetime
    data['Date'] = pd.to_datetime(data['Date'])
    
    # Select relevant features
    features = ['PM2.5', 'PM10', 'NO2', 'CO', 'O3', 'SO2', 'NH3', 'AQI']
    data = data[features]

    # Define AQI categories
    def categorize_aqi(aqi):
        if aqi <= 50:
            return 0  # Good
        elif aqi <= 100:
            return 1  # Satisfactory
        elif aqi <= 200:
            return 2  # Moderate
        elif aqi <= 300:
            return 3  # Poor
        elif aqi <= 400:
            return 4  # Very Poor
        else:
            return 5  # Severe

    # Create AQI category
    data['AQI_Category'] = data['AQI'].apply(categorize_aqi)

    # Features and target variable
    X = data.drop(['AQI', 'AQI_Category'], axis=1)
    y = data['AQI_Category']

    return X, y
