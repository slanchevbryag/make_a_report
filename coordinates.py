import gpxpy

import staticmaps


def get_starting_coordinates(gpx_file_path):
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


if __name__ == '__main__':
    print(get_starting_coordinates('1_day.gpx'))
