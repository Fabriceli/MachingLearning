# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2019-10-17 21:58
# @Author   : Fabrice LI
# @File     : week1.py
# @User     : liyihao
# @Software : PyCharm
# @Description: week 1 assignment
#Reference:**********************************************
import cv2
import numpy as np
from matplotlib import pyplot as plt
import random


def read_image():
    # 读取图片 B，G，R，返回一个ndarray类型
    # cv2.IMREAD_COLOR  # 以彩色模式读入 1
    # cv2.IMREAD_GRAYSCALE  # 以灰色模式读入 0
    img_gray = cv2.imread('lenna.jpeg', cv2.IMREAD_COLOR)
    # cv2.imshow('lenna', img_gray)
    # 返回多维矩阵，#(225, 225, 3)，
    print(type(img_gray), img_gray.shape, img_gray.size, img_gray.dtype)
    # ravel()展平n维矩阵的所有
    print(img_gray.ravel(), len(img_gray.ravel()))
    return img_gray


# 2. Please change image color through YUV space
def changeyuv(img):
    # cv2.COLOR_BGR2GRAY;cv2.COLOR_BGR2HSV
    # 彩色图像转灰度图像YUV(Y即为灰度图) Y = 0.299R + 0.587G + 0.114B
    B, G, R = cv2.split(img)
    cv2.imshow('rgb', img)
    cv2.imshow('B', B)
    cv2.imshow('G', G)
    cv2.imshow('R', R)
    img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('gray', img1)
    # 彩色图像转灰度图像YUV(Y->亮度；U,V->色度)
    img2 = cv2.cvtColor(img, cv2.COLOR_RGB2YUV)
    Y, U, V = cv2.split(img2)
    cv2.imshow('yuv', img2)
    cv2.imshow('Y', Y)
    cv2.imshow('U', U)
    cv2.imshow('V', V)
    cv2.waitKey()
    cv2.destroyAllWindows()


def random_light_color(img):
    B, G, R = cv2.split(img)
    b_rand = random.randint(-50, 50)
    if b_rand == 0:
        pass
    elif b_rand > 0:
        lim = 255 - b_rand
        B[B > lim] = 255
        B[B <= lim] = (b_rand + B[B <= lim]).astype(img.dtype)
    elif b_rand < 0:
        lim = 0 - b_rand
        B[B < lim] = 0
        B[B >= lim] = (b_rand + B[B >= lim]).astype(img.dtype)

    g_rand = random.randint(-50, 50)
    if g_rand == 0:
        pass
    elif g_rand > 0:
        lim = 255 - g_rand
        G[G > lim] = 255
        G[G <= lim] = (g_rand + G[G <= lim]).astype(img.dtype)
    elif g_rand < 0:
        lim = 0 - g_rand
        G[G < lim] = 0
        G[G >= lim] = (g_rand + G[G >= lim]).astype(img.dtype)

    r_rand = random.randint(-50, 50)
    if r_rand == 0:
        pass
    elif r_rand > 0:
        lim = 255 - r_rand
        R[R > lim] = 255
        R[R <= lim] = (r_rand + R[R <= lim]).astype(img.dtype)
    elif r_rand < 0:
        lim = 0 - r_rand
        R[R < lim] = 0
        R[R >= lim] = (r_rand + R[R >= lim]).astype(img.dtype)
    img_merge = cv2.merge((B, G, R))
    return img_merge


if __name__ == '__main__':
    img = read_image()
    # changeyuv(img)
    img_random = random_light_color(img)
    cv2.imshow('img_random', img_random)
    cv2.waitKey()
    cv2.destroyAllWindows()
