import requests

def get_weather(location):
    api_key = '33ddd549219d5905c1c90d65669aab65'  # Replace 'your_api_key_here' with your actual API key
    
    # Check if the input is a digit (ZIP code) or alphanumeric (city name)
    if location.isdigit():
        url = f'http://api.openweathermap.org/data/2.5/weather?zip={location}&appid={api_key}&units=metric'
    else:
        url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric'
    
    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            weather_info = {
                'Location': data['name'],
                'Country': data['sys']['country'],
                'Temperature': data['main']['temp'],
                'Feels Like': data['main']['feels_like'],
                'Humidity': data['main']['humidity'],
                'Description': data['weather'][0]['description'],
                'Wind Speed': data['wind']['speed'],
                'Visibility': data['visibility'] / 1000  # convert to kilometers
            }
            return weather_info
        else:
            print("Error fetching weather data. Please try again.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def main():
    print("Welcome to the Weather App!")
    location = input("Enter city name or ZIP code: ")

    weather = get_weather(location)

    if weather:
        print("\nWeather Information:")
        for key, value in weather.items():
            print(f"{key}: {value}")
    else:
        print("Weather data not available. Please try again.")

if __name__ == "__main__":
    main()
