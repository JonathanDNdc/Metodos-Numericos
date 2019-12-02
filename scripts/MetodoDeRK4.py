from sympy import *
import numpy as np


def rk4(x0, xn, y1, y2, f1, f2, h, order):
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
        k1y1 = h * f1(xlist[x - 1], y1list[x - 1], y2list[x - 1])
        k1y2 = h * f2(xlist[x - 1], y1list[x - 1], y2list[x - 1])
        k2y1 = h * f1(xlist[x - 1] + h / 2, y1list[x - 1] + k1y1 / 2, y2list[x - 1] + k1y2 / 2)
        k2y2 = h * f2(xlist[x - 1] + h / 2, y1list[x - 1] + k1y1 / 2, y2list[x - 1] + k1y2 / 2)
        k3y1 = h * f1(xlist[x - 1] + h / 2, y1list[x - 1] + k2y1 / 2, y2list[x - 1] + k2y2 / 2)
        k3y2 = h * f2(xlist[x - 1] + h / 2, y1list[x - 1] + k2y1 / 2, y2list[x - 1] + k2y2 / 2)
        k4y1 = h * f1(xlist[x - 1] + h, y1list[x - 1] + k3y1, y2list[x - 1] + k3y2)
        k4y2 = h * f2(xlist[x - 1] + h, y1list[x - 1] + k3y1, y2list[x - 1] + k3y2)

        y1list[x] = y1list[x - 1] + (k1y1 + 2 * k2y1 + 2 * k3y1 + k4y1) / 6
        y2list[x] = y2list[x - 1] + (k1y2 + 2 * k2y2 + 2 * k3y2 + k4y2) / 6

    return xlist, y1list, y2list
