from sympy import *
import numpy as np


def euler(x0, xn, y1, y2, f1, f2, h, order):
    f1 = lambdify(("x", "y1", "y2"), f1, "numpy")
    if order == "orden2":
        f2 = lambdify(("x", "y1", "y2"), f2, "numpy")
    else:
        f2 = f1

    xlist = np.arange(x0, xn + h, h)
    y1list = np.empty(xlist.size)
    y2list = np.empty(xlist.size)

    y1list[0] = y1
    y2list[0] = y2

    for x in range(1, xlist.size):
        y1list[x] = y1list[x - 1] + h * f1(xlist[x - 1], y1list[x - 1], y2list[x - 1])
        y2list[x] = y2list[x - 1] + h * f2(xlist[x - 1], y1list[x - 1], y2list[x - 1])

    return xlist, y1list, y2list
