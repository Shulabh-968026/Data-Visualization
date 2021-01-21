import cv2 as cv
import numpy as np

def nothing():
    pass
#capture the video
video=cv.VideoCapture(0) #0 for webcam
cv.namedWindow('sketch')
cv.createTrackbar('LTC','sketch',0,255,nothing)
cv.createTrackbar('UTC','sketch',0,255,nothing)

while True:
    isTrue,frame=video.read()
    #canvert live video in gray image
    image=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)

    #apply gaussian blur on image
    blurimage=cv.GaussianBlur(image,(5,5),0)

    ltc=cv.getTrackbarPos('LTC','sketch')
    utc=cv.getTrackbarPos('UTC','sketch')
    #find edge in image
    cannyimage=cv.Canny(blurimage,ltc,utc)

    #divide image in to white and black color
    ret,threshold=cv.threshold(cannyimage,50,255,cv.THRESH_BINARY_INV)

    #show images
    #cv.imshow('original',frame)
    cv.imshow('sketch',threshold)

    if cv.waitKey(20) & 0xFF==ord('q'):
        break

video.release()
cv.destroyAllWindows()
    