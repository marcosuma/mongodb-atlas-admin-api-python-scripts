import requests
import json
import os

public_key = os.environ.get('MONGODB_ATLAS_PUBLIC_KEY')
private_key = os.environ.get('MONGODB_ATLAS_PRIVATE_KEY')
base_url = os.environ.get('MONGODB_ATLAS_BASE_URL') # https://cloud.mongodb.com/
username = os.environ.get("MONGODB_ATLAS_USERNAME")

# Set the API URL
api_url = base_url + "api/atlas/v2/users/byName/" + username

# Set the authentication headers
auth = requests.auth.HTTPDigestAuth(public_key, private_key)

# Make the API call
response = requests.get(api_url, auth=auth, headers={"Accept": "application/vnd.atlas.2023-02-01+json"})


# Handle the response
if response.status_code == 200:
    # Success!
    print(response.json())
else:
    # Error!
    print(response.status_code)
    print(response.content)
    print(response)