import constants
from app import app
from flask import render_template, request
@app.route('/', methods=['GET'])
def index():
    name = ""
    gender = ""
    program_id = 0
    # список из номеров выбранных пользователем дисциплин
    subject_id = []
    olimp_id = []
    # список из выбранных пользователем дисциплин
    subjects_select = []
    olimp_select = []
    # выводим форму
    btn_is_clicked = False
    if request.values.get('clicked'):
        btn_is_clicked = True
        name = request.values.get('username')
        gender = request.values.get('gender')
        program_id = request.values.get('program')
        subject_id = request.values.getlist('subject[]')
        olimp_id = request.values.getlist('olimp[]')
        # формируем список из выбранных пользователем дисциплин
        subjects_select = [constants.subjects[int(i)] for i in subject_id]
        olimp_select = [constants.olimps[int(i)] for i in olimp_id]
    html = render_template(
        'index.html',
        program_list = constants.programs,
        subject_list = constants.subjects,
        len = len,
        range = range,
        name = name,
        gender = gender,
        program = constants.programs[int(program_id)],
        subjects_select = subjects_select,
        olimp_select = olimp_select,
        olimp_list = constants.olimps,
        btn_is_clicked = btn_is_clicked
    )

    return html
