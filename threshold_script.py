
import cv2
import os
# Applying preprocessing
def apply_filter(src):
    image = cv2.imread(src, cv2.IMREAD_GRAYSCALE)
    image = cv2.resize(image, (300, 300))
    image = cv2.medianBlur(image, 11)
    image = cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
    return image

path = 'dataset/finger_count_data/data/test/'
dist = 'threshold/test/'

# Going through all data and threshold it before training
for i in range(6):
    src = path + str(i) + '/'
    dst = dist + str(i) + '/'
    for filename in os.listdir(src):
        if filename.endswith('.jpg'): 
            img_path = src + filename
            img = apply_filter(img_path)
            cv2.imwrite(dst + filename, img)

