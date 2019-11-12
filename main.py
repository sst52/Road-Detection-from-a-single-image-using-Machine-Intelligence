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

if __name__=="__main__":
    roadImage = readImage("roadImage.jpg")
    roadImageBackup = np.copy(roadImage)
    showImage(roadImage, "Testing Image - Press Any Key to Continue")
    grayScaleImage = grayImage(roadImageBackup)
    gaussianBlur = GaussianBlur(grayScaleImage)
    EdgeDetection = edgeDetection(gaussianBlur)