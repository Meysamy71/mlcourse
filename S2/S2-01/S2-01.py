"""
File: S2-01.py
Author: Meysam Yavarikhoo
Date: 2024/05/28
Version: 1.0.0
License: GPLv3
Description: A simple Python script to image slicing
"""

import numpy as np
import cv2

img = cv2.imread('img.jpg', 0)


def SliceImg(y1, y2, x1, x2):
    Slice = img[y1:y2, x1:x2]
    Resize = cv2.resize(Slice, (28, 28))
    Numpy = np.array(Resize)
    Flat = Numpy.flatten()
    return Flat


num0 = SliceImg(370,520,70,160)
num1 = SliceImg(350,500,180,270)
num2 = SliceImg(335,485,270,400)
num3 = SliceImg(335,485,440,570)
num4 = SliceImg(320,465,610,730)
num5 = SliceImg(305,455,760,910)
num6 = SliceImg(280,430,960,1070)
num7 = SliceImg(290,440,1145,1285)
num8 = SliceImg(570,730,330,500)
num9 = SliceImg(560,720,610,760)

Numbers = np.column_stack((num0, num1, num2, num3, num4, num5, num6, num7, num8, num9))
Numbers.tofile('img.csv', sep=',')