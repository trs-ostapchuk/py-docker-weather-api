import requests


def get_weather() -> None:
    url = "http://api.weatherapi.com/v1/current.json?key=15ac9e69e52c4ff0921192849262701&q=Paris&aqi=no"
    response = requests.get(url)
    data = response.json()
    city = data["location"]["name"]
    country = data["location"]["country"]
    localtime = data["location"]["localtime"]
    temp_c = data["current"]["temp_c"]
    temp_condition = data["current"]["condition"]["text"]
    print(f"Performing request to Weather API for city {city}...")
    print(f"{city}/{country} {localtime} Weather: {temp_c} Celsius, {temp_condition}")


if __name__ == "__main__":
    get_weather()
