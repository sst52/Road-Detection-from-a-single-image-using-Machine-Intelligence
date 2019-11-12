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

roadImage = cv.imread("roadImage.jpg")
#cv.resize(roadImage,(500,500))
roadImageBackup = np.copy(roadImage)
gray = cv.cvtColor(roadImageBackup,cv.COLOR_RGB2GRAY)
cv.imshow("Testing Road Image - Press Any Key to Continue", roadImage)
#cv.resizeWindow(winname="Testing Image", size=(500,500))
cv.waitKey(0)
cv.destroyAllWindows()
cv.imshow("Gray Scale Image - Press Any Key to Continue", gray)
cv.waitKey(0)
cv.destroyAllWindows()
gaussianBlur = cv.GaussianBlur(gray, (5,5), 0)
gaussianBlurColoredImage = cv.GaussianBlur(roadImage, (5,5), 0)
cv.imshow("Gaussian Blured Image - Press Any Key to Continue", gaussianBlur)
cv.waitKey(0)
cv.destroyAllWindows()
cv.imshow("Gaussian Blured Color Image - Press Any Key to Continue", gaussianBlurColoredImage)
cv.waitKey(0)
cv.destroyAllWindows()
edgeDetection = cv.Canny(gray,50,150)
cv.imshow("Edge Detected Image - Press Any Key to Continue", edgeDetection)
cv.waitKey(0)
cv.destroyAllWindows()
ok