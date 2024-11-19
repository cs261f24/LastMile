import joblib
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix, mean_squared_error, r2_score
import json
import random
from pip import _vendor
import pip._vendor.requests
latitude = '39.1031'
longitude = '-84.5120'
#Base url for the Weather API
BASE_URL ='https://api.weather.gov'
USER_AGENT = "Weather API (nrothe22@gmail.com)"

# Variables for GUI
daytemp = []
dayprecip = []
dayvolunteer = []



# Load the data
def load_data(file_path):
    data = pd.read_csv(file_path)
    df1 = pd.read_csv("Weather.csv")
    df2 = pd.read_csv("LastMile.csv")

    count = df2['date'].value_counts()['12/29/21']
    #print (count)

    df2['volunteers'] = df2.groupby('date')['date'].transform('count')
    #print(df2)
    
    data = pd.merge(df1, df2, on='date')
    data = data.drop_duplicates(subset='date')

    data['preciptype'].fillna('none', inplace=True)
    data['windgust'].fillna(0, inplace=True)
    data['severerisk'].fillna(0, inplace=True)
    data = data[['temp', 'precipprob', 'volunteers']]
    #data.fillna('none', inplace=True) 
    data.dropna(inplace=True)
    print(data)
    
    return data


# Preprocess the data
def preprocess_data(data, target_column):
    X = data.drop(columns=[target_column])  # Features
    y = data[target_column]  # Target variable
    
    # Identify categorical and numerical columns
    categorical_cols = X.select_dtypes(include=['object']).columns
    numerical_cols = X.select_dtypes(include=['int64', 'float64']).columns
    
    return X, y, categorical_cols, numerical_cols

# Create the model pipeline
def create_pipeline(categorical_cols, numerical_cols):
    # Preprocessing for numerical data
    numerical_transformer = 'passthrough'  # No transformation for numerical data

    # Preprocessing for categorical data
    categorical_transformer = OneHotEncoder(handle_unknown='ignore')

    # Combine preprocessors
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numerical_transformer, numerical_cols),
            ('cat', categorical_transformer, categorical_cols)
        ]
    )

    # Create a pipeline that first transforms data and then fits a model
    model = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('classifier', RandomForestClassifier(random_state=42))
    ])
    
    return model

# Train and evaluate the model
def train_and_evaluate(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LogisticRegression(penalty='l1', C=0.01, solver='liblinear', max_iter=1000)
    model.fit(X_train, y_train)
    
    # Predictions
    y_pred = model.predict(X_test)
    
    # Evaluation
    score = accuracy_score(y_test,y_pred)
    #print(confusion_matrix(y_test, y_pred))
    #print(classification_report(y_test, y_pred))
    #print(score)

    filename = 'finalized_model.plk'
    joblib.dump(model, filename)

# Predict Volunteers with Parameters
def predict_volunteers(precipprob, temp):
    features = np.array([[precipprob, temp]])
    model = joblib.load('finalized_model.plk')
    prediction = model.predict(features)

    return prediction[0]


def get_weather_data(latitude,longitude):
    headers = {
    'User-Agent': USER_AGENT,
    'Accept': 'application/ld+json'
}
    
    url = f'{BASE_URL}/points/{latitude},{longitude}'
    grid_response = _vendor.requests.get(url, headers=headers)
    
    if grid_response.status_code != 200:
        print(f"Error fetching grid data: {grid_response.status_code}")
    
    grid_data = grid_response.json()
    print(grid_data)
    grid_id = grid_data['gridId']
    grid_x = grid_data['gridX']
    grid_y = grid_data['gridY']

    # Get the forecast for the grid point
    forecast_url = f"{BASE_URL}/gridpoints/ILN/{grid_x},{grid_y}/forecast"
    forecast_response = _vendor.requests.get(forecast_url, headers=headers)
    
    if forecast_response.status_code != 200:
        print(f"Error fetching forecast data: {forecast_response.status_code}")
    
    forecast_data = forecast_response.json()
    
    return forecast_data



def display_forecast(forecast_data):
    periods = forecast_data['periods']
    print(f"Weather Forecast for Cincinnati, OH:\n")

    num = 1
    for period in periods:
        temp = int(f"{period['temperature']}\n")
        precip = f"{period['probabilityOfPrecipitation']}:\n"
        volunteers = predict_volunteers(0, temp)
        # Test Purposes Random INT (POP Not working as INT)
        random_int = random.randint(10, 40)
        if num == 1:
            num = 0
            daytemp.append(temp)
            dayprecip.append(precip)
            dayvolunteer.append(volunteers + random_int)
        else:
            num = 1
    


# Main execution
def Skl():
    #file_path = 'Weather.csv'
    
    #data = load_data(file_path)
    #target_column = 'volunteers'  
    
    #X, y, categorical_cols, numerical_cols = preprocess_data(data, target_column)
    #train_and_evaluate(X, y)

    Real_forecast = get_weather_data(latitude, longitude)
    display_forecast(Real_forecast)
    print(daytemp)
    print(dayprecip)
    print(dayvolunteer)
    


