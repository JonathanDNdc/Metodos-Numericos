from scripts.Function import *


def secante(str_func, xi0, xi1, acc_error=0.000000001, itn=250):
    eps = acc_error + 1
    it = 0
    while eps > acc_error:
        it += 1
        try:
            fxi0 = float(f(str_func, xi0))
            fxi1 = float(f(str_func, xi1))
        except TypeError:
            return "Dominio invalido", 0
        except SympifyError:
            return "Error de sintaxis", 0

        try:
            xi1, xi0 = xi1 - fxi1 * (xi0 - xi1) / (fxi0 - fxi1), xi1
            eps = abs((xi1 - xi0) / xi1)
        except ZeroDivisionError:
            if f(str_func, xi1) == 0:
                return xi1, 1
            else:
                return "Intenta con nuevos valores iniciales", 1
        if eps == nan:
            return 0, 1
        if it > itn:
            return "No converge", 1
    return round(xi1, 6), 1
