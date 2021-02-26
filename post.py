import json
import requests

def post_to_slack(message):
    webhook_url = 'https://hooks.slack.com/services/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'
    slack_data = json.dumps({'text': message})
    response = requests.post(
        webhook_url, data=slack_data,
        headers={'Content-Type': 'application/json'}
    )
    if response.status_code != 200:
        raise ValueError(
            'Request to slack returned an error %s, the response is:\n%s'
            % (response.status_code, response.text)
        )
