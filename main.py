import requests

APP_ID = "e2f60d41"
API_KEY = "a1dc13ee26779ef2d33c39b09e835282"
WEIGHT = 70
AGE = 38
GENDER = 'male'

url_end_point = "https://trackapi.nutritionix.com/v2/natural/exercise"
user_input = input("Please enter your final activity: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": user_input,
    "gender": "female",
    "weight_kg": 72.5,
    "height_cm": 167.64,
    "age": 30
}

response = requests.post(url_end_point, json=parameters, headers=headers)
result = response.json()
print(result)