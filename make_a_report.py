from datetime import datetime, timedelta

import docx

from main import apply_travel_foto_one_day, apply_travel_notes_one_day, weathe_and_track_one_day

first_day = input("Введите дату начала похода в формате yyyy-MM-dd: ")
end_day = input("Введите дату окончания похода в формате yyyy-MM-dd: ")
first_day = datetime.strptime(first_day, "%Y-%m-%d").date()
end_day = datetime.strptime(end_day, "%Y-%m-%d").date()

gpx_files_path = input("Укажите путь к файлам gpx: ")
audio_file_path = input("Укажите путь к файлам аудио заметок: ")
path_to_foto = input("Укажите путь к файлам с фото: ")

doc = docx.Document()
doc.add_heading("Техническое описание", 0)
doc.save("report.docx")

for days_travels in range((end_day - first_day).days + 1):
    travel_day = first_day + timedelta(days_travels)
    date = datetime.strftime(travel_day, "%Y-%m-%d")

    thumbnail_size = weathe_and_track_one_day(date, days_travels, gpx_files_path)
    apply_travel_notes_one_day(date, audio_file_path, thumbnail_size[0], thumbnail_size[1])
    apply_travel_foto_one_day(date, path_to_foto)
