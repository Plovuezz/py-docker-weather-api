import os
import sys
from typing import Any

import requests
from requests import RequestException
from dotenv import load_dotenv


def validate(smth: Any) -> None:
    if smth is None:
        print(f"Error occurred")
        sys.exit(1)


def get_weather() -> None:
    load_dotenv()

    api_key = os.environ.get("API_KEY")
    q_param = os.environ.get("Q_PARAM")

    if not api_key:
        print("API key not found. Please set _API_KEY in .env")
        sys.exit(1)
    if not q_param:
        print("Q parameter not found. Please set Q_PARAM in .env")
        sys.exit(1)

    url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={q_param}"

    try:
        r = requests.get(url)
        data = r.json()
    except RequestException as e:
        print(f"Error occurred: {e}")
        sys.exit(1)

    location = data.get("location")
    validate(location)
    current = data.get("current")
    validate(current)

    city = location.get("name")
    validate(city)

    country = location.get("country")
    validate(country)

    time = location.get("localtime")
    validate(time)

    temperature = current.get("temp_c")
    validate(temperature)

    condition = current.get("condition").get("text")
    validate(condition)

    print(f"{country}/{city} {time} Weather: {temperature} {condition}")


if __name__ == "__main__":
    get_weather()
