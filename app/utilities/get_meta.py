from PIL import Image
from PIL.ExifTags import TAGS


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
