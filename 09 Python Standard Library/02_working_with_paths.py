# Working With Paths

from pathlib import Path

# Various ways to create a path object
# Path(r"C:\Program Files\Microsoft")
# Path("usr/local/bin")
# Path()
# Path("ecommerce/__init__.py")
# Path() / "ecommerce" / "__init__.py"
# Path.home()

path = Path("09 Python Standard Library/ecommerce/__init__.py")
print(path.exists())
print(path.is_file())
print(path.is_dir())
print(path.name)
print(path.stem)
print(path.suffix)
print(path.parent)

path = path.with_name("file.txt")
print(path)
print(path.absolute())

path = path.with_suffix(".txt")
print(path)
