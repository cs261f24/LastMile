import json
from pip import _vendor
import pip._vendor.requests

API_KEY = '14b80439951ab21af79d41a1c8856a57'
BASE_URL = 'https://api.the-odds-api.com/v4/sports'

# List of teams to search for
CINCINNATI_TEAMS = ["Cincinnati Bearcats","FC Cincinnati", "Cincinnati Bengals","Cincinnati Reds" ]

def get_sports(endpoint):
    """
    Fetches sports data for a given endpoint from the Odds API.
    """
    url = f"{BASE_URL}/{endpoint}/events"
    params = {
        'apiKey': API_KEY,
        'regions': 'us',  # Fetch only US-based data
        'markets': 'h2h,spreads',  # Head-to-head and spread markets
        'oddsFormat': 'decimal',  # Decimal format for odds
        'dateFormat': 'iso',  # ISO date format
    }

    try:
        response = _vendor.requests.get(url, params=params)

        # Check if the request was successful
        if response.status_code == 200:
            odds_data = response.json()
            found_games = False

            # Process and display game data
            for game in odds_data:
                home_team = game.get('home_team')
                away_team = game.get('away_team')

                # Check if any of the Cincinnati teams are involved
                if any(team in (home_team, away_team) for team in CINCINNATI_TEAMS):
                    found_games = True
                    print(f"Sport: {endpoint}")
                    print(f"Game: {home_team} vs {away_team}")
                    print(f"Date: {game['commence_time']}")
                    print('---')

            # If no games are found for Cincinnati teams
            if not found_games:
                print(f"No games featuring Cincinnati teams in {endpoint}.")
        else:
            print(f"Failed to fetch games for {endpoint}. Status Code: {response.status_code}")

    except _vendor.requests.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    sports_endpoints = [
        'americanfootball_ncaaf', 
        'soccer_usa_mls', 
        'americanfootball_nfl', 
        'baseball_mlb'
    ]

    for sport in sports_endpoints:
        print(f"\nFetching games for {sport}...")
        get_sports(sport)


