import requests

def get_weather(api_key, location):
    base_url = "https://api.openweathermap.org/data/2.5/weather"

    # Check if the user entered a zip code or city name
    if location.isdigit():
        params = {"zip": location}
    else:
        params = {"q": location}

    params["appid"] = api_key
    params["units"] = "metric"  # You can change to "imperial" for Fahrenheit

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Check for errors in the response
        weather_data = response.json()

        # Extract relevant information
        temperature = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        wind_speed = weather_data["wind"]["speed"]
        description = weather_data["weather"][0]["description"]

        return temperature, humidity, wind_speed, description

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def main():
    api_key = "aa0554b6257cd8206e0d17fc98ddc7c1"  # Replace with your actual API key
    location = input("Enter a city name or zip code: ")

    weather_info = get_weather(api_key, location)

    if weather_info:
        temperature, humidity, wind_speed, description = weather_info
        print("\nCurrent Weather:")
        print(f"Temperature: {temperature} °C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
        print(f"Description: {description}")
    else:
        print("Unable to fetch weather information.")

if __name__ == "__main__":
    main()
