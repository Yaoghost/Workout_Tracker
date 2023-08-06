import requests
from datetime import datetime

APP_ID = ""
API_KEY = ""
nutritionix_endpoint = ""
GENDER = "MALE"
WEIGHT_KG = 60.0
HEIGHT = 165.7
AGE = 50

exercise = input("What exercises have you done today? ")
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}
params = {
    "query": exercise,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT,
    "age": AGE
}
response = requests.post(url=nutritionix_endpoint, json=params, headers=headers)
response.raise_for_status()

workout_data = response.json()
duration = workout_data['exercises'][0]['duration_min']
calories = workout_data['exercises'][0]['nf_calories']
workout = workout_data['exercises'][0]['user_input']

# ----------- HANDLE POSTS TO GOOGLE SHEET WITH SHEETY -------------

SHEET_ENDPOINT = ""

today = datetime.now()
date_string = today.strftime("%d/%m/%Y")
time_string = today.strftime("%X")
headers = {
    'Content-Type': 'application/json'
}
data_for_sheet = {
    "sheet1": {
        "date": date_string,
        "time": time_string,
        "exercise": workout,
        "duration": duration,
        "calories": calories,
    }

}

response = requests.post(url=SHEET_ENDPOINT, json=data_for_sheet, headers=headers)
response.raise_for_status()
