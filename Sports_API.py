import json
from pip import _vendor
import pip._vendor.requests
API_KEY = '14b80439951ab21af79d41a1c8856a57'

# Base URL for the Odds API
url = 'https://api.the-odds-api.com/v4/sports/americanfootball_nfl/events?apiKey=14b80439951ab21af79d41a1c8856a57'

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
    # Loop through the events and find Bengals' games
    for game in odds_data:
        home_team = game.get('home_team')
        away_team = game.get('away_team')

        if 'Cincinnati Bengals' in (home_team, away_team):
            print(f"Game: {home_team} vs {away_team}")
            print(f"Date: {game['commence_time']}")
            print('---')
else:
    print(f"Failed to fetch Bengals Game, Status Code: {response.status_code}")
