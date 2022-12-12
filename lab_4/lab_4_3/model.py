import pandas as pd


def get_genre(conn):
    return pd.read_sql('''
    SELECT genre_id, genre_name, sum(available_numbers) AS cnt
    FROM 
	    book
        JOIN genre USING (genre_id)    
    GROUP BY genre_id
    ORDER BY genre_name
    ''', conn)


def get_author(conn):
    return pd.read_sql('''
    SELECT author_id, author_name, sum(available_numbers) AS cnt
    FROM 
	    book
        JOIN book_author USING (book_id)
        JOIN author USING (author_id) 
    GROUP BY author_id
    ORDER BY author_name
    ''', conn)


def get_publisher(conn):
    return pd.read_sql('''
    SELECT publisher_id, publisher_name, sum(available_numbers) AS cnt
    FROM 
	    book
        JOIN publisher USING (publisher_id)
    GROUP BY publisher_id
    ORDER BY publisher_name
    ''', conn)


def get_book(conn, genres, authors, publishers):
    if (len(genres) != 1) and (len(authors) != 1) and (len(publishers) != 1):
        return pd.read_sql(f'''
            SELECT title AS Название, author_name AS Авторы, genre_name AS Жанр, publisher_name AS Издательство, year_publication AS Год_издания, available_numbers AS Количество
            FROM
                book
                JOIN book_author USING (book_id)            
                JOIN author USING (author_id)
                JOIN genre USING (genre_id)
                JOIN publisher USING (publisher_id)
            WHERE genre_id IN {genres} AND author_id IN {authors} AND publisher_id IN {publishers}
            ORDER BY title
        ''', conn)
    elif (len(genres) == 1) and (len(authors) != 1) and (len(publishers) != 1):
        return pd.read_sql(f'''
            SELECT title AS Название, author_name AS Авторы, genre_name AS Жанр, publisher_name AS Издательство, year_publication AS Год_издания, available_numbers AS Количество
            FROM
                book
                JOIN book_author USING (book_id)            
                JOIN author USING (author_id)
                JOIN genre USING (genre_id)
                JOIN publisher USING (publisher_id)
            WHERE genre_id = {genres[0]} AND author_id IN {authors} AND publisher_id IN {publishers}
            ORDER BY title
        ''', conn)
    elif (len(genres) != 1) and (len(authors) == 1) and (len(publishers) != 1):
        return pd.read_sql(f'''
            SELECT title AS Название, author_name AS Авторы, genre_name AS Жанр, publisher_name AS Издательство, year_publication AS Год_издания, available_numbers AS Количество
            FROM
                book
                JOIN book_author USING (book_id)            
                JOIN author USING (author_id)
                JOIN genre USING (genre_id)
                JOIN publisher USING (publisher_id)
            WHERE genre_id IN {genres} AND author_id = {authors[0]} AND publisher_id IN {publishers}
            ORDER BY title
        ''', conn)
    elif (len(genres) != 1) and (len(authors) != 1) and (len(publishers) == 1):
        return pd.read_sql(f'''
            SELECT title AS Название, author_name AS Авторы, genre_name AS Жанр, publisher_name AS Издательство, year_publication AS Год_издания, available_numbers AS Количество
            FROM
                book
                JOIN book_author USING (book_id)            
                JOIN author USING (author_id)
                JOIN genre USING (genre_id)
                JOIN publisher USING (publisher_id)
            WHERE genre_id IN {genres} AND author_id IN {authors} AND publisher_id = {publishers[0]}
            ORDER BY title
        ''', conn)
    elif (len(genres) == 1) and (len(authors) != 1) and (len(publishers) == 1):
        return pd.read_sql(f'''
            SELECT title AS Название, author_name AS Авторы, genre_name AS Жанр, publisher_name AS Издательство, year_publication AS Год_издания, available_numbers AS Количество
            FROM
                book
                JOIN book_author USING (book_id)            
                JOIN author USING (author_id)
                JOIN genre USING (genre_id)
                JOIN publisher USING (publisher_id)
            WHERE genre_id = {genres[0]} AND author_id IN {authors} AND publisher_id = {publishers[0]}
            ORDER BY title
        ''', conn)
    elif (len(genres) != 1) and (len(authors) == 1) and (len(publishers) == 1):
        return pd.read_sql(f'''
            SELECT title AS Название, author_name AS Авторы, genre_name AS Жанр, publisher_name AS Издательство, year_publication AS Год_издания, available_numbers AS Количество
            FROM
                book
                JOIN book_author USING (book_id)            
                JOIN author USING (author_id)
                JOIN genre USING (genre_id)
                JOIN publisher USING (publisher_id)
            WHERE genre_id IN {genres} AND author_id = {authors[0]} AND publisher_id = {publishers[0]}
            ORDER BY title
        ''', conn)
    elif (len(genres) == 1) and (len(authors) == 1) and (len(publishers) != 1):
        return pd.read_sql(f'''
            SELECT title AS Название, author_name AS Авторы, genre_name AS Жанр, publisher_name AS Издательство, year_publication AS Год_издания, available_numbers AS Количество
            FROM
                book
                JOIN book_author USING (book_id)            
                JOIN author USING (author_id)
                JOIN genre USING (genre_id)
                JOIN publisher USING (publisher_id)
            WHERE genre_id = {genres[0]} AND author_id = {authors[0]} AND publisher_id IN {publishers}
            ORDER BY title
        ''', conn)
    else:
        return pd.read_sql(f'''
            SELECT title AS Название, author_name AS Авторы, genre_name AS Жанр, publisher_name AS Издательство, year_publication AS Год_издания, available_numbers AS Количество
            FROM
                book
                JOIN book_author USING (book_id)            
                JOIN author USING (author_id)
                JOIN genre USING (genre_id)
                JOIN publisher USING (publisher_id)
            WHERE genre_id = {genres[0]} AND author_id = {authors[0]} AND publisher_id = {publishers[0]}
            ORDER BY title
        ''', conn)
