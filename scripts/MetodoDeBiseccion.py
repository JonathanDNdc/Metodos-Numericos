from scripts.Function import *


def xrf(xl, xu):
    return (xl + xu) / 2


def biseccion(str_func, xl, xu, acc_error=0.000000001):
    try:
        xr = [xrf(xl, xu)] * 2
        eps = acc_error + 1

        while eps > acc_error:
            if f(str_func, xl)*f(str_func, xr[1]) > 0:
                xl = xr[1]
            else:
                xu = xr[1]

            xr[0], xr[1] = xr[1], xrf(xl, xu)

            try:
                eps = abs((xr[1] - xr[0]) / xr[1])
            except ZeroDivisionError:
                return 0

        return round(xr[1], 4)

    except TypeError:
        return "Dominio invalido"
    except SympifyError:
        return "Error de sintaxis"

