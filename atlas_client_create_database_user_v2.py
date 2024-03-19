import requests
import json
import os

public_key = os.environ.get('MONGODB_ATLAS_PUBLIC_KEY')
private_key = os.environ.get('MONGODB_ATLAS_PRIVATE_KEY')
base_url = os.environ.get('MONGODB_ATLAS_BASE_URL') # https://cloud.mongodb.com/
project_id = os.environ.get('MONGODB_ATLAS_PROJECT_ID')
username = os.environ.get('MONGODB_ATLAS_USERNAME')

# Set the authentication headers
auth = requests.auth.HTTPDigestAuth(public_key, private_key)

# Set the API URL
api_url = base_url + "api/atlas/v2/groups/" + project_id + "/databaseUsers"

request_body = {
  "username":username,
  "x509Type":"MANAGED",
  "databaseName":"$external",
 
  "roles": [
    {
        "roleName":"readWrite",
        "databaseName":"spoke",
    },
  ],
}

# Make the API call
response = requests.post(api_url, json=request_body, auth=auth, headers={"Accept": "application/vnd.atlas.2023-11-15+json"})


# Handle the response
if response.status_code == 201:
    # Success!
    print(response.json())
else:
    # Error!
    print(response.status_code)
    print(response.content)
    print(response)