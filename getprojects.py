# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://xxxkp.atlassian.net//rest/api/3/project"

auth = HTTPBasicAuth("krishkprawat02@gmail.com", "add tokenn here")
headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

output= json.loads(response.text)
name= output[1]["name"]
print(name)
