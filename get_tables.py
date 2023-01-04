import sqlite3

with sqlite3.connect("netflix.db") as connection:
    cursor = connection.cursor()
    query = """
            select *
            from sqlite_master
            where type = 'table'
    """
    cursor.execute(query)

    tables = cursor.fetchall()
    print(tables)
