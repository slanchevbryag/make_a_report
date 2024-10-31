import re


def getting_coordinats(filepath_track):
    '''
<<<<<<< HEAD
    Эта функция получает из файла .gpx координаты
    начальной и конечной точки трека.
=======
    Эта функция получает координаты точек начала и конца трека
    из файла .gpx
>>>>>>> cd0c4ef30ed2b84d21112b0e58715d6c2aff57ae
    '''
    listpoint = []

    try:
        with open(filepath_track, 'r', encoding='utf-8') as f:
            for line in f:
                if "<trkpt" in line:
                    listpoint.append(line)

            if not listpoint:
                raise ValueError("Файл не содержит координат.")

        first_point = re.findall(r'\d{2}\.\d{6}', listpoint[0])
        last_point = re.findall(r'\d{2}\.\d{6}', listpoint[-1])
<<<<<<< HEAD

=======
>>>>>>> cd0c4ef30ed2b84d21112b0e58715d6c2aff57ae
        return first_point, last_point

    except FileNotFoundError:
        print('Файл не найден')
        return None


if __name__ == '__main__':
<<<<<<< HEAD
    print(getting_coordinats('/home/nausikaa/Learn_Python/project/make_a_report/tracks/1_day.gpx'))
=======
    print(getting_coordinats(
        '/home/nausikaa/Learn_Python/project/make_a_report/tracks/1_day.gpx'))
>>>>>>> cd0c4ef30ed2b84d21112b0e58715d6c2aff57ae
