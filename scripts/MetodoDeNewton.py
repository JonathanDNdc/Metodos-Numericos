from sympy import *
import scripts.Matrices as mt


def newton(funciones_str, initials_str, err=0.000000001, itn=250):
    nan_flag = False
    initials = {}
    for i in initials_str.split(","):
        initials[i.split("=")[0].strip()] = float(i.split("=")[1].strip())

    funciones = [S(fun) for fun in funciones_str.split(",")]
    variables = [Symbol(str(var)) for var in initials.keys()]
    mat_jac = [[diff(fun, var) for var in variables] for fun in funciones]
    mat_jac_latex = [[latex(n) for n in row] for row in mat_jac]
    errs = [err + 1 for n in variables]
    it = 0
    while not all(n < err for n in errs):
        it += 1
        mat_jac_sub = [[N(real_root(n.subs(initials))) for n in row] for row in mat_jac]
        f = [[N(real_root(fn.subs(initials)))] for fn in funciones]
        if mt.det(mat_jac_sub) == 0:
            return "Intenta con nuevos valores iniciales", initials, mat_jac_latex, funciones
        dx = mt.mmult(mt.minverse(mat_jac_sub), f)
        for n in range(len(dx)):
            try:
                new_value = initials[str(list(variables)[n])] - dx[n][0]
            except KeyError:
                return "Ingresa todos los valores inciales", initials, mat_jac_latex, funciones
            if not new_value.is_real:
                return "Intenta con nuevos valores iniciales", initials, mat_jac_latex, funciones

            new_error = Abs((new_value - initials[str(list(variables)[n])])/new_value)
            if errs[n] == new_error == 1:
                return "No converge", initials, mat_jac_latex, funciones
            errs[n] = new_error 
            initials[str(list(variables)[n])] = new_value

        for n in range(len(errs)):
            if errs[n] == nan:
                errs[n] = 0

        if it > itn:
            return "No converge", initials, mat_jac_latex, funciones

    for key, value in initials.items():
        initials[key] = round(value, 6)
        
    return initials, initials, mat_jac_latex, funciones
