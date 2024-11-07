import json
from pip import _vendor
import pip._vendor.requests
latitude = '39.1031'
longitude = '-84.5120'
#Base url for the Weather API
BASE_URL ='https://api.weather.gov'
USER_AGENT = "Weather API (nrothe22@gmail.com)"

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
    for period in periods:
        print(f"{period['name']}: {period['probabilityOfPrecipitation']}\n")
        print(f"{period['name']}: {period['temperature']}\n")
       

if __name__ == "__main__":
    Real_forecast = get_weather_data(latitude, longitude)
    display_forecast(Real_forecast)