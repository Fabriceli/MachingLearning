# -*-coding:utf-8 -*-
# Reference:**********************************************
# @Time     : 2019-09-22 10:51
# @Author   : Fabrice LI
# @File     : generate_anchor.py
# @User     : liyihao
# @Software: PyCharm
# @Description: todo
# Reference:**********************************************
import numpy as np


def get_scale_anchors(anchor, scales):
    w, h, x_ctr, y_ctr = whctrs(anchor)
    ws = w * scales
    hs = h * scales
    anchors = make_anchors(ws, hs, x_ctr, y_ctr)
    return anchors


def generate_anchor(base_size=16, ratios=[0.5, 1, 2], scales=2 ** np.arange(3, 6)):
    base_anchor = np.array([1, 1, base_size, base_size]) - 1
    ratios_anchors = get_ratios_anchor(base_anchor, ratios)
    anchors = np.vstack([get_scale_anchors(ratios_anchors[i, :], scales) for i in range(ratios_anchors.shape[0])])
    return anchors


def get_ratios_anchor(anchor, ratios):
    # 找到anchor长宽和中心点
    w, h, x_ctr, y_ctr = whctrs(anchor)
    # 不同的ratios做我们的anchor
    # 但是长宽是按照ratios变化，不变的是面积
    area = w * h
    area_ratios = area / ratios  # 算出系数
    ws = np.round(np.sqrt(area_ratios))
    hs = np.round(ws * ratios)
    # 找anchors
    anchors = make_anchors(ws, hs, x_ctr, y_ctr)
    return anchors


def make_anchors(ws, hs, x_ctr, y_ctr):
    ws = ws[:, np.newaxis]
    hs = hs[:, np.newaxis]
    # 做四边,四个角
    anchors = np.hstack((x_ctr - 0.5 * (ws - 1),
                         y_ctr - 0.5 * (hs - 1),
                         x_ctr + 0.5 * (ws - 1),
                         y_ctr + 0.5 * (hs - 1)
                         ))
    return anchors


def whctrs(anchor):
    # anchor => (x1, y1, x2, y2, conf)
    w = anchor[2] - anchor[0] + 1  # x2 - x1 + 1
    h = anchor[3] - anchor[1] + 1  # y2 - y1 + 1
    x_ctr = anchor[0] + (w - 1) / 2  # 二分法要点1，防止溢出 left + (right - left) / 2 or (left + right) >> 1
    y_ctr = anchor[1] + (h - 1) / 2
    return w, h, x_ctr, y_ctr


if __name__ == '__main__':
    anchors = generate_anchor()
    print(anchors)
