# src/main.py
import math
import os
import re
import requests as req

WEATHER_REQUEST_URL = "https://api.openweathermap.org/data/2.5/weather?id={}&units={}&mod=json&appid={}"

WEATHER_TEMPLATE="""<h3>Hello from {} province of <img src="https://flagicons.lipis.dev/flags/4x3/{}.svg" width="28" height="21"/></h3>
<p>Currently, the weather is: <b> {}°{}, <img src="https://openweathermap.org/img/wn/{}.png" width="28" height="28" title= "Weather Icon" alt="Weather Icon"> <i>({})</i></b></br>Today, the sun rises at <b>{}</b> and sets at <b>{}</b>.</p>"""

def refresh_contents(old_content, new_content):
    r = re.compile(r'<!\-\- WEATHER:START \-\->((.|\n)*)<!\-\- WEATHER:END \-\->', re.DOTALL)
    new_content_formated = '<!-- WEATHER:START -->\n{}\n<!-- WEATHER:END -->'.format(new_content)
    return r.sub(new_content_formated, old_content)

def prepare_url(city_id, units, weather_api_key):
    global WEATHER_REQUEST_URL
    WEATHER_REQUEST_URL = WEATHER_REQUEST_URL.format(city_id, 'imperial' if units == 'f' else 'metric', weather_api_key)

def prepare_template(city, country_code, temp, units, icon, desc, sunrise, sunset):
    global WEATHER_TEMPLATE
    WEATHER_TEMPLATE = WEATHER_TEMPLATE.format(city, country_code, temp, units.capitalize(), icon, desc, sunrise, sunset)

def make_request():
    try:
        response = req.get(WEATHER_REQUEST_URL)
        response.raise_for_status()
    except req.exceptions.HTTPError as error:
        print(error)

    return response.json()

def main():

    try:
        WEATHER_API_KEY = os.environ["INPUT_WEATHER_API_KEY"]
    except KeyError:
        WEATHER_API_KEY = "Token not available!"

    try:
        CITY_ID = os.environ["INPUT_CITY_ID"]
    except KeyError:
        CITY_ID = "Token not available!"

    try:
        UNITS = os.environ["INPUT_UNITS"]
    except KeyError:
        UNITS = "Token not available!"

    try:
        COUNTRY_CODE = os.environ["INPUT_COUNTRY_CODE"]
    except KeyError:
        COUNTRY_CODE = "Token not available!"

    try:
        README_PATH = os.environ["README_PATH"]
    except KeyError:
        README_PATH = "Token not available!"

    prepare_url(CITY_ID, UNITS, WEATHER_API_KEY)
    api_data_json = make_request()

    city = api_data_json['name']
    temp = math.ceil(api_data_json['main']['temp'])
    icon = api_data_json['weather'][0]['icon']
    desc = api_data_json['weather'][0]['description']
    sunrise = api_data_json['sys']['sunrise']
    sunset = api_data_json['sys']['sunset']

    prepare_template(city, COUNTRY_CODE, temp, UNITS, icon, desc, sunrise, sunset)

    with open(README_PATH, 'r', encoding='utf-8') as fr:
        readme = fr.read()

    readme_new = refresh_contents(readme, WEATHER_TEMPLATE)

    with open(README_PATH, mode="w", encoding="utf-8") as fw:
        fw.write(readme_new)

if __name__ == "__main__":
    main()
