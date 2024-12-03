# Developer Documentation 
<p><em>Last Mile 2</em><p> 
<img src="https://upload.wikimedia.org/wikipedia/commons/6/66/Xavier_University_%28Cincinnati%29_logo.png" jsaction="" class="sFlh5c FyHeAf iPVvYb" style="max-width: 536px; height: 92px; margin: 47px 0px; width: 350px;" alt="File:Xavier University (Cincinnati) logo.png - Wikipedia" jsname="kn3ccd" aria-hidden="false">

### How to set up the environment if it's not executable:
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
<p><strong>There are several different API's that this program runs on such as:</strong>
    <ul>
        <li>Odds Data API.</li>
        <li>OHGO API.</li>
        <li>National Weather Service API.</li> 
    </ul>
<strong>To get to the API's if you want to view how the code runs access the following files:</strong>
    <ol>
        <li>Traffic_API.py for traffic and incident reports along with travel delays.  
        <li>Sports_API.py for sports game information.
        <li>Weather_API.py for 7 days forecast with a chance of precipitation.
    </ol>
<p><strong>For running the API on your own:</strong>
    <ul> 
        <li>You will need to set up your account at each website</li>
        <li>With each website you will need to get your own API key</li>
        <li>For Traffic and Sports API you will replace the API_KEY with your API key you get from the website</li>
        <li>For Weather API you will need to replace USER_AGENT with your own account email address</li>
    </ul>
</p>
<strong>Features of the API's are all a bit different in the formats that they return and how they operate:</strong>
    <ol>
        <li>Traffic API works by taking the location variable that has been to Cincinnati. Then by swapping the endpoint variable out for different valid endpoints in OHGO's API, it fetches construction data, incidents data, and travel delays. In its main, it takes the data that has been fetched for each endpoint and prints out the respective data for each fetch.</li>
        <li>Sports API works in a similar way as the Traffic API with it swamping the endpoint variable out of valid endpoints: americanfootball_nfl, americanfootball_ncaaf, soccer_usa_mls, and baseball_mlb. For each of these endpoints, it searches from the list called CINCINNATI_TEAMS to look for teachers in their respective areas. If it finds that a team from Cincinnati has a game it returns a team to the home_team variable and the other team to the away_team value. Along with this, it returns the game in date-time format for when it starts. If it does not find a Cincinnati team playing soon it will return that there is no game today. Additionally, the API includes a function for the GUI to reference called conflictCheck. This function reads in a date in date-time format and will check if there are any sporting events on that date. If there is a conflict, the function will return true. This is utilized in the GUI to determine whether a notification of a sporting event needs to be displayed or not.</li>
        <li>Weather API works by giving a 7-day forecast for a location that has been put into coordience to search within that grid. At the current moment, it gives a forecast of the next 7 days with a high to low for the day and night times. It also returns that string that gives us the value from precipitation for that day.
        </li>
    </ol>
</p>

## Documentation of SKLearn Model:
<p>Information on what each section of the SciKitPorgram.py does:
    <ol>
        <li> First Section are simple imports that allow the SKLearn to run along with some imports for the live weather API.
        <li> Live Weather API Info: URL and login information for the API along with location information.
        <li> Variables for GUI: Array variables for weather and volunteer information for the GUI to use.
        <li> Load Data: Reads in two separate CSV files; Historic weather data and historic Last Mile data.  Creates a singular data frame using both files and combines the same-day deliveries into one variable for each day known as volunteers.  The last part selects only the columns used for the SKLearn Model.
        <li> Preprocess Data: Create features and target data variables. Identifies categorical vs numerical data for the Pipeline
        <li> Create Pipeline: Creates a pipeline that transforms the data into numerical data that can be used by the model.
        <li> Train and Evaluate: Trains data using a Logistic Regression model and dumps model into finalized_model.plk
        <li> Predict Volunteers: Creates a function that takes parameters used in the model and outputs a volunteer prediction
        <li> Get Weather Data: Retrieves Live Weather data from the API
        <li> Display Forecast: Transforms weather data into 3 arrays, one for temperature, precipitation, and volunteer estimate. Precipitation data still in not int format
    <ol>
</p>
