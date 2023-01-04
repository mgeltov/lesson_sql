import sqlite3

with sqlite3.connect('books_db.sqlite') as connection:
    cursor = connection.cursor()

    # query = """
    # drop table books
    # """

    query = """
            create table books  (
                id integer primary key autoincrement 
            ,   name varchar(100)
            ,   author varchar(80)
            ,   description varchar(300)
            ,   genre varchar(20) constraint df_genre default 'undefined' -- после ключевого слова constraint необходимо задать название ограничения 
            ,   publication_date date
            ,   pages_count integer constraint ch_value check (pages_count > 0) 
            ,   price decimal
                                )
    """
    cursor.execute(query)

    index_query = """
            create index book_name_idx on books (name)
    """
    cursor.execute(index_query)
