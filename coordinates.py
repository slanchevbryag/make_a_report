import re

def getting_coordinats(filepath_track): #эта функция получает координаты начальной и конечной точки пути
          
    listpoint = []

    with open(filepath_track, 'r', encoding='utf-8') as f: #открываем файл .gpx
        for line in f:
            if "<trkpt" in line:                           #и берём из него только строки с координатами точек трека
                listpoint.append(line)

    first_point = re.findall(r'\d\d.\d\d\d\d\d\d', listpoint[0])  #нам нужна первая и последняя строки 
    last_point = re.findall(r'\d\d.\d\d\d\d\d\d', listpoint[-1])  #это кординаты начала и конца трека 
    return first_point, last_point

if __name__=='__main__':
    print(getting_coordinats('c:\\projects\\make_a_report\\tracks\\1_day.gpx'))