#Final_project part1 : E-mail
from gpiozero import MotionSensor,LED
import time
import yagmail
from picamzero import Camera
#from camera import Camera
import os
from signal import pause

#Initialization
pir = MotionSensor(4)
led = LED(26)
print("gpio setup OK")

motion_start = time.time()
last_time_photo_taken = 0
MOVEMENT_DETECT_THRESHOLD = 2
GAP_BETWEEN_PHOTO = 30
folder_name = "/home/vector/camera/pic_series"
LOG_FILE_NAME = folder_name + "/photo_log.txt"

camera1 = Camera()
camera1.still_size = (640, 480)
camera1.flip_camera(hflip=True ,vflip=False )
print("camera configured successfully")

#setup mail
password = ""

with open("/home/vector/.local/share/temp" , "r")as f:
    password = f.read().rstrip()
print("email setup")

if os.path.exists(LOG_FILE_NAME):
   os.remove(LOG_FILE_NAME)
   print("previous log file removed")

if not os.path.exists("/home/vector/camera/pic_series"):
    os.mkdir("/home/vector/camera/pic_series")
    
def update_log_file(pic, log_file_name):
    with open (log_file_name, "a") as f:
        f.write(pic)
        f.write("\n")
def send_mail(pic):
    yag_server = yagmail.SMTP("amthestranger1@gmail.com", password)
    print("Initialize .ready to send email")
    yag_server.send(to="sawanttejas2004@gmail.com",
                    subject="Alert",
                    contents="Certain movement spotted",
                    attachments=pic)
    
    
    

def take_picture(camera1, folder_name):
    file_name = folder_name + "/img_" + str(time.time())+ ".jpg"
    camera1.take_photo(file_name)
    return file_name

def motion_detected():
    #print("starting timer")
    global motion_start
    motion_start = time.time()
    led.on()

def motion_finished():
    global last_time_photo_taken
    led.off()
    motion_duration = time.time() - motion_start
    #print(motion_duration)
    if motion_duration >= MOVEMENT_DETECT_THRESHOLD:
        if time.time() - last_time_photo_taken >= GAP_BETWEEN_PHOTO:
            last_time_photo_taken = time.time()
            print("Taking photo")
            pic = take_picture(camera1 , folder_name)
            update_log_file(pic,LOG_FILE_NAME)
            send_mail(pic)
            
        
pir.when_motion = motion_detected
pir.when_no_motion = motion_finished
print("everything is been setup")
pause()
