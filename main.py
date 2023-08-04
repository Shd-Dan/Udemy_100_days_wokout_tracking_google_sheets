import requests
import datetime
import base64
import os

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
USERNAME = os.environ.get('USERNAME')
PASSWORD = os.environ.get('PASSWORD')
WEIGHT = 70
AGE = 38
GENDER = 'male'

url_end_point = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = os.environ.get("sheet_endpoint")
user_input = input("Please enter your final activity: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

params = {
    "query": user_input,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "age": AGE
}

response = requests.post(url_end_point, json=params, headers=headers)
result = response.json()

now = datetime.datetime.now()
current_day = now.strftime("%d/%m/%Y")
current_time = now.strftime("%H:%M:%S")

for exercise in result['exercises']:
    sheet_params = {
        "workout": {
            "date": current_day,
            "time": current_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    sheet_response = requests.post(url=sheet_endpoint,
                                   json=sheet_params,
                                   auth=(
                                       USERNAME,
                                       PASSWORD
                                   )
                                   )
    print(sheet_response.text)
