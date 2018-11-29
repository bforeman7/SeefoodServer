from server import api, application
from flask import render_template, request, jsonify, send_file, url_for
from werkzeug.utils import secure_filename
from os.path import join, dirname, realpath
## import is used to create tables
from ImageModel import ImageModel
from seefoodWrapper import SeefoodWrapper
from server import logger

## Used for image processing and conversion
from PIL import Image
import server
import os


@application.before_first_request
def startup():
    os.chdir("/home/ubuntu/SeefoodServer/server/seefood")
    # this is here for debugging purposes to tell us whether we got to the seefood directory or not
    print(os.listdir("/home/ubuntu/SeefoodServer/server/seefood"))
    global seefoodWrapper
    seefoodWrapper = SeefoodWrapper()
   
#@application.before_request
#def before_failure():
     # send image to seefood
#    seefoodWrapper.pollForReady()
        

## Entry point to API
@application.route("/", methods=["GET"])
def home():
    return render_template("index.html")

## Recieves images and their dates from mobile application
@application.route("/image", methods=["POST"])
def post_images():
    if request.method == "POST":
       #path to static 
        LOCAL_STATIC_PATH = 'static/'
        UPLOADS_PATH = join(dirname(realpath(__file__)), LOCAL_STATIC_PATH)
        DATABASE_SIZE = 10
	## check to see if request body is filled
        if "image" not in request.files:
            return jsonify(msg="'image' cannot be left blank."), 400
        elif "time_taken" not in request.form:
            return jsonify(msg="'time_taken' cannot be left blank."), 400
        elif "image_orientation" not in request.form:
            return jsonify(msg="'image_orientation' cannot be left blank."), 400

        # get the image
        image = request.files.get("image")
        time =request.form.get("time_taken")
        orientation = request.form.get("image_orientation")        


        try:
	    seefoodWrapper.pollForReady()

	   # save the image to the server
            image_name = secure_filename(image.filename)
            path = UPLOADS_PATH + image_name
            image.save(path)
            
            # Seefood AI can take .bmp, .jpg, .png, etc. no need to convert. We can filter out images on app before
            # they are sent to the server
            confidences = seefoodWrapper.sendImage(path)
	    logger.write_info("routes.py:Got confidence ratings " + confidences[0] + " " +confidences[1])
            # convert the image for server gallery
            new_img = Image.open(path)
            os.remove(path)

            truncName = image_name.split(".")
            newName = truncName[0] + '.png'
            newNamePath = UPLOADS_PATH + newName
            new_img.save(newNamePath, 'png')

	    logger.write_info("routes.py:Sucessfully re-saved image")

            img_return_path = LOCAL_STATIC_PATH + newName
            
            # ENFORCE DATABASE SIZE
            all_images = ImageModel.query.all()
            if len(all_images) == DATABASE_SIZE:
                first_image = all_images[0]
                first_image.delete_from_database()

            imageModel = ImageModel(truncName[0], time, confidences[0], confidences[1], img_return_path, orientation )
	    logger.write_info("routes.py:Created imageModel")
            imageModel.save_to_database()
	    logger.write_info("routes.py:Saved to database")

            return jsonify(image=imageModel.json()), 201

        except Exception as error:
	    logger.write_error(error)
            return jsonify(msg="An error occured during image POST: {}".format(error)), 500

@application.route("/images", methods=["GET"])
def get_images():

    ## all the images in the database stored in a list
    all_images = ImageModel.query.all()

    if "start" not in request.args:
        return jsonify(msg="'start' cannot be left blank."), 400
    elif "end" not in request.args:
        return jsonify(msg="'end' cannot be left blank."), 400

    ## images returned are subset of all_images, i.e [start_index, end_index] C all_images
    start = int(request.args.get("start"))
    end = int(request.args.get("end"))

    try:
        #do checks to see if start_index and end_index are within all_images
        requested_images = None
        num_of_imgs = len(all_images)

        if (start > num_of_imgs and end > num_of_imgs) or (start <= 0 and end <= 0):
            requested_images = []
        else:
            if start <= 0: start = 1
            if start > num_of_imgs: start = num_of_imgs
            if end <= 0: end = 0
            if end > num_of_imgs : end = num_of_imgs
            
            requested_images= all_images[start-1:end]

        return jsonify({"images": [image.json() for image in requested_images]}), 200

    except Exception as error:
        return jsonify(msg="An error occured during image GET: {}".format(error)), 500

@application.route("/image", methods=["DELETE"])
def delete_image():
    if request.method == "DELETE":
        if "id" not in request.args:
            return jsonify(msg="'id' cannot be left blank."), 400
        
        try:
            img_id = request.args.get("id")
            image = ImageModel.find_by_id(img_id)
            if image:
                image.delete_from_database()
                return jsonify(msg="Image with id '{}' has been successfully deleted.".format(img_id)), 200
            return jsonify(msg="id '{}' does not exist.".format(img_id)), 400
        except Exception as error:
            return jsonify(msg="An error occured during image DELETE: {}".format(error)), 500