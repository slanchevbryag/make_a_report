﻿import re


# эта функция получает координаты
# начальной и конечной точки пути
def getting_coordinats(filepath_track):

    listpoint = []

    try:  # открываем файл .gpx
        with open(filepath_track, 'r', encoding='utf-8') as f:
            for line in f:
                if "<trkpt" in line:  # и берём из него только строки
                    listpoint.append(line)  # с координатами точек трека

            if not listpoint:
                raise ValueError("Файл не содержит координат.")

        first_point = re.findall(r'\d{2}\.\d{6}', listpoint[0])
        # нам нужна первая и последняя строки
        last_point = re.findall(r'\d{2}\.\d{6}', listpoint[-1])
        # это кординаты начала и конца трека
        return first_point, last_point

    except FileNotFoundError:
        print('Файл не найден')
        return None


if __name__ == '__main__':
    print(getting_coordinats('c:\\projects\\make_a_report\\tracks\\1_day.gpx'))
