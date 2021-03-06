# -*-coding:utf-8 -*-
# Reference:**********************************************
# @Time     : 2019-08-25 18:33
# @Author   : Fabrice LI
# @File     : week4.py
# @User     : liyihao
# @Software: PyCharm
# @Description: todo
# Reference:**********************************************
import numpy as np
import sklearn.datasets
import sklearn.linear_model

# generate data set
np.random.seed(0)
X, y = sklearn.datasets.make_moons(200, noise=0.2)

num_examples = len(X)
nn_input_dim = 2
nn_output_dim = 2

lr = 0.01
reg_lamba = 0.01


def calculate_loss(model):
    w1, b1, w2, b2 = model['w1'], model['b1'], model['w2'], model['b2']
    z1 = X.dot(w1) + b1
    a1 = np.tanh(z1)

    z2 = a1.dot(w2) + b2
    exp_scores = np.exp(z2)
    probs = exp_scores / np.sum(exp_scores, axis=1, keepdims=True)
    log_probs = -np.log(probs[range(num_examples), y])
    loss = np.sum(log_probs)
    return 1./num_examples *loss


def build_model(nn_dim, num_passes=30000, print_loss=False):
    w1 = np.random.randn(nn_input_dim, nn_dim) / np.sqrt(nn_input_dim)
    b1 = np.zeros((1, nn_dim))
    w2 = np.random.randn(nn_dim, nn_output_dim) / np.sqrt(nn_dim)
    b2 = np.zeros((1, nn_output_dim))

    model = {}

    # Gradient descent.
    for i in range(0, num_passes):
        # forward
        z1 = X.dot(w1) + b1
        a1 = np.tanh(z1)
        z2 = a1.dot(w2) + b2
        # softmax 多分类
        exp_scores = np.exp(z2)
        probs = exp_scores / np.sum(exp_scores, axis=1, keepdims=True)

        # bp
        # 求loss
        delta3 = probs
        delta3[range(num_examples), y] -= 1
        dw2 = (a1.T).dot(delta3)
        db2 = np.sum(delta3, axis=0, keepdims=True)
        delta2 = delta3.dot(w2.T) * (1 - np.power(a1, 2))
        dw1 = np.dot(X.T, delta2)
        db1 = np.sum(delta2, axis=0)

        #
        w1 += -lr * dw1
        b1 += -lr * db1
        w2 += -lr * dw2
        b2 += -lr * db2

        model = {'w1': w1, 'b1': b1, 'w2': w2, 'b2': b2}
        if print_loss & i % 1000 == 0:
            print("loss after iteration %i: %f" % (i, calculate_loss(model)))
    return model


model = build_model(10, print_loss=True)
