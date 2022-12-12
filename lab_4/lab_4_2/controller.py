from jinja2 import Template
import sqlite3
from model import *

reader_id = 3

conn = sqlite3.connect("library.sqlite")

df_book_reader = get_book_reader(conn, reader_id)
df_reader = get_reader(conn)

conn.close()

f_template = open('reader_book_template.html',
                  'r', encoding='utf-8-sig')
html = f_template.read()
f_template.close()

template = Template(html)

result_html = template.render(
    reader_id=reader_id,
    combo_box=df_reader,
    book_reader=df_book_reader,
    len=len
)

f = open('reader_book.html', 'w', encoding='utf-8-sig')

f.write(result_html)
f.close()
