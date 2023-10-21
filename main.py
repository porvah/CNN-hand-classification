# Required Libraries
import tensorflow as tf
from tensorflow.keras import models 
from ultralytics import YOLO
import cv2
import supervision as sv
import numpy as np
import serial 

# Set the COM port used for the arduino demo
comport = "COM3"

# This function preprocess cropped images from the YOLO model, passes  it to the CNN model and returns the predicted output for the demo
def pass2CNN(img, model):	
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.resize(img, (300, 300))
    img = cv2.medianBlur(img, 11)
    img = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
    image_arr = tf.keras.utils.img_to_array(img)
    image_arr = np.array([image_arr])/255.0

    return np.argmax(model.predict(image_arr))
# Beginin a Serial connection with the arduino
arduino = serial.Serial(port=comport, baudrate=115200)

# Loading both the YOLO retrained model and the CNN classification model
CNN = tf.keras.models.load_model('D:/projects/CNN_hand_project/CNN_model_extended.keras')
yolo = YOLO('D:/projects/CNN_hand_project/bestv2.pt')

# Setting camera capture
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

while True:
    # Get image from camera
    ret, img= cap.read()
    # get results from the YOLO model
    results = yolo.predict(img, conf = 0.2, imgsz= (640, 480), max_det=1)[0]
    annotated_frame = results.plot()
    # Present bordered box
    cv2.imshow("YOLOv8 Inference", annotated_frame)
    bounds = sv.Detections.from_ultralytics(results).xyxy
    # If any detection is found, the image would be cropped using the borderbox, passed to CNN and returns prediction package to the arduino
    if len(bounds) > 0:
        [xmin, ymin, xmax, ymax] = bounds[0]
        cropped = img[int(ymin):int(ymax), int(xmin):int(xmax)]
        prediction = pass2CNN(cropped, CNN)
        pred_img = cv2.imread("D:/projects/CNN_hand_project/"+str(prediction)+".jpg")
        cv2.imshow("prediction", pred_img)
        strpred = str(prediction) + "\r"
        arduino.write(strpred.encode())
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
  