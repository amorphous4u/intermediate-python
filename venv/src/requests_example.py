__author__ = 'Amit Verma'

# Install using python3 -m pip install requests

import requests

r = requests.get('https://api.github.com/events')

print(r)
print(r.status_code)
print(r.text)
print(r.content)
print(r.json())