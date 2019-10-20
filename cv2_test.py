# -*-coding:utf-8 -*-
# Reference:**********************************************
# @Time     : 2019-08-22 21:30
# @Author   : Fabrice LI
# @File     : cv2_test.py
# @User     : liyihao
# @Software: PyCharm
# @Description: line regression
# Reference:**********************************************

import numpy as np
import random
import torch

# hypothesis  function
def inference(theta1, theta0, x):
    pred_h = theta1 * x + theta0  # (theta1, theta0) = theta [theta0: bias, theta1: weight]
    return pred_h


# cost function
def eval_loss(theta1, theta0, x_list, gt_y_list):
    avg_loss = 0.0
    for i in range(len(x_list)):
        avg_loss += 0.5 * (theta1 * x_list[i] + theta0 - gt_y_list[i]) ** 2
    avg_loss /= len(gt_y_list)
    return avg_loss


def gradient(pred_h, gt_y, x):  # 求导
    diff = pred_h - gt_y
    d_theta1 = diff * x
    d_theta0 = diff
    return d_theta1, d_theta0


def cal_step_gradient(batch_x_list, batch_gt_y_list, w, b, lr):
    avg_dw, avg_db = 0, 0
    batch_size = len(batch_x_list)
    for i in range(batch_size):
        pred_y = inference(w, b, batch_x_list[i])
        dw, db = gradient(pred_y, batch_gt_y_list[i], batch_x_list[i])
        avg_dw += dw
        avg_db += db
    avg_db /= batch_size
    avg_dw /= batch_size
    w -= lr * avg_dw
    b -= lr * avg_db
    return w, b


def train(x_list, gt_y_list, batch_size, lr, max_iter):
    w = 0
    b = 0
    num_samples = len(x_list)
    for i in range(max_iter):
        batch_idxs = np.random.choice(num_samples, batch_size)
        batch_x = [x_list[j] for j in batch_idxs]
        batch_y = [gt_y_list[j] for j in batch_idxs]
        w, b = cal_step_gradient(batch_x, batch_y, w, b, lr)
        print("w: {0}, b: {1}".format(w, b))
        print("loss is : {0}".format(eval_loss(w, b, x_list, gt_y_list)))


def gen_sample_data():
    w = random.randint(0, 10) + random.random()
    b = random.randint(0, 5) + random.random()
    num_samples = 100
    x_list = []
    y_list = []
    for i in range(num_samples):
        x = random.randint(0, 100) * random.random()
        y = w * x + b + random.random() * random.randint(-1, 1)
        x_list.append(x)
        y_list.append(y)
    return x_list, y_list, w, b


def run():
    x_list, y_list, w, b = gen_sample_data()
    lr = 0.0009
    max_iter = 10000
    train(x_list, y_list, 50, lr, max_iter)


if __name__ == '__main__':
    run()
