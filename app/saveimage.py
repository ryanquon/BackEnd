#based on https://medium.com/bilesanmiahmad/how-to-upload-a-file-to-amazon-s3-in-python-68757a1867c6
#https://stackoverflow.com/questions/8637153/how-to-return-images-in-flask-response
#https://stackoverflow.com/questions/18908426/increasing-client-max-body-size-in-nginx-conf-on-aws-elastic-beanstalk
#https://medium.com/@marilu597/getting-to-know-and-love-aws-elastic-beanstalk-configuration-files-ebextensions-9a4502a26e3c
#https://stackoverflow.com/questions/40336918/how-to-write-a-file-or-data-to-an-s3-object-using-boto3
#https://towardsdatascience.com/object-detection-with-less-than-10-lines-of-code-using-python-2d28eebc5b11
import boto3
import os
from botocore.exceptions import NoCredentialsError
from flask import Blueprint
from flask import request
import mysql.connector
import json
from keys import keyaccess #only use if you're gonna localhost
from keys import keysecret #only use on localhost
from flask import send_file
import tempfile
import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox

imagesaver = Blueprint('imagesaver', __name__)

def determine(eachObject, centerx, centery): # (x1, y1, x2, y2). x1 and y1 refers to the lowerleft corner 
    #and x2 and y2 refers to the upperright corner.
    if (eachObject[0] <= centerx <= eachObject[2]):
        if (eachObject[1] <= centery <= eachObject[3]):
            return True
    return False


ACCESS_KEY = keyaccess
SECRET_KEY = keysecret

@imagesaver.route("/", methods=['POST','GET'])
def upload_to_aws():
    #we know for sure that the apple.jpg is in fact existent
    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY)
    bucketname = 'elasticbeanstalk-us-east-1-864793221722'
    keyname = 'input.jpg'
    tmp = tempfile.NamedTemporaryFile()
    with open(tmp.name, 'wb') as f:
        s3.download_fileobj(bucketname, keyname, f)  

    im = cv2.imread(tmp.name)
    h, w, c = im.shape
    centerx = w/2
    centery = h/2
    bbox, label, conf = cv.detect_common_objects(im)

    finallist = [x for x in bbox if determine(x,centerx,centery)]

    if (len(finallist) > 0):
        left = finallist[0][0]
        top = finallist[0][1]
        right = finallist[0][2]
        bottom = finallist[0][3]
        im1 = im[top:bottom, left:right]
        cv2.imwrite("output.jpg",im1)
        s3.upload_file("output.jpg", bucketname, 'trial2.jpg')
    os.remove("output.jpg")
    return 'went fine'



