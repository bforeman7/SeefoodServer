from server import api, application
from flask import render_template, request, jsonify
## import is used to create tables
from ImageModel import ImageModel

@application.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@application.route("/images", methods=["POST"])
def post_images():
    if request.method == "POST" and "images" in request.files:
        images = request.files.getlist("images")

        for image in images:
            print image.filename

        return jsonify(msg="placeholder for response"), 201

    return jsonify(msg="'images' cannot be left blank"), 400
