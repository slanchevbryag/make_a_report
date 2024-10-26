import re

import coordinates

import print_to_doc

import track_image

import weather

day_date = input("Укажите дату в формате yyyy-MM-dd: ")
gpx_file_path = input("Укажите путь к файлу gpx: ")

starting_point = str(coordinates.get_starting_coordinates(gpx_file_path))

starting_point = re.findall(r'\d{2}\.\d{6}\,\d{2}\.\d{6}', starting_point)

weather_and_astro = weather.weather_by_terrain(starting_point, day_date)

print('Настройки миниатюры по-умолчанию ширина 500, длина 800, приближение 12')
thumbnail_sett = input("Хотите изменить настройки миниатюры карты? yes/no: ")

if thumbnail_sett == 'yes':

    img_width = int(input("Укажите ширину миниатюры карты: "))
    img_length = int(input("Укажите длинну миниатюры карты: "))
    zoom = int(input("Укажите величину приближения карты: "))

else:
    img_width = 500
    img_length = 800
    zoom = 12

track_image.track_image(gpx_file_path, img_width, img_length, zoom)

while thumbnail_sett:
    thumbnail_sett = input("Вам нравиться или хотите что-то изменить? yes/no: ")

    if thumbnail_sett == 'yes':

        img_width = int(input(
            f"Укажите ширину миниатюры карты (сейчас {img_width}): "))
        img_length = int(input(
            f"Укажите длинну миниатюры карты (сейчас {img_length}): "))
        zoom = int(input(
            f"Укажите величину приближения карты (сейчас {zoom}): "))
        track_image.track_image(gpx_file_path, img_width, img_length, zoom)

    else:
        break

print_to_doc.print_to_doc(weather_and_astro, day_date)
