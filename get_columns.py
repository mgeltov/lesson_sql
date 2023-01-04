import sqlite3

with sqlite3.connect("netflix.db") as connection:
    cursor = connection.cursor()
    query = """
            select *
            from netflix
            limit 1
    """
    cursor.execute(query)

    for column in cursor.description:
        print(column[0])