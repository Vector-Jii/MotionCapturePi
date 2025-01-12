#Final_project_part2 (Web server)
from flask import Flask
from gpiozero import LED,MotionSensor
import os

LOG_FILE_NAME = "/home/vector/camera/pic_series/photo_log.txt"
camera_folder = "/home/vector/camera/pic_series"

previous_line_counter =0

app = Flask(__name__,static_url_path = camera_folder , static_folder = camera_folder)   #init flask app
@app.route("/")
def index():
    return "Hello world web"

@app.route("/check-photo")
def check_photo():
    if os.path.exists(LOG_FILE_NAME):
        last_photo_name = ""
        #count lines
        global previous_line_counter
        current_counter = 0
        with open(LOG_FILE_NAME, "r")as f:
            for line in f:
                current_counter +=1
                last_photo_name = line.rstrip()
        diff = current_counter - previous_line_counter 
        previous_line_counter = current_counter
        message =  str(diff) + "  number of photos since last checked  <br/>"
        message += "Last photo =" + last_photo_name + "<br/>"
        message += "<img src=\"" + last_photo_name + "\">"    # <img src="path">
        return message
    else:
        return"No image"

app.run(host="0.0.0.0")