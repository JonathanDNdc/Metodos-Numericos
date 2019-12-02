from sympy import *


def jacobi(funciones_str, initials_str, err=0.000000001, it=250):

    nan_flag = False
    initials = {}
    for i in initials_str.split(","):
        initials[i.split("=")[0].strip()] = float(i.split("=")[1].strip())

    new_initials = dict(initials)
    funciones = [S(fun) for fun in funciones_str.split(",")]

    variables = [Symbol(str(var)) for var in initials.keys()]
    mat = [[float(Poly(fn, var).all_coeffs()[0]) if len(Poly(fn, var).all_coeffs()) > 1 else 0 for var in variables] +
           [-float(Add.make_args(fn)[0]) if len(Add.make_args(fn)[0].free_symbols) == 0 else 0] for fn in funciones]

    for n in funciones:
        if not Poly(n).is_linear:
            return "Funcion no lineal", initials, mat, funciones
    
    errs = [err + 1 for n in variables]
    itn = 0
    while not all(n < err for n in errs):
        itn += 1
        for func, var, var1 in zip(mat, variables, range(len(variables))):
            a = func[-1]
            for var2, var3 in zip(variables, range(len(variables))):
                if var != var2:
                    a -= initials[str(var2)] * func[var3]
            try:
                a /= func[var1]
            except ZeroDivisionError:
                return "Reordena la matriz", new_initials, mat, funciones
            new_initials[str(var)] = round(a, 12)
            try:
                errs[var1] = Abs((new_initials[str(var)] - initials[str(var)]) / new_initials[str(var)])
            except ZeroDivisionError:
                pass
        initials = dict(new_initials)

        for n in errs:
            if n == nan:
                nan_flag = True

        if nan_flag:
            break
        
        if itn > it:
            return "No converge", new_initials, mat, funciones

    for key, value in new_initials.items():
        new_initials[key] = round(value, 6)

    return new_initials, new_initials, mat, funciones
