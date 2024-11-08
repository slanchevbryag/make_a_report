# Создание отчёта по туристическому походу (пункт Техническое описание).

Программа формирует отчёт по туристическому походу (пункт Техническое описание) используя данные пользователя и сохраняет его в документе с расширением docx.

## Установка

Скачайте проект с github:

```
git clone https://github.com/Slanchevbryag/make_a_report.git
```

Создайте виртуальное окружение и установите зависимости:

```
pip install -r requirements.txt
```

Создайте файл config.py и создайте в нём базовые переменные:

```
API_KEY = "API ключ с сайта worldweatheronline.com"
weather_url = "http://api.worldweatheronline.com/premium/v1/past-weather.ashx"
```

## Запуск программы

Для запуска программы запустите файл `make_a_report.py`. Введите дату начала похода, дату окончания, пути к файлам с аудио заметками и фото и введите путь к файлу с треком (для проверки есть папка test_files).

Программа предложет задать настройки миниатюры с картой, введите 'нет', программы возьмёт настройки по-умолчанию, создат файл map.png и спросит, хотите ли вы поменять настройки.

Если результат вас удовлетворил введите 'нет', если нет, введите 'да' и поменяйте настройки.

Затем программа создат файл report.docx.

Далее програма попытается считать дату, когда была сделана запись аудио заметок, из названия файла.
Если она найдёт файлы с текущей датой, программа транскрибирует их и создаст файл draft.txt.
Если таких файлов не окажется, то будет предложено пользователю самому ввести названия файлов аудио заметок.

После программа предложит отредактировать файл draft.txt и добавит результат к отчёту.

Делее программа попытается считать дату съёмки фото из метаданных. При удаче, все файлы с текущей датой будут скопированы в папку temp, иначе будет предложено поместить файлы в папку temp вручную. 

Изображения из временной папке будут вставлены в отчёт, а папка удалена.

Программа будет повторять операции для каждого дня похода и добавлять результат к отчёту.
