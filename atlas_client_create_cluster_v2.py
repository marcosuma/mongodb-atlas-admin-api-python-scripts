import requests
import json
import os


public_key = os.environ.get('MONGODB_ATLAS_PUBLIC_KEY')
private_key = os.environ.get('MONGODB_ATLAS_PRIVATE_KEY')
base_url = os.environ.get('MONGODB_ATLAS_BASE_URL') # https://cloud.mongodb.com/
project_id = os.environ.get('MONGODB_ATLAS_PROJECT_ID')
cluster_name = os.environ.get('MONGODB_ATLAS_CLUSTER_NAME')

# Set the API URL
api_url = base_url + "api/atlas/v2/groups/" + project_id + "/clusters"

# Set the authentication headers
auth = requests.auth.HTTPDigestAuth(public_key, private_key)

# Request body
request_body = {
  "name": cluster_name,
  "clusterType": "REPLICASET",
  "numShards": 1,
  "links": [],
  "replicationSpecs": [
    {
      "numShards": 1,
      "regionConfigs": [
        {
          "electableSpecs": {
            "instanceSize": "M30",
            "nodeCount": 3
          },
          "readOnlySpecs": {
            "instanceSize": "M30",
            "nodeCount": 0
          },
          "priority": 7,
          "providerName": "AWS",
          "regionName": "EU_WEST_1"
        },
        {
          "electableSpecs": {
            "instanceSize": "M30",
            "nodeCount": 2
          },
          "readOnlySpecs": {
            "instanceSize": "M30",
            "nodeCount": 0
          },          
          "priority": 6,
          "providerName": "AWS",
          "regionName": "US_EAST_1"
        }
      ],
      "zoneName": "zone_name"
    }
  ]
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