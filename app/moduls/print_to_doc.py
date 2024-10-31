from typing import Any

from app.utilities import float_img

import docx
from docx.shared import Mm


def print_weather(weather_and_astro: dict[str, Any], date: str, img_width: int, img_length: int) -> None:
    """
    Эта функция создаёт документ с отчётом и заносит в него миниатюру карты
    с треком и астрономические и погодные данные.
    """

    doc = docx.Document()

    doc.add_heading("Техническое описание", 0)
    doc.add_heading("1 день", 1)

    try:
        mini_map = doc.add_paragraph()

        if img_length > img_width:

            float_img.add_float_picture(
                mini_map, "map.png", width=Mm(50), pos_x=Mm(30), pos_y=Mm(60),
            )

        else:

            float_img.add_float_picture(
                mini_map, "map.png", width=Mm(80), pos_x=Mm(30), pos_y=Mm(60),
            )

    except FileNotFoundError:
        print('Файл не найден')
        mini_map = doc.add_paragraph()
        float_img.add_float_picture(
            mini_map, "dead_smiley.png", width=Mm(50), pos_x=Mm(30), pos_y=Mm(60),
        )

    par3 = doc.add_paragraph("  Дата: ")
    doc.paragraphs[3].runs[0].bold = True
    par3.add_run(date)

    par4 = doc.add_paragraph("  Восход: ")
    doc.paragraphs[4].runs[0].bold = True
    par4.add_run(weather_and_astro["sunrise"])
    par4.add_run("  Закат: ").bold = True
    par4.add_run(weather_and_astro["sunset"])

    par5 = doc.add_paragraph("  Max температура: ")
    doc.paragraphs[5].runs[0].bold = True
    par5.add_run(f'{weather_and_astro['maxtempC']} C')

    par6 = doc.add_paragraph("  Min температура: ")
    doc.paragraphs[6].runs[0].bold = True
    par6.add_run(f'{weather_and_astro['mintempC']} C')

    par7 = doc.add_paragraph()
    par7.add_run(f'  {weather_and_astro['weatherDesc']}')

    doc.save("report.docx")


def print_travel_notes(img_width: int, img_length: int) -> None:
    '''
    Эта функция добавляет в файл отчёта путевые заметки.
    '''

    with open('draft.txt', 'r', encoding='utf-8') as d:
        draft = d.read()

    doc = docx.Document("report.docx")

    if img_length > img_width:

        for _ in range(1, 4):
            _ = doc.add_paragraph()

    par_draft = doc.add_paragraph()
    par_draft.add_run(draft)

    doc.save("report.docx")
