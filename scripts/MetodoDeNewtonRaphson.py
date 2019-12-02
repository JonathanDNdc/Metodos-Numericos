from scripts.Function import *


def newton_raphson(str_func, xi, acc_error=0.000000001, itn=250):
    xi = [xi] * 2
    eps = acc_error + 1

    it = 0
    while eps > acc_error:
        it += 1

        fxi0 = float(f(str_func, xi[0]))
        dfxi0 = float(f(diff(str_func), xi[0]))
        if dfxi0 == 0:
            return "Intenta con nuevos valores iniciales"

        xi[0], xi[1] = xi[0] - fxi0 / dfxi0, xi[0]

        try:
            eps = abs((xi[1] - xi[0]) / xi[1])
        except ZeroDivisionError:
            if fxi0 == 0:
                return 0

        if it > itn:
            return "No converge"

    return round(xi[1], 4)
