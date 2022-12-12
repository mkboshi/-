from jinja2 import Template
import sqlite3
from model import *

genre_ids = (1, 2, 4)
author_ids = (0, 2, 3)
publisher_ids = (0, 1, 2, 4, 5)

conn = sqlite3.connect("library.sqlite")

df_genre = get_genre(conn)
df_author = get_author(conn)
df_publisher = get_publisher(conn)
df_book = get_book(conn, genre_ids, author_ids, publisher_ids)

conn.close()

f_template = open('book_template.html', 'r', encoding='utf-8-sig')
html = f_template.read()
f_template.close()

template = Template(html)

result_html = template.render(
    genre=df_genre,
    genre_ids=genre_ids,
    author=df_author,
    author_ids=author_ids,
    publisher=df_publisher,
    publisher_ids=publisher_ids,
    book=df_book,
    len=len
)

f = open('book.html', 'w', encoding='utf-8-sig')

f.write(result_html)
f.close()
