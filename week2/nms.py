# -*-coding:utf-8 -*-
# Reference:**********************************************
# @Time     : 2019-09-19 22:30
# @Author   : Fabrice LI
# @File     : nms.py
# @User     : liyihao
# @Software: PyCharm
# @Description: todo
# Reference:**********************************************
import numpy as np


def NMS(lists, thre):
    # input [0, 4]:坐标值x1,x2,y1,y2; list[4]:score
    if len(lists) == 0:
        return {}
    lists = np.array(lists)
    res = []
    x1, x2, y1, y2, score = [lists[:, i] for i in range(5)]
    area = (x2 - x1 + 1) * (y1 - y2 + 1)
    # 从大到小排序score，降序
    idxs = score.argsort()[::-1]
    # idxs = np.argsort(score) 升序
    while len(idxs):
        i = idxs[0]  # 最大值
        res.append(i)

        xmin = np.maximum(x1[i], x1[idxs[1:]])
        ymin = np.maximum(y1[i], y1[idxs[1:]])
        xmax = np.minimum(x2[i], x2[idxs[1:]])
        ymax = np.minimum(y2[i], y2[idxs[1:]])

        w = np.maximum(0, xmax - xmin + 1)
        h = np.maximum(0, ymax - ymin + 1)
        inner_area = w * h

        iou = inner_area / (area[i] + area[idxs[1:]] - inner_area)
        idxs = idxs[np.where(iou < thre)[0] + 1]
    return res


def py_cpu_nms(dets, thresh):
    """Pure Python NMS baseline."""
    # x1、y1、x2、y2、以及score赋值
    dets = np.array(dets)
    x1 = dets[:, 0]
    y1 = dets[:, 1]
    x2 = dets[:, 2]
    y2 = dets[:, 3]
    scores = dets[:, 4]

    #每一个检测框的面积
    areas = (x2 - x1 + 1) * (y2 - y1 + 1)

    #按照score置信度降序排序
    order = scores.argsort()[::-1]
    keep = []
    #保留的结果框集合
    while order.size > 0:
        i = order[0]
        keep.append(i) #保留该类剩余box中得分最高的一个
        #得到相交区域,左上及右下
        xx1 = np.maximum(x1[i], x1[order[1:]])
        yy1 = np.maximum(y1[i], y1[order[1:]])
        xx2 = np.minimum(x2[i], x2[order[1:]])
        yy2 = np.minimum(y2[i], y2[order[1:]])

        #计算相交的面积,不重叠时面积为0
        w = np.maximum(0.0, xx2 - xx1 + 1)
        h = np.maximum(0.0, yy2 - yy1 + 1)
        inter = w * h
        #计算IoU：重叠面积 /（面积1+面积2-重叠面积）
        ovr = inter / (areas[i] + areas[order[1:]] - inter)
        #保留IoU小于阈值的box
        inds = np.where(ovr <= thresh)[0]
        order = order[inds + 1]
        #因为ovr数组的长度比order数组少一个,所以这里要将所有下标后移一位
    return keep



if __name__ == '__main__':
    lists = [[100, 100, 210, 210, 0.72],
             [105, 107, 215, 217, 0.76],
             [90, 95, 200, 205, 0.74],
             [101, 102, 211, 212, 0.78],
             [108, 107, 218, 217, 0.75],
             [1, 15, 150, 140, 0.80],
             [10, 30, 210, 210, 0.76]
             ]
    # print(NMS(lists, 0.5))
    print(py_cpu_nms(lists, 0.5))
