import gpxpy
import gpxpy.geo
import gpxpy.gpx

import requests

import staticmaps


def get_start_finish_coordinates(gpx_file_path: str) -> float:
    '''
    Эта функция получает координаты начальной и конечной точук трека
    из файла .gpx
    '''
    try:
        with open(gpx_file_path, "r") as file:
            gpx = gpxpy.parse(file)

    except FileNotFoundError:
        print('Файл не найден')
        return None

    for point in gpx.walk(only_points=True):
        starting_lat = point.latitude
        starting_long = point.longitude
        break

    for point in gpx.walk(only_points=True):
        finish_point_lat = point.latitude
        finish_point_long = point.longitude

    return starting_lat, starting_long, finish_point_lat, finish_point_long


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


def calc_distance(
        start_point_lat: float, start_point_long: float, finish_point_lat: float, finish_point_long: float) -> float:
    '''
    Эта функция подсчитывает пройденную дистанцию.
    '''

    distance = gpxpy.geo.haversine_distance(start_point_lat, start_point_long, finish_point_lat, finish_point_long)
    distance = round(distance/1000, 1)

    return distance
