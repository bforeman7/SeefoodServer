from server import api, application
from flask import render_template, request, jsonify, send_file, url_for
from werkzeug.utils import secure_filename
from os.path import join, dirname, realpath
## import is used to create tables
from ImageModel import ImageModel

## Used for image processing and conversion
from PIL import Image
import server
import os

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
        
        # get the image
        image = request.files.get("image")
        time =request.form.get("time_taken")

        # save the image to the server
        image_name = secure_filename(image.filename)
        path = UPLOADS_PATH + image_name
        image.save(path)

        # send image to seefood
        if server.seefoodWrapper.isReady() == False:
            while server.seefoodWrapper.isReady() == False:
                server.seefoodWrapper.pollForReady()
                break
        
        # Seefood AI can take .bmp, .jpg, .png, etc. no need to convert. We can filter out images on app before
        # they are sent to the server
        confidences = server.seefoodWrapper.sendImage(path)

        # convert the image for server gallery
        tempImg = Image.open(path)
        new_img = tempImg.resize((320, 320))
        os.remove(path)

        truncName = image_name.split(".")
        newName = truncName[0] + '.png'
        newNamePath = UPLOADS_PATH + newName
        new_img.save(newNamePath, 'png')

        imageModel = ImageModel(truncName[0], time, confidences[0], confidences[1], newNamePath)

        return jsonify(msg="Your food confidence rating is: " + confidences[0] + " " + confidences[1]), 201

@application.route("/images", methods=["GET"])
def get_images():
    pass
