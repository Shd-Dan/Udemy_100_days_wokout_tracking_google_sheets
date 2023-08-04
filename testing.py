import requests
import base64

# Replace 'url' with the actual URL you want to fetch data from
url = 'your_url_here'

# Encode your credentials in Base64 (if required)
username = 'null'
password = 'null'
credentials = f"{username}:{password}".encode('utf-8')
base64_credentials = base64.b64encode(credentials).decode('utf-8')

# Set up custom headers
headers = {
    'Authorization': f'Basic {base64_credentials}'
}

# Make the GET request with custom headers
response = requests.get(url, headers=headers)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the response as JSON
    json_data = response.json()
    # Do something with your data
    print(json_data)
else:
    print(f"Request failed with status code: {response.status_code}")