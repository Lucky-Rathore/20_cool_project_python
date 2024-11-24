import requests

def get_weather_forecast(lat, lon):
    api_key = 'your_api_key'  # Replace with your API key
    base_url = 'https://api.openweathermap.org/data/2.5/weather'
    complete_url = f"{base_url}?lat={lat}&lon={lon}&appid={api_key}"
    
    response = requests.get(complete_url)
    
    if response.status_code == 200:
        data = response.json()
        try:  # Added a try-except block for cases where city or country might be missing
            city_name = data['name']
            country = data['sys']['country']
            forecast = data # Current weather data, not a forecast list
            print(f"Current weather for {city_name}, {country}:")

            date_time = data['dt'] # Use dt for timestamp and format it
            from datetime import datetime
            formatted_date_time = datetime.utcfromtimestamp(date_time).strftime('%Y-%m-%d %H:%M:%S')
            temperature = forecast['main']['temp']
            description = forecast['weather'][0]['description']

            print(f"Date/Time: {formatted_date_time} UTC") # Clarify it's UTC
            print(f"Temperature: {temperature - 273.15:.2f}°C")
            print(f"Description: {description}")

        except KeyError as e:
            print(f"Error: Key not found in weather data: {e}")
            print(data) # print the data for debugging
    else:
        print("Unable to fetch weather data")


# Example usage
if __name__ == "__main__":
    latitude = input("Enter latitude: ")
    longitude = input("Enter longitude: ")
    get_weather_forecast(latitude, longitude)
# Example usage
if __name__ == "__main__":
    latitude = input("Enter latitude: ")
    longitude = input("Enter longitude: ")
    get_weather_forecast(latitude, longitude)
