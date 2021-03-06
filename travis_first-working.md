# language: python
# python:
#   - "3.6"      # current default Python on Travis CI
#   - "3.7"
#   - "nightly"  # nightly build
# # command to install dependencies
# install:
#   - pip install -r requirements.txt
# # command to run tests
# script:
#   - pytest


# sudo: required
# services:
#   - docker

# before_install:
#   - docker build -t nathphoenix/flask-standard -f dockerfile .

# script:
#   - docker run nathphoenix/flask-standard pytest

language: python

# python:
# - "3.7"

services:
- docker

install:
- pip install -r requirements.txt

before_install:
- docker-compose -f docker-compose.yml up --build -d
# - docker-compose -f SQLInjection/docker-compose.yml up --build -d

script:
- pytest

deploy:
  provider: elasticbeanstalk
  region: 'us-east-1'
  app: 'flask-standard'
  env: 'Flaskstandard-env'
  bucket_name: 'elasticbeanstalk-us-east-1-960726601836'
  # s3_host_name: 's3-eu-west-1.amazonaws.com'
  bucket_path: 'flask-standard'
  on:
    branch: master
  #adding the variable name that was use to store the generated amazon credentials on travis website that is link to this repo
  access_key_id: $AWS_ACCESS_KEY
  secret_access_key: $AWS_SECRET_KEY

