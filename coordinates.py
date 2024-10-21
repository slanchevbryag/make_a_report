import gpxpy
import staticmaps


def getting_coordinats(filepath_track):
    '''
    Эта функция получает координаты начальной точки трека
    из файла .gpx
    '''
    try:
        with open(filepath_track, "r") as file:
            gpx = gpxpy.parse(file)

        for point in gpx.walk(only_points=True):
            first_point = staticmaps.create_latlng(
                point.latitude, point.longitude)
            break

        return first_point

    except FileNotFoundError:
        print('Файл не найден')
        return None


if __name__ == '__main__':
    print(getting_coordinats('1_day.gpx'))
