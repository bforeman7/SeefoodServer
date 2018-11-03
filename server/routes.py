from server import api, application
from flask import render_template, request, jsonify, send_file, url_for
from werkzeug.utils import secure_filename
from os.path import join, dirname, realpath
## import is used to create tables
from ImageModel import ImageModel

## Entry point to API
@application.route("/", methods=["GET"])
def home():
    return render_template("index.html")

## Recieves images and their dates from mobile application
@application.route("/image", methods=["POST"])
def post_images():
    if request.method == "POST":
       #path to static 
        UPLOADS_PATH = join(dirname(realpath(__file__)), 'static/')

        ## check to see if request body is filled
        if "image" not in request.files:
            return jsonify(msg="'image' cannot be left blank."), 400
        elif "time_taken" not in request.form:
            return jsonify(msg="'time_taken' cannot be left blank."), 400
        
        #stuff we need
        image = request.files.get("image")
        time =request.form.get("time_taken")
 
        ## DO IMAGE CONVERSION HERE

        ## saves image to statics
        image_name = secure_filename(image.filename)
        image.save(UPLOADS_PATH + image_name)

        return jsonify(msg="Will place return stuff later"), 201

@application.route("/images", methods=["GET"])
def get_images():
    pass
