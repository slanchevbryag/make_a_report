import requests
import config


def weather_by_terrain(point_coordinates, date):
    '''
    Эта функция делает запрос на сайт www.worldweatheronline.com,
    используя дату и координаты места.
    Из полученных данных формирует словарь с астрономическими
    данными, данными о max и min температуре и погодными явлениями.
    '''
    params = {
        "key": config.API_KEY,
        "q": point_coordinates,
        "date": date,
        "format": "json",
        "lang": "ru"
    }
    requests_of_weather = requests.get(config.weather_url, params=params)
    requests_of_weather.raise_for_status()
    weather = requests_of_weather.json()

    if "data" in weather:
        weather_data = weather["data"].get("weather", [{}])[0]
        if all(key in weather_data for key in ["astronomy",
                                               "maxtempC", "mintempC"]):
            try:
                weather_and_astro = weather_data["astronomy"][0]
                weather_and_astro["maxtempC"] = weather_data["maxtempC"]
                weather_and_astro["mintempC"] = weather_data["mintempC"]
                weather_and_astro["weatherDesc"] = weather_data["hourly"][4][
                                                        "lang_ru"][0]["value"]
                weather_and_astro["weatherDescIcon"] = weather_data["hourly"][
                                            4]["weatherIconUrl"][0]["value"]
                return weather_and_astro
            except (IndexError, TypeError):
                return False


if __name__ == '__main__':
    print(weather_by_terrain("54.497125,38.801394", "2024-07-08"))
