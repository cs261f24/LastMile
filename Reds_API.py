import json
from pip import _vendor
import pip._vendor.requests
API_KEY = '14b80439951ab21af79d41a1c8856a57'

# Base URL for the Odds API
url = 'https://api.the-odds-api.com/v4/sports/baseball_mlb/events'

# Parameters for the request
params = {
    'apiKey': API_KEY,
    'regions': 'us',  # Regions US
    'markets': 'h2h,spreads', 
    'oddsFormat': 'decimal',  
    'dateFormat': 'iso',     
}

# Making the request
response = _vendor.requests.get(url, params=params)

# Check if the request was successful
if response.status_code == 200:
    odds_data = response.json()
    

    # Loop through the events and find Cincinnati Reds games
    for game in odds_data:
        home_team = game.get('home_team')
        away_team = game.get('away_team')

        if 'Cincinnati Reds' in (home_team, away_team):
            print(f"Game: {home_team} vs {away_team}")
            print(f"Date: {game['commence_time']}")
            print('---')

        
    #Return no games if no team is playing in Cincinnati
    if 'Cincinnati Reds' not in odds_data:
        print("No Cincinnati Reds game happening today")

        
else:
    print(f"Failed to fetch games. Statues Code: {response.status_code}")