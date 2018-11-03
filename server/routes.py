from server import api, application
from flask import render_template, request, jsonify
## import is used to create tables
from ImageModel import ImageModel

@application.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@application.route("/images", methods=["POST"])
def post_images():
    if request.method == "POST":
        
        ## check to see if request body is filled
        if "images" not in request.files:
            return jsonify(msg="'images' cannot be left blank."), 400
        elif "time_taken" not in request.form:
            return jsonify(msg="'time_taken' cannot be left blank."), 400
        
        #stuff we need
        images = request.files.getlist("images")
        time =request.form.get("time_taken")

        ##displaying info for now
        for image in images:
            print str(image.filename)
        print str(time)

        return jsonify(msg="placeholder for response."), 201

    
