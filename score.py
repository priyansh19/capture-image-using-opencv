# import libraries
import cv2
import os, json, sys

# define init function
def init(filepath=None):
    # define global variable
    global path

    # find scipt location
    if(filepath != None):
        path = filepath
    else:
        path="./"

# define run function to execute script
def run():
    # define status (result) dictionary
    status = dict()

    # create camera object
    camera = cv2.VideoCapture(0)

    # while camera is open
    while(camera.isOpened()):
        # read image from camera
        check, frame = camera.read()
        # release camera resources
        camera.release()
        # destroy all open window
        cv2.destroyAllWindows()

        # if image captured, break
        if status == True:
            break

    # encode data into PNG format
    data = cv2.imencode(".png", frame)[1].tostring()

    # save image
    cv2.imwrite("Authentication.png",frame)

    # return status
    if(check == True):
        status["status"] = True
        return(json.dumps(status))
    else:
        status["status"] = False
        return(json.dumps(status))

if __name__ == "__main__":
    init()
    status = run()
    print("Status {}".format(status))
