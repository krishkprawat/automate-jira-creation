# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://xxxkp.atlassian.net/rest/api/3/issue"

API_TOKEN = "ATATT3xFfGF0U7AmcaDZeJHbq-nQRKtW6WaxjBiFPqwVFwKXDTn9Fh_XiCS0h6BRDSHavHJyutuLRVDDQPw-KatY529qVfiigKOr8iKsjf2e6PDRplTyrNjz0ts4o8McHfsmnU18o9ZhgI6NrTFg4EeAHR0-3ISOKvGopbrX4IR-6Rvh6sxFAF8=2BA35B0F"

auth = HTTPBasicAuth("krishkprawat02@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps( {
  "fields": {
    "description": {
      "content": [
        {
          "content": [
            {
              "text": "My first jira ticket",
              "type": "text"
            }
          ],
          "type": "paragraph"
        }
      ],
      "type": "doc",
      "version": 1
    },
    "project": {
      "key": "XXX"
    },
    "issuetype": {
      "id": "10006"
    },
    "summary": "First JIRA Ticket",
  },
  "update": {}
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))