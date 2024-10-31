import re
import sys

import app.moduls.coordinates as coordinates
import app.moduls.print_to_doc as print_to_doc
import app.moduls.track_image as track_image
import app.moduls.weather as weather
from app.moduls.draft import create_a_draft, get_audio_files, get_user_notes

date = input("Укажите дату в формате yyyy-MM-dd: ")
gpx_file_path = input("Укажите путь к файлу gpx: ")

starting_point = coordinates.get_starting_coordinates(gpx_file_path)

if starting_point is None:
    sys.exit(1)

starting_point = re.findall(r'\d{2}\.\d{6}', str(starting_point))
starting_point = ','.join(starting_point)

weather_and_astro = weather.weather_by_terrain(starting_point, date)

print('Настройки миниатюры по-умолчанию ширина 500, длина 800, приближение 12')
thumbnail_sett = input("Хотите изменить настройки миниатюры карты? да/нет: ")

if thumbnail_sett.lower() == 'да':

    img_width = int(input("Укажите ширину миниатюры карты: "))
    img_length = int(input("Укажите длинну миниатюры карты: "))
    zoom = int(input("Укажите величину приближения карты: "))

else:
    img_width = 500
    img_length = 800
    zoom = 12

track_image.create_track_image(gpx_file_path, img_width, img_length, zoom)

while thumbnail_sett:
    thumbnail_sett = input("Вам нравиться или хотите что-то изменить? да/нет: ")

    if thumbnail_sett.lower() == 'да':

        img_width = int(input(
            f"Укажите ширину миниатюры карты (сейчас {img_width}): "))
        img_length = int(input(
            f"Укажите длинну миниатюры карты (сейчас {img_length}): "))
        zoom = int(input(
            f"Укажите величину приближения карты (сейчас {zoom}): "))
        track_image.create_track_image(gpx_file_path, img_width, img_length, zoom)

    else:
        break

print_to_doc.print_weather(weather_and_astro, date, img_width, img_length)

audio_file_path = input("Укажите путь к файлам аудио заметок: ")

list_audio_files = get_audio_files(audio_file_path, date)

if len(list_audio_files) == 2:
    recognized_audio_files = list_audio_files[1]
    create_a_draft(recognized_audio_files, date)

else:

    for audio_file in list_audio_files:
        print(audio_file)

    while True:
        user_files = input("Введите через запятую названия файлов вручную, используя список выше: ")

        trake_notes = get_user_notes(user_files, audio_file_path, list_audio_files)
        if trake_notes is None:
            continue
        else:
            create_a_draft(trake_notes, date)
            break

print('Откройте файл draft и сделайти правки в черновике.')
draft_edits = input('Вы готовы внести ваши путевые заметки в отчёт? да/нет: ')

if draft_edits.lower() == "да":
    print_to_doc.print_travel_notes(img_width, img_length)
