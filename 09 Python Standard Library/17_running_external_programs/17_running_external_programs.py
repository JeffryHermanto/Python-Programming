# Running External Programs

import subprocess

basePath = "09 Python Standard Library/17_running_external_programs"


try:
    # completed = subprocess.run(["ls", "-l"])

    # completed = subprocess.run(["python3", "other.py"],
    #                            capture_output=True,
    #                            text=True,
    #                            check=True)

    # completed = subprocess.run(["python3", f"{basePath}/other.py"],
    #                            capture_output=True,
    #                            text=True,
    #                            check=True)

    completed = subprocess.run(["ls", "-l"],
                               capture_output=True,
                               text=True,
                               check=True)

    print("args", completed.args)
    print("returncode", completed.returncode)
    print("stderr", completed.stderr)
    print("stdout", completed.stdout)
except subprocess.CalledProcessError as ex:
    print(ex)
