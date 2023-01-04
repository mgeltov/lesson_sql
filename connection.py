import sqlite3
with sqlite3.connect("netflix.db") as connection:
    cursor = connection.cursor()
    query = """
            select type, count(show_id) as cnt, sum(duration) as total_duration, sum(cast(duration as float)) / count(show_id) as avg_duration
            from netflix
            group by type
    """

    cursor.execute(query)

    for row in cursor.fetchall():
        print(row)