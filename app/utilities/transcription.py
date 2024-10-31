import whisper


def get_travel_notes(audio_file: str) -> str:
    '''
    Эта функция транскрибирует аудио файлы.
    '''

    model_name = 'base'
    model = whisper.load_model(model_name)

    travel_note = model.transcribe(audio_file)
    return travel_note["text"]


if __name__ in '__main__':
    print(get_travel_notes('test_files/audio.m4a'))
