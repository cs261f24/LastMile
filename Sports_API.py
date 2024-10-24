from datetime import datetime
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

# Read in an input of a date
dateInput = input("Enter the date (YYYY-MM-DD): ")

# Array to hold the dates of the Bengals Games
bengalsGame = []

# Array to hold the formatted Bengals Games
formattedBengalsGames = []

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

            # Adds the dates of games to a an array
            bengalsGame.append(game['commence_time'])

else:
    print(f"Failed to fetch Bengals Game, Status Code: {response.status_code}")

# Function converts date into more manageable format


def convertGame(bengalsGame):
    for x in bengalsGame:

        # Convert to a datetime object
        dateTimeObject = datetime.strptime(x, "%Y-%m-%dT%H:%M:%SZ")

        # Format it to only include the date part
        modifiedDate = dateTimeObject.strftime("%Y-%m-%d")

        # Adds the modified date to a seperate array
        formattedBengalsGames.append(modifiedDate)

    # Returns bengalsGame with the dates formatted as strings


# Variable that holds the propely formatted game date
convertGame(bengalsGame)

# Function checks if there is a home game on a specific date and returns true
# if there is


def conflictCheck(formattedBengalsGames, dateInput):
    for x in formattedBengalsGames:

        # Compare the dates
        if x == dateInput:
            # Returns true if a date matches
            return True

    # Returns False if none of the dates match
    return False


# Prints the results of the conflict check function
print(conflictCheck(formattedBengalsGames, dateInput))
