# Working With Zip Files

from pathlib import Path
from zipfile import ZipFile

# zipFile = ZipFile(
#     "09 Python Standard Library/05_working_with_zip_files/files.zip", "w")

# iterablePath = Path("09 Python Standard Library/ecommerce")

# with zipFile as zip:
#     for path in iterablePath.rglob("*.*"):
#         zip.write(path)

# with ZipFile(
#         "09 Python Standard Library/05_working_with_zip_files/files.zip") as zip:
#     print(zip.namelist())
#     info = zip.getinfo(
#         "09 Python Standard Library/ecommerce/__init__.py")
#     print(info.file_size)
#     print(info.compress_size)
#     zip.extractall(
#         "09 Python Standard Library/05_working_with_zip_files/extract")
