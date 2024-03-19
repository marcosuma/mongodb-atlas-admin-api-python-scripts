## Prerequisites
* Have Python installed on your local machine
* Be able to use a terminal on your local machine
* Have a [MongoDB Atlas](https://cloud.mongodb.com/) Account.
* Set-up your programmatic API keys
  * You can find more information [here](https://www.mongodb.com/docs/atlas/configure-api-access/).

## How to use it
Using these scripts is fairly simple.
1. Define the local environment variables needed for the script to run. For example:
```
export MONGODB_ATLAS_BASE_URL=https://cloud.mongodb.com/
export MONGODB_ATLAS_PROJECT_ID=project_id
export MONGODB_ATLAS_PUBLIC_KEY=public_key
export MONGODB_ATLAS_PRIVATE_KEY=xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
```
2. Run the script using python. For example:
```
python atlas_client_create_cluster_v2.py
```
