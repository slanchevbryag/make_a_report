import os

from app.utilities.get_meta import get_date_gpx

import gpxpy
import gpxpy.geo
import gpxpy.gpx

import requests

import staticmaps


def ckeck_track_date(gpx_files_path: str, date: str) -> str:
    '''
    Эта функция проверяет есть ли в указанной папке треки за текущую дату и
    возвращает путь к найденному файлу или просит пользователя ввести его вручную.
    '''

    gpx_files = []
    exstension = (".gpx")

    for file_in_dir in os.listdir(path=gpx_files_path):
        if file_in_dir.lower().endswith(exstension):
            gpx_files.append(file_in_dir)

    if gpx_files == []:
        print("gpx файлы не найдены")
        return None

    for gpx_file in gpx_files:
        gpx_path = os.path.join(gpx_files_path, gpx_file)
        if date == get_date_gpx(gpx_path):
            return gpx_path

    for gpx_file in gpx_files:
        print(gpx_file)

    print("gpx файлы за данную дату не найдены.")

    while True:
        user_gpx_file = input("Введите имя файла из списка: ")

        if user_gpx_file in gpx_files:
            return os.path.join(gpx_files_path, user_gpx_file)
            break

        else:
            print(f'Файл {user_gpx_file} не найден в списке. Проверте регистр и указали ли вы расширение.')


def get_gpx_points_coord(gpx_file_path: str) -> float:
    '''
    Эта функция получает координаты начальной точуки трека
    из файла .gpx
    '''

    try:
        with open(gpx_file_path, "r") as file:
            gpx = gpxpy.parse(file)

    except FileNotFoundError:
        print(f'gpx файл не найден: {gpx_file_path}')
        return None

    for point in gpx.walk(only_points=True):
        starting_lat = point.latitude
        starting_long = point.longitude
        break
    return starting_lat, starting_long


def create_track_image(gpx_file_path: str, img_width: int = 500, img_length: int = 800, zoom: int = 12) -> float:
    '''
    Эта функция создаёт изображение, включающее в себя участок карты,
    где проходит текущий трек и сам трек с точками старта и финиша.
    '''

    context = staticmaps.Context()
    context.set_tile_provider(staticmaps.tile_provider_OSM)
    context.set_zoom(zoom)

    with open(gpx_file_path, "r") as file:
        gpx = gpxpy.parse(file)

    for track in gpx.tracks:
        for segment in track.segments:
            line = [staticmaps.create_latlng(
                p.latitude, p.longitude) for p in segment.points]
            context.add_object(staticmaps.Line(line, width=3))

    for point in gpx.walk(only_points=True):
        start_point = staticmaps.create_latlng(point.latitude, point.longitude)
        marker = staticmaps.ImageMarker(
            start_point, "start.png", origin_x=27, origin_y=5)
        context.add_object(marker)
        break

    for point in gpx.walk(only_points=True):
        finish_point = staticmaps.create_latlng(point.latitude, point.longitude)
    marker = staticmaps.ImageMarker(
        finish_point, "finish.png", origin_x=5, origin_y=35)
    context.add_object(marker)

    try:

        image = context.render_cairo(img_width, img_length)
        image.write_to_png("map.png")

    except requests.exceptions.ConnectionError:
        print('Ошибка подключения к OpenStreetMap')


def calc_distance(gpx_path: str) -> float:
    '''
    Эта функция считает пройденное расстояние.
    '''
    with open(gpx_path, "r") as file:
        gpx = gpxpy.parse(file)
        distance = gpx.length_2d()
        return round(distance/1000, 1)
