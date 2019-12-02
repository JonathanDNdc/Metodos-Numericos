from scripts.Function import *


def secante(str_func, xi0, xi1, acc_error=0.000000001, itn=250):
    eps = acc_error + 1
    it = 0
    fxi1 = 0
    while eps > acc_error:
        it += 1
        try:
            fxi0 = float(f(str_func, xi0))
            fxi1 = float(f(str_func, xi1))
        except TypeError:
            return "Dominio invalido"
        except SympifyError:
            return "Error de sintaxis"

        try:
            xi1, xi0 = xi1 - fxi1 * (xi0 - xi1) / (fxi0 - fxi1), xi1
            eps = abs((xi1 - xi0) / xi1)
        except ZeroDivisionError:
            if f(str_func, xi1) == 0:
                return xi1
            else:
                return "Intenta con nuevos valores iniciales"
        if eps == nan:
            return 0
        if it > itn:
            return "No converge"
    return round(xi1, 6)
