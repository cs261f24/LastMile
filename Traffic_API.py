import json
import pip._vendor.requests as requests  

API_KEY = '?api-key=6d7a57bf-20f9-443b-9f98-2eb9ad850c18'
BASE_URL = 'https://publicapi.ohgo.com/api/v1/'

# This function gets traffic data for a specific region or statewide
def get_traffic_data(endpoint, location=None):
    # Define the API URL
    url = f'{BASE_URL}{endpoint}{API_KEY}'

    # Sets up the parameters
    params = {
        'apikey': API_KEY,
    }
    if location:
        params['location'] = location  # Specific region or location filter

    # Make the GET request to the OHGO API
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: Unable to fetch data from {endpoint} (Status Code: {response.status_code})")
        return None

# Fetch construction data
def get_construction(location=None):
    return get_traffic_data('construction', location)

# Fetch incidents data
def get_incidents(location=None):
    return get_traffic_data('incidents', location)

# Fetch travel delays data
def get_travel_delays(location=None):
    return get_traffic_data('travel-delays', location)

# Main code
if __name__ == '__main__':
    location = 'Cincinnati'  # Cincinnati-specific data

    # Get construction data
    construction_data = get_construction(location)
    if construction_data:
        construction_descriptions = [item.get('description', 'No description') for item in construction_data.get('results', [])]
        print("Construction Data:")
        print(json.dumps(construction_descriptions, indent=4))

    # Get incidents data
    incidents_data = get_incidents(location)
    if incidents_data:
        incidents_descriptions = [item.get('description', 'No description') for item in incidents_data.get('results', [])]
        print("\nIncidents Data:")
        print(json.dumps(incidents_descriptions, indent=4))

    # Get travel delays data
    travel_delays_data = get_travel_delays(location)
    if travel_delays_data:
        travel_description = [item.get('description', 'No description') for item in travel_delays_data.get('results', [])]
        print("\nTravel Delays Data:")
        print(json.dumps(travel_descriptions, indent=4))

