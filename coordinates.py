import re


def getting_coordinats(filepath_track):
    '''
    Эта функция получает из файла .gpx координаты
    начальной и конечной точки трека.
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

        return first_point, last_point

    except FileNotFoundError:
        print('Файл не найден')
        return None


if __name__ == '__main__':
    print(getting_coordinats('/home/nausikaa/Learn_Python/project/make_a_report/tracks/1_day.gpx'))
