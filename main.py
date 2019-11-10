# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 22:06:44 2019

@author: saitej
"""
import cv2 as cv
import numpy as np

roadImage = cv.imread("roadImage.jpg")
#cv.resize(roadImage,(500,500))
roadImageBackup = np.copy(roadImage)
gray = cv.cvtColor(roadImageBackup,cv.COLOR_RGB2GRAY)
cv.imshow("Testing Image", roadImage)
#cv.resizeWindow(winname="Testing Image", size=(500,500))
cv.waitKey(1000000000)
cv.destroyAllWindows()

