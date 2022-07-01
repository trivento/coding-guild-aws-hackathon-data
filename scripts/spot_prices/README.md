# Get spot prices from AWS

## Setup python env

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

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

## Run the script

This will show you a nice spot price graph.

```
python aws_spot_prices.py
```

## Common issues

* if you get the error `botocore.exceptions.NoCredentialsError: Unable to locate credentials` make sure you have
your aws api credentials set.