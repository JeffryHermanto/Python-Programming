# Working With Directories

from pathlib import Path

path = Path("09 Python Standard Library/ecommerce")

for p in path.iterdir():
    print(p)
# OR
print("")
paths = [p for p in path.iterdir() if p.is_dir()]
print(paths)

# PosixPath
# Posix is the standard used in Unix like operating system
# On Mac: PosixPath
# On Windos: WindowsPath

print("")

py_files = [p for p in path.glob("*.py")]
print(py_files)

print("")

# To search recursively, change the * pattern
py_files = [p for p in path.rglob("**/*.py")]
print(py_files)
