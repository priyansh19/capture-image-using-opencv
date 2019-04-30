# Capture Image using OpenCV

Computer vision is concerned with the automatic extraction, analysis and understanding of useful information from a single image or a sequence of images.

OpenCV-Python is a library of Python bindings designed to solve computer vision problems. To install OpenCV create conda environment and install OpenCV using pip.

`conda env create --clone base --name opencv`

`pip install opencv-python`


### Import Library
```
import cv2
```

### Create Camera Object
This allow python script to access webcam and take video or image.
```
camera = cv2.VideoCapture(0)

```

```
while(camera.isOpened()):
    # read image from camera
    check, frame = camera.read()
    # release camera resources
    camera.release()
    # destroy all open window
    cv2.destroyAllWindows()

    # if image captured, break
    if check == True:
        break
```


### Save/Encode Image

```
# save image
cv2.imwrite("Authentication.png",frame)

```
```
# encode data into PNG format
data = cv2.imencode(".png", frame)[1].tostring()
```
