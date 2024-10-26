import os

import utilities.transcription as tr


def trake_notes_draft(audio_file_path, date):

    audio_files = []

    try:
        for files_in_dir in os.walk(audio_file_path):
            for file_in_dir in files_in_dir[2]:
                if file_in_dir.endswith(".mp3", ".wav", ".aac", ".flac", ".m4a", ".ogg"):
                    audio_file = os.path.join(audio_file_path, file_in_dir)
                    audio_files.append(audio_file)

    except FileNotFoundError:
        print("Файл не найден")
        return None

    audio_files.sort()

    with open("draft.txt", "w", encoding="utf-8") as f:
        f.write(f"Дата: {date}")

    try:
        for audio_file in audio_files:
            note = tr.get_travel_notes(audio_file=audio_file)

            with open("draft.txt", "a", encoding="utf-8") as f:
                f.write(f"\n{note}")

    except Exception:
        print("Упс! Что-то пошло не так!")
        return None


if __name__ in "__main__":
    trake_notes_draft("test_files", "2022-06-15")
