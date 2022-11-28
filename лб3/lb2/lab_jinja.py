from jinja2 import Template, Environment

def add_spaces(text): 
    return " ".join(text) 

def discipline(n):
    strg = ""
    if n == 1:
        strg = "дисциплину"
    elif n > 1 and n < 5:
        strg = "дисциплины"
    else:
        strg = "дисциплин"
    return strg

f_template = open('ind_test_template.html','r', encoding ='utf-8-sig')
html = f_template.read()
f_template.close()

template = Template(html)

student =[
        ["Алина", "ж", "38.03.05", "Бизнес-информатика", ["Базы данных",
                                        "Программирование", "Статистика"]],
        ["Вадим","м", "38.03.01", "Экономика", ["Информатика", "Теория игр",
                                "Статистика"]],
        ["Ксения","ж", "38.03.01", "Экономика", ["Информатика", "Теория игр",
        "Статистика"]]
        ]

template.globals["add_spaces"] = add_spaces
template.globals["discipline"] = discipline
template.globals["len"] = len 

result_html = template.render(user = student, ind = 0)

#создадим файл для HTML-страницы
f = open('test.html', 'w', encoding ='utf-8-sig')
# выводим сгенерированную страницу в файл
f.write(result_html)
f.close()
