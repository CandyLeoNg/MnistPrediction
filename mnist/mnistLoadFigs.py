import cv2

import os

from keras.datasets import mnist

import numpy as np

str_1 = 'mnisttrain'

str_2 = 'mnisttest'

if os.path.exists(str_1) is False:
    os.mkdir(str_1)

if os.path.exists(str_2) is False:
    os.mkdir(str_2)

# 自动下载mnist数据集

(X_train, Y_train), (X_test, Y_test) = mnist.load_data()

for i in range(0, 59999):  # 迭代 0 到 59999 之间的数字

    fileName = "mnisttrain/" + str(Y_train[i]) + "_" + str(i) + ".jpg"

    cv2.imwrite(fileName, X_train[i])

for i in range(0, 9999):  # 迭代 0 到 9999 之间的数字

    fileName = "mnisttest/" + str(Y_test[i]) + "_" + str(i) + ".jpg"

    cv2.imwrite(fileName, X_test[i])
