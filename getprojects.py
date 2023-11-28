# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://xxxkp.atlassian.net//rest/api/3/project"

auth = HTTPBasicAuth("krishkprawat02@gmail.com", "ATATT3xFfGF0wqABlExJke8XTHePeoVqKbs2IzgCMXLiia-lkEhUjE-S5KMeiP1ddruQdQAXxGiJAQbn6DyzWNAHqjBUNp38co8AGTq27kFYsySjvB5Wd7ZW1ESgP-FgAilkDzKFnNxps0h_52U63B52cq7iWOhQV19-DDYkFVNiRxcMz_MzRTQ=EA46F88E")
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