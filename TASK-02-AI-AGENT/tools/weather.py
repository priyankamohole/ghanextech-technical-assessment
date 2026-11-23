
import requests

from langchain.tools import tool
from pydantic import BaseModel, Field


class WeatherInput(BaseModel):
    city: str = Field(
        description="Name of the city for which current weather is required."
    )


GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
WEATHER_URL = "https://api.open-meteo.com/v1/forecast"


WEATHER_CODES = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Fog",
    48: "Depositing rime fog",
    51: "Light drizzle",
    53: "Moderate drizzle",
    55: "Dense drizzle",
    61: "Slight rain",
    63: "Moderate rain",
    65: "Heavy rain",
    71: "Slight snowfall",
    73: "Moderate snowfall",
    75: "Heavy snowfall",
    80: "Rain showers",
    81: "Moderate rain showers",
    82: "Violent rain showers",
    95: "Thunderstorm",
    96: "Thunderstorm with hail",
    99: "Heavy thunderstorm with hail",
}


@tool(args_schema=WeatherInput)
def get_weather(city: str) -> str:
    """
    Fetches current weather conditions for a city.

    Use when the user asks about current weather,
    temperature, humidity, rainfall, or wind conditions.
    """

    try:
        city = city.strip()

        if not city or len(city) > 100:
            return "Error: Please provide a valid city name."

        geo_response = requests.get(
            GEOCODING_URL,
            params={
                "name": city,
                "count": 1,
                "language": "en",
                "format": "json"
            },
            timeout=10
        )

        geo_response.raise_for_status()

        locations = geo_response.json().get("results", [])

        if not locations:
            return f"Error: Could not find the location '{city}'."

        location = locations[0]

        latitude = location["latitude"]
        longitude = location["longitude"]

        weather_response = requests.get(
            WEATHER_URL,
            params={
                "latitude": latitude,
                "longitude": longitude,
                "current": (
                    "temperature_2m,"
                    "relative_humidity_2m,"
                    "apparent_temperature,"
                    "precipitation,"
                    "weather_code,"
                    "wind_speed_10m"
                ),
                "timezone": "auto"
            },
            timeout=10
        )

        weather_response.raise_for_status()

        data = weather_response.json()
        current = data.get("current")

        if not current:
            return "Error: Current weather data is unavailable."

        code = current.get("weather_code")

        description = WEATHER_CODES.get(
            code,
            "Unknown weather condition"
        )

        return (
            f"Weather for {location['name']}, "
            f"{location.get('country', 'Unknown country')}:\n"
            f"Temperature: {current['temperature_2m']} °C\n"
            f"Feels like: {current['apparent_temperature']} °C\n"
            f"Humidity: {current['relative_humidity_2m']}%\n"
            f"Wind speed: {current['wind_speed_10m']} km/h\n"
            f"Precipitation: {current['precipitation']} mm\n"
            f"Condition: {description}\n"
            f"Observation time: {current['time']} "
            f"({data.get('timezone', 'local timezone')})"
        )

    except requests.exceptions.Timeout:
        return "Error: Weather service timed out. Please try again."

    except requests.exceptions.RequestException:
        return "Error: Unable to connect to the weather service."

    except (KeyError, ValueError, TypeError):
        return "Error: Unexpected weather data received."

    except Exception:
        return "Error: Something went wrong while fetching weather."
