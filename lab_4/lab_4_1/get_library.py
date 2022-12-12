# импортируем необходимые модули
from jinja2 import Template
from jinja2 import Environment, FileSystemLoader
import sqlite3
from library_model import get_publisher, get_genre, get_reader, get_author, get_book_author
# устанавливаем соединение с базой данных (базу данных взять из ЛР 1)
conn = sqlite3.connect("library.sqlite")
# выбираем записи из таблицы publisher
df_publisher = get_publisher(conn)
df_genre = get_genre(conn)
df_reader = get_reader(conn)
df_author = get_author(conn)
df_book_author = get_book_author(conn)
# закрываем соединение с базой
conn.close()
# открываем шаблон из файла library_templ.html и читаем информацию
f_template = open('library_templ.html', 'r', encoding ='utf-8-sig')
html = f_template.read()
f_template.close()
# создаем объект-шаблон
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('library_templ.html')
# генерируем результат на основе шаблона
result_html = template.render(
    table_1 = "publisher",
    relation_1 = df_publisher,
    table_2 = "genre",
    relation_2 = df_genre,
    table_3 = "reader",
    relation_3 = df_reader,
    table_4 = "author",
    relation_4 = df_author,
    table_5 = "book_author",
    relation_5 = df_book_author,
    len = len
    )
# создаем файл для HTML-страницы
f = open('library.html', 'w', encoding ='utf-8-sig')
# выводим сгенерированную страницу в файл
f.write(result_html)
f.close()

