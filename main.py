import os
import shutil
import sys

from app.moduls.draft import create_a_draft, get_audio_files, get_user_notes
from app.moduls.foto import get_foto
from app.moduls.print_to_doc import print_foto, print_travel_notes, print_weather_and_trake
from app.moduls.track_and_coordinates import create_track_image, get_starting_coordinates
from app.moduls.weather import weather_by_terrain

date = input("Укажите дату в формате yyyy-MM-dd: ")
gpx_file_path = input("Укажите путь к файлу gpx: ")

starting_point = get_starting_coordinates(gpx_file_path)

if starting_point is None:
    sys.exit(1)

starting_point = ",".join(str(elem) for elem in starting_point)

weather_and_astro = weather_by_terrain(starting_point, date)

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

distance = create_track_image(gpx_file_path, img_width, img_length, zoom)

while thumbnail_sett:
    thumbnail_sett = input("Вам нравиться или хотите что-то изменить? да/нет: ")

    if thumbnail_sett.lower() == 'да':

        img_width = int(input(
            f"Укажите ширину миниатюры карты (сейчас {img_width}): "))
        img_length = int(input(
            f"Укажите длинну миниатюры карты (сейчас {img_length}): "))
        zoom = int(input(
            f"Укажите величину приближения карты (сейчас {zoom}): "))
        create_track_image(gpx_file_path, img_width, img_length, zoom)

    else:
        break

print_weather_and_trake(weather_and_astro, date, img_width, img_length, distance)

audio_file_path = input("Укажите путь к файлам аудио заметок: ")

list_audio_files = get_audio_files(audio_file_path, date)

try:
    if list_audio_files[1][0]:
        recognized_audio_files = list_audio_files[1]
        create_a_draft(recognized_audio_files)

except IndexError:
    for audio_file in list_audio_files:
        print(audio_file)

    while True:
        user_files = input("Введите через запятую названия файлов вручную, используя список выше: ")

        trake_notes = get_user_notes(user_files, audio_file_path, list_audio_files)
        if trake_notes is None:
            continue
        else:
            create_a_draft(trake_notes)
            break

print('Откройте файл draft и сделайти правки в черновике.')
draft_edits = input('Вы готовы внести ваши путевые заметки в отчёт? да/нет: ')

if draft_edits.lower() == "да":
    print_travel_notes(img_width, img_length)

path_to_foto = input("Укажите путь к файлам с фото: ")

list_of_fotofiles = get_foto(path_to_foto, date)

os.makedirs('temp', exist_ok=True)

if list_of_fotofiles is None:
    print("Добавьте файлы в папку temp в ручную")

num_file = 1
while num_file <= len(list_of_fotofiles):
    for fotofile in list_of_fotofiles:
        temp_path = os.path.join('temp', f'{num_file}.jpg')
        shutil.copy2(fotofile, temp_path)
        num_file += 1

print("В папке temp оставьте только те фото, которые хотите добавить в отчёт")
done_img = input("Вы готовы добавить фото в отчёт да/нет: ")

if done_img.lower() == "да":
    print_foto()
else:
    print("Фото не занесены в отчёт")

shutil.rmtree("temp")
