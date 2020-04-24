from flask import Blueprint
from flask import request
import mysql.connector
import json

process = Blueprint('process', __name__)

@process.route("/", methods=['POST'])
def processfunc():
    data = request.get_json()
    connection = mysql.connector.connect(user='root',
                              password='fOrtranmyeggo124',
                              host='tagoosedev.cm63orfguism.us-east-1.rds.amazonaws.com',
                              database='USER_DATA')
                
    mycursor = connection.cursor()
    mycursor.execute("SELECT * FROM USER_DATA.table1")
    mycursor.execute("SELECT latitude, longitude FROM `USER_DATA`.`table1` WHERE sqrt(pow(latitude-data[latitude],2)+ pow(longitude-data[longitude],2)) <= 10")
    #not sure if data[latitude] is correct formatting
    myresult = mycursor.fetchall()  
    myresult = json.dumps(myresult)
    return myresult
    #return data