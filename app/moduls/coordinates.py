import gpxpy


def get_starting_coordinates(gpx_file_path: str) -> float:
    '''
    Эта функция получает координаты начальной точки трека
    из файла .gpx
    '''
    try:
        with open(gpx_file_path, "r") as file:
            gpx = gpxpy.parse(file)

        for point in gpx.walk(only_points=True):
            starting_lat = point.latitude
            starting_long = point.longitude
            break
        return starting_lat, starting_long

    except FileNotFoundError:
        print('Файл не найден')
        return None
