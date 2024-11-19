from datetime import datetime
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

# Array to hold the dates of the Reds Games
redsGamesRaw = []

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

            # Adds the dates of games to a an array
            redsGamesRaw.append(game['commence_time'])

    # Return no games if no team is playing in Cincinnati
    if 'Cincinnati Reds' not in odds_data:
        print("No Cincinnati Reds game happening today")


else:
    print(f"Failed to fetch games. Statues Code: {response.status_code}")

# Function converts the Reds dates into more manageable format


def convertGame(redsGamesRaw, redsGamesFixed):
    for x in redsGamesRaw:

        # Convert to a datetime object
        dateTimeObject = datetime.strptime(x, "%Y-%m-%dT%H:%M:%SZ")

        # Format it to only include the date part
        fixedDate = dateTimeObject.strftime("%Y-%m-%d")

        # Adds the modified date to a seperate array
        redsGamesFixed.append(fixedDate)

# Function checks if there is a home game on a specific date and returns true
# if there is


def redsGameCheck(dateInput):

    # Array to hold the formatted Bengals Games
    redsGamesFixed = []
    # Variable that holds the propely formatted game date
    convertGame(redsGamesRaw, redsGamesFixed)

    for x in redsGamesFixed:

        # Compare the dates
        if x == dateInput:
            # Returns true if a date matches
            return True

    # Returns False if none of the dates match
    return False


# Made for test purposes, comment out when not in use
# dateInput = input("Enter a date in YYYY-MM-DD format: ")
# print(redsGameCheck(dateInput))
