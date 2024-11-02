import os

from app.utilities.get_meta import get_meta_img


def get_foto(path_to_files: str, date: str) -> list:
    '''
    Эта функция отбирает jpeg файлы из папки пользователя, даты съёмки которых
    совпадают с текущей датой. При неудаче возвращает None.
    Пока только jpeg.
    '''

    jpg_files_with_path = []
    jpg_files_with_date = []
    exstension = (".jpg", ".jpeg")

    date_in_name = date.replace("-", ":")

    for file_in_dir in os.listdir(path=path_to_files):
        if file_in_dir.lower().endswith(exstension):
            path_to_foto = os.path.join(path_to_files, file_in_dir)
            jpg_files_with_path.append(path_to_foto)

    if jpg_files_with_path == []:
        print("JPG файлы не найдены")
        return None

    for path_to_foto in jpg_files_with_path:
        datetime_in_foto = get_meta_img(path_to_foto)
        if date_in_name in datetime_in_foto:
            jpg_files_with_date.append(path_to_foto)

    if jpg_files_with_date == []:
        print("Файлы за данную дату не найдены.")
        return None

    jpg_files_with_date.sort()
    return jpg_files_with_date
