# Get spot prices from AWS

### Setup aws credentials

* Login to the aws console
* Go to IAM
* Create an user `spot-prices-api-user` with Access Key.
* Setup your local credentials :
```
aws configure
```

Fill in the following values:
* AWS Access Key ID [None]: COPY_FROM_AWS_CONSOLE
* AWS Secret Access Key [None]: COPY_FROM_AWS_CONSOLE
* Default region name [None]: eu-central-1
* Default output format [None]: json


### Create a bucket

* Select region: eu-central-1
* Go to s3
* Create bucket with unique name, e.g.: aws-hackathon-team-data-spot-prices

## Setup python env - using pipenv

Prerequisites: install pipenv

```bash
pipenv install
pipenv shell
```

## Setup python env - alternative - using pip

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install boto3
```

## Run the script

This will upload your file into the bucket.

```
python upload_to_s3.py aws-hackathon-team-data-spot-prices example.json
```

