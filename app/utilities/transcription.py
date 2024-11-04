import whisper


def get_travel_notes(audio_file: str) -> str:
    '''
    Эта функция транскрибирует аудио файлы.
    '''

    model_name = 'turbo'
    model = whisper.load_model(model_name)

    travel_note = model.transcribe(audio_file)
    return travel_note["text"]
