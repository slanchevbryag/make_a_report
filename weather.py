import requests
import config

def weather_by_terrain(point_coordinates, date):  #эта функция делает запрос на сайт погоды и помещает в словарь нужные нам параметры
    weather_url = "http://api.worldweatheronline.com/premium/v1/past-weather.ashx"
    params = {
        "key": config.API_KEY,
        "q": point_coordinates,
        "date": date,
        "format": "json",
        "lang": "ru"
    }   
    requests_of_weather = requests.get(weather_url, params=params)
    weather = requests_of_weather.json()
    
    if "data" in weather:
        if "weather" in weather["data"]:
            if "astronomy" and "maxtempC" and "mintempC" in weather["data"]["weather"][0]:
                try:
                    weather_and_astro = weather["data"]["weather"][0]["astronomy"][0]
                    weather_and_astro["maxtempC"] = weather["data"]["weather"][0] ["maxtempC"]
                    weather_and_astro["mintempC"] = weather["data"]["weather"][0] ["mintempC"]
                    weather_and_astro["weatherDesc"] = weather["data"]["weather"][0]["hourly"][4]["lang_ru"][0]["value"]
                    weather_and_astro["weatherDescIcon"] = weather["data"]["weather"][0]["hourly"][4]["weatherIconUrl"][0]["value"]
                    return weather_and_astro
                except(IndexError, TypeError):
                    return False
    
                
if __name__=='__main__':
    print(weather_by_terrain("54.497125,38.801394","2024-07-08"))