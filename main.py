import coordinates
import weather
import track_image
import print_to_doc

date = input("Укажите дату в формате yyyy-MM-dd: ")
filepath_track = input("Укажите путь к файлу gpx: ")

first_point = coordinates.getting_coordinats(filepath_track)

weather_and_astro = weather.weather_by_terrain(first_point, date)

print('Настройки миниатюры по-умолчанию ширина 500, длина 800, приближение 12')
thumbnail_sett = input("Хотите изменить настройки миниатюры карты? y/n: ")

if thumbnail_sett == 'y':

    img_width = int(input("Укажите ширину миниатюры карты: "))
    img_length = int(input("Укажите длинну миниатюры карты: "))
    zoom = int(input("Укажите величину приближения карты: "))

else:
    img_width = 500
    img_length = 800
    zoom = 12

track_image.track_image(filepath_track, img_width, img_length, zoom)

while thumbnail_sett:
    thumbnail_sett = input("Вам нравиться или хотите что-то изменить? y/n: ")

    if thumbnail_sett == 'y':

        img_width = int(input(
            f"Укажите ширину миниатюры карты (сейчас {img_width}): "))
        img_length = int(input(
            f"Укажите длинну миниатюры карты (сейчас {img_length}): "))
        zoom = int(input(
            f"Укажите величину приближения карты (сейчас {zoom}): "))
        track_image.track_image(filepath_track, img_width, img_length, zoom)

    else:
        break

print_to_doc.print_to_doc(weather_and_astro, date)
