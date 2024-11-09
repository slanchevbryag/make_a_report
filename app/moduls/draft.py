import os

import app.utilities.transcription as tr


def get_audio_files(audio_file_path: str, date: str) -> list:
    '''
    Эта функция находит в указанной папке аудио файлы и создаёт их список.
    Затем пробует найти в названиях файлов текущую дату и создаёт список путей к этим файлам.
    '''

    audio_files = []
    audio_files_with_date = []
    exstension = (".mp3", ".wav", ".aac", ".flac", ".m4a", ".ogg", ".wma", ".mp4")

    date_in_name = date.replace("-", "")

    for file_in_dir in os.listdir(path=audio_file_path):
        if file_in_dir.lower().endswith(exstension):
            audio_files.append(file_in_dir)

    if audio_files == []:
        print(f"Аудио файлы не найдены: {audio_file_path}")
        return None

    for audio_file in audio_files:
        if date_in_name in audio_file:
            audio_file_with_date = os.path.join(audio_file_path, audio_file)
            audio_files_with_date.append(audio_file_with_date)

    if audio_files_with_date == []:
        print("Аудио файлы за данную дату не найдены.")
        audio_files.sort()
        return audio_files

    audio_files_with_date.sort()
    return audio_files, audio_files_with_date


def create_a_draft(recognized_audio_files: list) -> None:
    '''
    Эта функция передаёт поочереди файлы с аудио заметками из полученного списка
    в функцию transcription и помещает полученный текст в файл черновика.
    '''

    with open("draft.txt", "w", encoding="utf-8") as f:
        f.write("")

    try:
        for audio_file in recognized_audio_files:
            note = tr.get_travel_notes(audio_file)

            with open("draft.txt", "a", encoding="utf-8") as f:
                f.write(f"\n{note}")

    except Exception as err:
        print("Упс! Что-то пошло не так!")
        print(f'An error occurred: {err}')
        return None


def get_user_notes(user_files: str, audio_file_path: str, list_audio_files: list) -> list:
    '''
    Эта функция из перечня файлов пользователя создаёт список и сравнивает названия с уже
    сформированным списком аудио файлов. Если такой файл в папке есть, она заносит
    его в список, добавляя путь.
    '''

    audio_files_no_date = []
    notes = user_files.split(",")

    for user_audio_file in notes:

        if user_audio_file.strip() in list_audio_files:
            audio_file_no_date = os.path.join(audio_file_path, user_audio_file.strip())
            audio_files_no_date.append(audio_file_no_date)
        else:
            print(f'Файл {user_audio_file} не найден в списке. Проверте регистр.')
            return None

    return audio_files_no_date
