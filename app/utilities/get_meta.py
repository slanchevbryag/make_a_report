from datetime import datetime

from PIL import Image
from PIL.ExifTags import TAGS

import gpxpy

# import staticmaps


def get_meta_img(path_to_foto: str) -> str:
    '''
    Эта функция считывает метаданные с файлов .jpg и возвращает
    дату и время, когда была сделана фотография.
    '''

    image = Image.open(path_to_foto)

    exifdata = image.getexif()

    for tag_id_img in exifdata:
        tag_img = TAGS.get(tag_id_img, tag_id_img)
        if tag_img == "DateTime":
            data_img = exifdata.get(tag_id_img)

            return data_img


def get_date_gpx(gpx_path: str) -> str:
    '''
    Эта функция получает из файла трека, дату и время первой точки и возвращает
    дату ввиде строки.
    '''

    with open(gpx_path, "r") as file:
        gpx = gpxpy.parse(file)
    for point in gpx.walk(only_points=True):
        time = point.time
        break

    date_track = datetime.strftime(time, "%Y-%m-%d")
    return date_track
