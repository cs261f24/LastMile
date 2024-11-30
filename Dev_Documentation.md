# Developer Documentation 
<p><em>Last Mile 2</em><p> 
<img src="https://upload.wikimedia.org/wikipedia/commons/6/66/Xavier_University_%28Cincinnati%29_logo.png" jsaction="" class="sFlh5c FyHeAf iPVvYb" style="max-width: 536px; height: 92px; margin: 47px 0px; width: 350px;" alt="File:Xavier University (Cincinnati) logo.png - Wikipedia" jsname="kn3ccd" aria-hidden="false">

### How to set up the enviroment if it's not executeable:
<ol>
    <li> Install PyInstaller:
    Type below command in the command prompt to create python to executable. 
    
    pip install pyinstaller

</li>
    <li> Prepare Your Script: 
    Make sure the Python script is working as expected.
    </li>
    <li> Run the Packing Command:
    Use PyInstaller to generate the .exe file.

    pyinstaller --onefile Last_Mile_2.py
</li>
    <li>Locate the .exe File:
    After running the command, you can find the .exe file in the <em>dict</em> directory.
    </li>
</ol>

## Documentation of API's:
<p>There are several differnt API's that this program runs on such as:
    <ul>
        <li>Odds Data API.</li>
        <li>OHGO API.</li>
        <li>National Weather Service API.</li> 
    </ul>
<strong>To get to the API's if you want to view how the code runs access the following files:</strong>
    <ol>
        <li>Traffic_API.py for traffic and incendent reports along with travel delays.  
        <li>Sports_API.py for sports game information.
        <li>Weather_API.py for 7 days forecast with chance of percipitation.
    </ol>
<strong>Features of the API's are all a bit different in the formats that they reutrn and how they operate:</strong>
    <ol>
        <li>Traffic API work by taking the location variable that been to Cincinatti. Then by swaping the endpoint variable out for different valid endpoints in OHGO's api and it fetchs contrstruction data, incdents data, and travels dealys. In its main it takes the data that has been fetched for each endpoint and prints out the respective data for each fetch.</li>
        <li>Sports API works in a simliar way as the Traffic API with it swamping the endpoint variable out fo valid endpoints: americanfootball_nfl, americanfootball_ncaaf, soccer_usa_mls, and baseball_mlb. For each of these endpoint it seaches from the list called CINCINNATI_TEAMS to look for teach in their respective area. If it find that a team from Cincinnati has a game it returns a team to the home_team variable and the other team to the away_team value. Along with this it returns the game in date - time format for when it starts. If it does not find a Cincinnati team playing soon it will return that there is no game today. </li>
        <li>Weather API works by givng a 7 day forcast for a locatin that has been put into corridnance to search within that grid. At the current moment it gives a forcast of the next 7 days with a high to low for the day and night times. It also reutrns that string that gives us the value from percipitation for that day.
        </li>
    </ol>
</p>

