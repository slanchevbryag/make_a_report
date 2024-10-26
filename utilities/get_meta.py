from PIL import Image
from PIL.ExifTags import TAGS


def get_meta_img(imagename):

    # читать данные изображения с помощью PIL
    image = Image.open(imagename)

    # извлечь данные EXIF
    exifdata = image.getexif()

    # перебор всех полей данных EXIF
    for tag_id in exifdata:
        # получить имя тега вместо нечитаемого идентификатора
        tag = TAGS.get(tag_id, tag_id)
        data = exifdata.get(tag_id)
        # декодировать байты
        if isinstance(data, bytes):
            data = data.decode()
        print(f"{tag:25}:% {data}")


if __name__ in '__main__':
    get_meta_img('test_files/20220712_162726.jpg')
