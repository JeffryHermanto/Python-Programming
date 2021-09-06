# Working With a SQLite Database

import sqlite3
import json
from pathlib import Path

basePath = "09 Python Standard Library/08_working_with_a_sqlite_database"

# movies = json.loads(Path(f"{basePath}/movies.json").read_text())

# with sqlite3.connect(f"{basePath}/db.sqlite3") as conn:
#     command = "INSERT INTO Movies VALUES(?, ?, ?)"
#     for movie in movies:
#         conn.execute(command, tuple(movie.values()))
#     conn.commit()

with sqlite3.connect(f"{basePath}/db.sqlite3") as conn:
    command = "SELECT * FROM Movies"
    cursor = conn.execute(command)
    # for row in cursor:
    #     print(row)
    movies = cursor.fetchall()
    print(movies)
