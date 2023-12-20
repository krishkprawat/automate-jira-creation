# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json
from flask import Flask, request

app = Flask(__name__)

# Define a route that handles POST requests
@app.route('/createJira', methods=['POST'])
def create_jira():
    url = "https://xxxkp.atlassian.net/rest/api/3/issue"
    API_TOKEN = ""
    auth = HTTPBasicAuth(".", API_TOKEN)

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    webhook = request.json

    # Check if the comment body starts with /jira
    if webhook.get('comment') and webhook['comment'].get('body', '').startswith("/jira"):
        payload = json.dumps({
            "fields": {
                "description": {
                    "content": [
                        {
                            "content": [
                                {
                                    "text": "Order entry fails when selecting supplier.",
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
                    "key": "KKPP"
                },
                "issuetype": {
                    "id": "10007"
                },
                "summary": "new ---Main order flow broken in kp environment",
            },
            "update": {}
        })

        # Make a request to create a Jira issue
        response = requests.post(
            url,
            data=payload,
            headers=headers,
            auth=auth
        )

        if response.ok:
            return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))
        else:
            return f"Failed to create Jira issue. Status code: {response.status_code}"

    return "Jira issue will be created if the comment starts with /jira"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
