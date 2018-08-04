
import requests
import json
tel = {'text': "test"}
response = requests.post(
    'https://hooks.slack.com/services/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', data=json.dumps(tel),
    headers={'Content-Type': 'application/json'}
)
if response.status_code != 200:
    raise ValueError(
        'Request to slack returned an error %s, the response is:\n%s'
        % (response.status_code, response.text)
    )

print response
