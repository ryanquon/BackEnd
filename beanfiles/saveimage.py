#based on https://medium.com/bilesanmiahmad/how-to-upload-a-file-to-amazon-s3-in-python-68757a1867c6
#https://stackoverflow.com/questions/8637153/how-to-return-images-in-flask-response
#https://stackoverflow.com/questions/18908426/increasing-client-max-body-size-in-nginx-conf-on-aws-elastic-beanstalk
#https://medium.com/@marilu597/getting-to-know-and-love-aws-elastic-beanstalk-configuration-files-ebextensions-9a4502a26e3c
#https://stackoverflow.com/questions/40336918/how-to-write-a-file-or-data-to-an-s3-object-using-boto3
import boto3
import os
from botocore.exceptions import NoCredentialsError
import matplotlib.image as mpimg
from flask import Blueprint
from flask import request
import mysql.connector
import json
from flask import send_file
import tempfile
import io

imagesaver = Blueprint('imagesaver', __name__)


ACCESS_KEY = os.environ.get('AWS_ACCESS_KEY')
SECRET_KEY = os.environ.get('AWS_SECRET_KEY')

@imagesaver.route("/", methods=['POST'])
def upload_to_aws():
    #we know for sure that the apple.jpg is in fact existent
    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY)
    bucketname = 'elasticbeanstalk-us-east-1-864793221722'
    keyname = 'apple.jpg'
    tmp = tempfile.NamedTemporaryFile()
    with open(tmp.name, 'wb') as f:
        s3.download_fileobj(bucketname, keyname, f)   
    s3.upload_fileobj(tmp, bucketname, 'fake2.jpg')
    return 'went fine'


