# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://xxxkp.atlassian.net//rest/api/3/project"

auth = HTTPBasicAuth("krishkprawat02.com", "ATATT3xFfGF00R_xNzK9jt8tBWqEdsAxkUOfOSVEtM2TfaloNmjOIFsZIAV5vi5dzUlKnnKDNJVWyajK5k96TwHtajg-iFpGqo2bt_7horvn_yreujdsfQRjdmynVx94Kv1GNaj6I-7aC9VQr4d-p3DbF3lhkzqZ1oGilyOvyu9tKhcDrIvIKy4=3EAF6574")

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))