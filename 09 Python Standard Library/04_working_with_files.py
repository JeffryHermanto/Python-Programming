# Working With Files

from pathlib import Path
from time import ctime
import shutil

path = Path("09 Python Standard Library/ecommerce/__init__.py")

print(path.exists())

# path.rename("init.txt")
# path.unlink()

# print(path.stat())
print(ctime(path.stat().st_ctime))

print(path.read_bytes())
print(path.read_text())


source = Path("09 Python Standard Library/ecommerce/__init__.py")
target = Path() / "__init__.py"

# shutil.copy(source, target)
