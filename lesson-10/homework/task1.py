import request

def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = request.get(url) 
    if response.status_code == 200:
        data = response.json()
        weather_info = {
            "City": data["name"],
            "Temperature (°C)": data["main"]["temp"],
            "Humidity (%)": data["main"]["humidity"],
            "Weather": data["weather"][0]["description"],
            "Wind Speed (m/s)": data["wind"]["speed"]
        }
        return weather_info
    else:
        return {"Error": "City not found or invalid API key"}
API_KEY = "your_api_key_here"
CITY = "Tashkent"
weather_data = get_weather(CITY, API_KEY)
print("\nWeather Information:")
for key, value in weather_data.items():
    print(f"{key}: {value}")