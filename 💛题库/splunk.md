## Splunk 


### AUTHENTICATION
- crediential
- token


### API

jobs
- get:

- post: search/jobs/{searchid}








https://dev.splunk.com/enterprise/docs/devtools/python/sdk-python/howtousesplunkpython/howtorunsearchespython/



import os
import requests

# Set up the session with our adapter
SEARCH_ENDPOINT = "https://"+os.environ['SPLUNK_HOST']+":8089/services/search/jobs"
headers = {
    'Authorization': 'Bearer '+os.environ['SPLUNK_TOKEN'],
    "Accept": "application/json"
}
params = {
    "search": "inputcsv search-output.csv",
    "output_mode": "json"
}

response = requests.post(SEARCH_ENDPOINT, data=params, headers=headers, verify=True)
print(response.text)



https://splunkui.splunk.com/Packages/search-job/API