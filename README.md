# Workout_Tracker
This Python script allows you to track your exercises and record them in a Google Sheet using the Nutritionix API and the Sheety API. It's a simple and convenient way to keep a log of your workouts and monitor your progress over time.

Prerequisites
Before using this script, make sure you have the following:

Python installed on your system.
The requests library. You can install it using the following command:
bash

pip install requests
Access to Nutritionix API and Sheety API:

Get your Nutritionix API credentials (APP_ID and API_KEY) by signing up at https://www.nutritionix.com/business/api.
Create an account on Sheety at https://sheety.co/ and create a new Google Sheet.
Setup
Clone or download this repository to your local machine.

Open the exercise_tracker.py file in a text editor.

Fill in your Nutritionix API credentials:

APP_ID = "YOUR_NUTRITIONIX_APP_ID"
API_KEY = "YOUR_NUTRITIONIX_API_KEY"
Set the Nutritionix endpoint:
python
Copy code
nutritionix_endpoint = "https://api.nutritionix.com/v1_1/natural/exercise"
Adjust your personal information (gender, weight, height, and age):
python
Copy code
GENDER = "MALE"  # Change to "FEMALE" if applicable
WEIGHT_KG = 60.0
HEIGHT = 165.7
AGE = 50
Set up the Sheety endpoint:
python
Copy code
SHEET_ENDPOINT = "YOUR_SHEETY_API_ENDPOINT"
Run the script using the command:
bash
Copy code
python exercise_tracker.py
How to Use
When you run the script, it will prompt you to enter the exercises you've done today.

The script will make a request to the Nutritionix API to calculate the duration and calories burned for the specified exercise.

The data (date, time, exercise, duration, and calories) will be recorded in the Google Sheet using the Sheety API.

You can view your exercise log in the Google Sheet.

Contributing
Feel free to contribute to this project by opening issues or pull requests on the GitHub repository.

Happy exercising!
