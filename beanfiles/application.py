from flask import Flask
from server import process
from welcome import hello
from saveimage import imagesaver

application = app = Flask(__name__)
app.register_blueprint(process, url_prefix='/process')
app.register_blueprint(hello, url_prefix='')
app.register_blueprint(imagesaver, url_prefix='/saveimage')

if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True #uncomment to test
    app.run()