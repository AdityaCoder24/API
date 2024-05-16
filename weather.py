import requests

# Replace with your actual API key
API_KEY = "224cb7edb1224d72b8b131521241505"

# Base URL for WeatherAPI
BASE_URL = "https://api.weatherapi.com/v1/"

# Example: Get current weather for a specific location (e.g., New York)
location = "Gurgaon"
endpoint = f"current.json?key={API_KEY}&q={location}"

try:
    response = requests.get(BASE_URL + endpoint)
    data = response.json()

    # Extract relevant information from the response
    temperature = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]

    print(f"Current temperature in {location}: {temperature}°C ({condition})")
except requests.RequestException as e:
    print(f"Error fetching data: {e}")

