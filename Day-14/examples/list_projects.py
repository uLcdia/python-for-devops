# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://veeramallaabhishek.atlassian.net/rest/api/3/project"

API_TOKEN=""

auth = HTTPBasicAuth("", API_TOKEN)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

output = json.loads(response.text)

name = output[0]["name"]

print(name)
"""
Traceback (most recent call last):
  File "/home/nenya/source/python-for-devops/./Day-14/examples/list_projects.py", line 26, in <module>
    name = output[0]["name"]
           ~~~~~~^^^
KeyError: 0
"""
