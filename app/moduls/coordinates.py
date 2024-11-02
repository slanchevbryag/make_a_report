import gpxpy

import s2sphere

import staticmaps


def get_starting_coordinates(gpx_file_path: str) -> s2sphere.LatLng:
    '''
    Эта функция получает координаты начальной точки трека
    из файла .gpx
    '''
    try:
        with open(gpx_file_path, "r") as file:
            gpx = gpxpy.parse(file)

        for point in gpx.walk(only_points=True):
            starting_point = staticmaps.create_latlng(
                point.latitude, point.longitude)

            break
        return starting_point

    except FileNotFoundError:
        print('Файл не найден')
        return None
