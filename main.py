import coordinates
import weather
import track_image
import print_to_doc

date = input("Укажите дату в формате yyyy-MM-dd: ")
filepath_track = input("Укажите путь к файлу gpx: ")

first_point = coordinates.getting_coordinats(filepath_track)

weather_and_astro = weather.weather_by_terrain(first_point, date)

print_to_doc.print_to_doc(weather_and_astro, date)

track_image.track_image(filepath_track)
