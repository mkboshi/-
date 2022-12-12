import pandas as pd


def get_reader(conn):
    return pd.read_sql("SELECT * FROM reader", conn)


def get_book_reader(conn, reader_id):
    return pd.read_sql(f'''
        SELECT title AS Книга, group_concat(DISTINCT author_name) AS Авторы, borrow_date AS Дата_выдачи, return_date AS Дата_возврата
        FROM
            book_reader
            JOIN book USING (book_id)
            JOIN book_author USING (book_id)
            JOIN author USING (author_id)
        WHERE reader_id = {reader_id}
        GROUP BY book_id
        ORDER BY title
    ''', conn)
