#based on https://medium.com/bilesanmiahmad/how-to-upload-a-file-to-amazon-s3-in-python-68757a1867c6
#https://stackoverflow.com/questions/8637153/how-to-return-images-in-flask-response
#https://stackoverflow.com/questions/18908426/increasing-client-max-body-size-in-nginx-conf-on-aws-elastic-beanstalk
#https://medium.com/@marilu597/getting-to-know-and-love-aws-elastic-beanstalk-configuration-files-ebextensions-9a4502a26e3c
#https://stackoverflow.com/questions/40336918/how-to-write-a-file-or-data-to-an-s3-object-using-boto3
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
#from imageai.Detection import ObjectDetection   # unfortunately not compatible with python 3.7
import cv2

imagesaver = Blueprint('imagesaver', __name__)

def determine(eachObject, centerx, centery): # (x1, y1, x2, y2). x1 and y1 refers to the lowerleft corner 
    #and x2 and y2 refers to the upperright corner.
    if (eachObject["box_points"][0] <= centerx <= eachObject["box_points"][2]):
        if (eachObject["box_points"][1] <= centery <= eachObject["box_points"][3]):
            return True
    return False


#ACCESS_KEY = os.environ.get('AWS_ACCESS_KEY') #do this when you actually deploy
#SECRET_KEY = os.environ.get('AWS_SECRET_KEY')
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

    #im = cv2.imread(tmp.name)
    #h, w, c = im.shape
    #centerx = w/2
    #centery = h/2

    #execution_path = os.getcwd()

    #detector = ObjectDetection()    # DEFINE object detection variable
    #detector.setModelTypeAsRetinaNet()
    #detector.setModelPath( os.path.join(execution_path , "model.h5"))
    ## !!! 'resnet50_coco_best_v2.0.1.h5' is the RetinaNet model file used for object detection
    #detector.loadModel()
    #detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , tmp.name), output_image_path=os.path.join(execution_path , "output.jpg"))
    ## !!! IMAGE FILE MUST BE CALLED 'image.jpg'

    #finallist = [x for x in detections if determine(x,centerx,centery)]
    #if (len(finallist) > 0):
        #left = finallist[0]["box_points"][0]
        #top = finallist[0]["box_points"][1]
        #right = finallist[0]["box_points"][2]
        #bottom = finallist[0]["box_points"][3]
        #im1 = im[top:bottom, left:right]
        #cv2.imwrite("output.jpg",im1)
        #s3.upload_fileobj("output.jpg", bucketname, 'fake2.jpg')
        #s3.upload_file("output.jpg", bucketname, 'output.jpg')
    #os.remove("output.jpg")
    return 'went fine'



