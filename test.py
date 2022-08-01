import os
import cv2
from utils.boxes import Box 

if __name__ == '__main__':
    imgPath = r"./images/eagle.jpg"
    img = cv2.imread(imgPath)
    xmin = 81
    xmax = 384
    ymin = 112
    ymax = 488
    cv2.rectangle(img, (xmin, ymin), (xmax, ymax), (0,0,255), 2)
    #cv2.rectangle(img, (xmin, ymax), (xmax, ymin), (255,0,0), 2)
    cv2.imshow('src',img)
    cv2.waitKey()
