import coordinates
import weather

date = input("Укажите дату в формате yyyy-MM-dd: ")
filepath_track = input("Укажите путь к файлу gpx: ")

point = coordinates.getting_coordinats(filepath_track)
point_coordinates = point[0]
point_coordinates = " ".join(point_coordinates)

weather_and_astro = weather.weather_by_terrain(point_coordinates, date)

print(f"Дата: {date}")
print(f"Восход: {weather_and_astro['sunrise']}")
print(f"Закат: {weather_and_astro['sunset']}")
print(f"Max температура: {weather_and_astro['maxtempC']} С")
print(f"Min температура: {weather_and_astro['mintempC']} С")
print(weather_and_astro["weatherDesc"])
