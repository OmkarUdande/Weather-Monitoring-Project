# Weather Monitoiring System:=

# OverView :=

This project is a Django_Based Weather Monitoring System That Retrives Real-Time Weather Data From The OpernWeatherMap API.
It allows Users To view current weather Conditions For Multiple Cites And Dispays essential Information Like Tempeature And Weather Status.

# FEATURES :=

--> Fetches Current Weather Data For Cities Like 'MUMBAI',DELHI,BANGALORE',CHENNAI, KOLKATA And HYDERABAD'.
--> Displays Tempereature (in Celsius), Feels-Like Temperature, and Weather condition.
--> Stores Weather Data In a Database For Easy Retrieval.
--> User-friendly Web Interface For Displaying Weather Information.

# Installation :=

### Requirements:=

Befor You Begin, Ensure You Have The Follwing installed One Machine :
**Python**: Version 3.x
**Django**: Version 3.x or higher
**Requests** library: For making HTTP requests

### Steps to Install :=

**Clone the Repository**

**1.**
First ,CLone The Repository TO YOur Local Machine Using Git
Open Your Terminal or Command Prompt and Run: ```bash
git clone<repository-url>
cd weather-monitoring

**2.**

### Install Dependencies

    Install the required Python packages using pip. Make sure you have a requirements.txt file in your project directory:

    --> pip install -r requirements.txt <--

**3.**

### Set Up Your API Key

    Sign Up at OpenWeatherMap And Obtain Your API key.
    Open Your Django Settings File (usually settings.py) And Add The Following Line:

    --> OPENWEATHERMAP_API_KEY = '011b9642af74618550daecfc028bb3b6' <--

**4.**

### Run Migrations

    Apply the database migrations to set up the necessary tables:

    --> python manage.py migrate <--

**5.**

### Start the Development Server

    Launch the Django development server to run your application:

    --> python manage.py runserver <--

**6.**

### Access the Application

    Open your web browser and navigate to

     --> http://127.0.0.1:8000/weather/ <--

to view the weather monitoring application.
