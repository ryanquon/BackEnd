from flask import Blueprint
from flask import request
import mysql.connector

hello = Blueprint('hello', __name__)

@hello.route("/")
def fun():
    return 'This verifies a change can be made! hello world! I am ready to work on tagoose! Flask is cool! My key is safe. I want a picture2! You can have one too!'