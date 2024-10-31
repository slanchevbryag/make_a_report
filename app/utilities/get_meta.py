from PIL import Image
from PIL.ExifTags import TAGS


def get_meta_img(foto_file_path):

    image = Image.open(foto_file_path)

    exifdata = image.getexif()

    for tag_id_img in exifdata:
        tag_img = TAGS.get(tag_id_img, tag_id_img)
        data_img = exifdata.get(tag_id_img)
        if isinstance(data_img, bytes):
            data_img = data_img.decode()
        print(f"{tag_img:25}:% {data_img}")


if __name__ in '__main__':
    get_meta_img('test_files/pic.jpg')
