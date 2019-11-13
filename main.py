# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 22:06:44 2019

@author: saitej
"""
!pip install numpy
!pip install matplotlib
!pip install opencv-python
!pip install opencv-contrib-python
#!pip install opencv-python-headless
#!pip install opencv-contrib-python-headless

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


def readImage(imageName):
    img = cv.imread(imageName)
    return img

def showImage(img, msg):
    cv.imshow(msg, img)
    cv.waitKey(0)
    cv.destroyAllWindows()

def grayImage(img):
    gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
    showImage(gray, "Gray Scaled Image - Press Any Key to Continue")
    return gray

def GaussianBlur(img):
    gaussianBlur = cv.GaussianBlur(img, (5,5), 0)
    showImage(gaussianBlur, "Gaussian Blured Image - Press Any Key to Continue")
    return gaussianBlur

def edgeDetection(img):
    canny = cv.Canny(img, 50,150)
    showImage(canny, "Edge Detection Image - Press Any Key to Continue")
    return canny

def graphShow(img):
    plt.imshow(img)
    plt.show()

# Manual technique to find the mask of an image - Finding mask manually
def findingMask(img):
    height = img.shape[0]
    trianglePolygon = np.array([[(200,height), (1100,height), (600,300)]])
    mask = np.zeros_like(img) # creates array same shape as image of zeros
    cv.fillPoly(mask, trianglePolygon, color = 255) #color 255 is white
    return mask

def regionOfInterest(img):
    mask = findingMask(img)
    roadDetectedImage = cv.bitwise_and(img, mask)
    return roadDetectedImage

if __name__=="__main__":
    roadImage = readImage("roadImage.jpg")
    roadImageBackup = np.copy(roadImage)
    showImage(roadImage, "Testing Image - Press Any Key to Continue")
    grayScaleImage = grayImage(roadImageBackup)
    gaussianBlur = GaussianBlur(grayScaleImage)
    EdgeDetection = edgeDetection(gaussianBlur)
    graphShow(EdgeDetection)
    print(7*" "+"Canny Edges plotted on graph")
    # roadImage.shape[0] = Height (Maximum y) and roadImage.shape[1] = Width (Maximum x)
    
    detectedImageWithAreaOfInterest = regionOfInterest(EdgeDetection)
    showImage(detectedImageWithAreaOfInterest, "Road Detected Manually by AND operation on masking and image - Press Any Key to Continue")
    
    lines = cv.HoughLinesP(detectedImageWithAreaOfInterest, 2, np.pi/180, 100, np.array([]), minLineLength = 40, maxLineGap = 5) # r=2, theta and threshold
    showImage(detectedImageWithAreaOfInterest, "Hough Transform Space for Detecting lines in an Image - Press Any Key to Continue")