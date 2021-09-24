# Pipenv

# $ pip3 install pipenv
# $ pipenv install requests
# $ pipenv --venv
# $ pipenv shell

import requests

response = requests.get("http://google.com")
print(response)
