# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2019-09-24 20:42
# @Author   : Fabrice LI
# @File     : week2.py
# @User     : liyihao
# @Software: PyCharm
# @Description: todo
#Reference:**********************************************
import cv2
import numpy as np

img = cv2.imread('lenna.jpeg')
# cv2.imshow('lenna', img)
print(img)
print(cv2.getGaussianKernel(7, 1))
# cv2.waitKey()
# cv2.destroyAllWindows()
