# Working With JSON Files

import json
from pathlib import Path

# movies = [
#     {"id": 1, "title": "Terminator", "year": 1984},
#     {"id": 2, "title": "Kindergarten Cop", "year": 1990}
# ]

# data = json.dumps(movies)

# print(data)

# Path("09 Python Standard Library/07_working_with_json_files/movies.json").write_text(data)

data = Path(
    "09 Python Standard Library/07_working_with_json_files/movies.json").read_text()
movies = json.loads(data)
print(movies)
print(movies[0])
print(movies[1]["title"])
