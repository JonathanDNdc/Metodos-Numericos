from flask import Flask, render_template
from flask_material import Material
import scripts.Function as scFunc
import scripts.MetodoDeBiseccion as mb
import scripts.MetodoDeSecante as ms
import scripts.MetodoDeNewtonRaphson as mnr
import scripts.MetodoDeBairstow as mbs
import scripts.MetodoDeJacobi as mj
import scripts.MetodoDeGaussSeidel as mgs
import scripts.MetodoDeNewton as mn
import scripts.MetodoDeEuler as me
import scripts.MetodoDeRK2 as mrk2
import scripts.MetodoDeRK4 as mrk4
from sympy import *
from mayavi import mlab

algebra_methods = ["biseccion", "secante", "newton_raphson", "bairstow"]
sis_agebra_methods = ["jacobi", "gauss_seidel", "newton"]
diferenciales_methods = ["euler", "runge-kutta-2", "runge-kutta-4"]

app = Flask(__name__)
Material(app)


@app.after_request
def add_header(response):
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/algebra/<metodo>')
def algebra(metodo, str_func="", lim_inf="", lim_sup="", ans_root="", c="", d="", e="250", err="0.001", load_img=0):
    if metodo in algebra_methods:
        return render_template("algebra.html", metodo=metodo, str_func=str_func, lim_inf=lim_inf, lim_sup=lim_sup,
                               ans_root=ans_root, c=c, d=d, e=e, err=err, load_img=load_img)


@app.route('/sistema_algebra/<metodo>')
def sis_algebra(metodo, func="", vars0="", err="0.001", it="250",
                lx="-10", ux="10", ly="-10", uy="10", lz="-10", uz="10", res="1",
                latexstring="", ans_vars="", load_img=0):
    if metodo in sis_agebra_methods:
        return render_template("sis_algebra.html", metodo=metodo, func=func, vars0=vars0, err=err, it=it,
                               lx=lx, ux=ux, ly=ly, uy=uy, lz=lz, uz=uz, res=res,
                               latex=latexstring, ans_vars=ans_vars, load_img=load_img)


@app.route('/diferenciales/<metodo>/')
def diferenciales(metodo, x0="", xn="", y1="", y2="", f1="", f2="", h="", order="orden1", latexstring="", load_img=0):
    if metodo in diferenciales_methods:
        return render_template("diferenciales.html", metodo=metodo,
                               x0=x0, xn=xn, y1=y1, y2=y2, f1=f1, f2=f2, h=h, order=order,
                               latex=latexstring, load_img=load_img)


@app.route('/algebra/<metodo>/<str_func>/<x0>/<x1>/<c>/<d>/<err>/<e>')
def graph(metodo, str_func, x0, x1, c, d, err, e):
    str_func = scFunc.slashconverter(str_func)
    scFunc.graph(str_func, float(x0), float(x1))
    if metodo == "biseccion":
        ans_root = mb.biseccion(str_func, float(c), float(d), float(err))
    elif metodo == "secante":
        ans_root = ms.secante(str_func, float(c), float(d), float(err), float(e))
    elif metodo == "newton_raphson":
        ans_root = mnr.newton_raphson(str_func, float(c), float(err), float(e))
    elif metodo == "bairstow":
        try:
            ans_root = mbs.bairstow(float(c), float(d), Poly(str_func).all_coeffs(), float(err))
        except PolynomialError:
            ans_root = "Funcion no polinomial"
    else:
        ans_root = 0
    return algebra(metodo, str_func, x0, x1, ans_root, c, d, e, err, 1)


@app.route('/sistema_algebra/<metodo>/<func>/<vars0>/<err>/<it>/<lx>/<ux>/<ly>/<uy>/<lz>/<uz>/<res>')
def lateximg_graph(metodo, func, vars0, err, it, lx, ux, ly, uy, lz, uz, res):
    func = scFunc.slashconverter(func)
    latexstring = ""
    ans_vars = ""
    funciones = ""
    variables = []

    try:
        lx = float(lx)
        ux = float(ux)
        ly = float(ly)
        uy = float(uy)
        lz = float(lz)
        uz = float(uz)
        res = float(res)

        if metodo == "jacobi":
            ans_vars, variables, mat, funciones = mj.jacobi(func, vars0, float(err), float(it))
            solutions = scFunc.has_linear_solution(mat)
            latexstring = solutions + scFunc.matrix2latex(mat)
        elif metodo == "gauss_seidel":
            ans_vars, variables, mat, funciones = mgs.gauss_seidel(func, vars0, float(err), float(it))
            solutions = scFunc.has_linear_solution(mat)
            latexstring = solutions + scFunc.matrix2latex(mat)
        elif metodo == "newton":
            ans_vars, variables, mat, funciones = mn.newton(func, vars0, float(err), float(it))
            latexstring = "J = " + scFunc.matrix2latex(mat)

    except (ValueError, IndexError) as ex_error:
        ans_vars = "Error de sintaxis"

    flag = scFunc.graph_implicit(funciones, variables, ans_vars, lx, ux, ly, uy, lz, uz, res)
    return sis_algebra(metodo, func, vars0, err, it, lx, ux, ly, uy, lz, uz, res, latexstring, ans_vars, flag)


@app.route('/diferenciales/<metodo>/<f1>/<y1>/<f2>/<y2>/<x0>/<xn>/<h>/<order>')
def diferenciales_latex(metodo, f1, y1, f2, y2, x0, xn, h, order):
    try:
        f1 = scFunc.slashconverter(f1)
        f2 = scFunc.slashconverter(f2)
        x0 = float(x0)
        xn = float(xn)
        y1 = float(y1)
        y2 = float(y2)
        h = float(h)
        y11 = 0
        y21 = 0
        xlist = []
        y1list = []
        y2list = []

        if metodo == "euler":
            xlist, y1list, y2list = me.euler(x0, xn, y1, y2, f1, f2, h, order)
            y11 = y1list[-1]
            y21 = y2list[-1]
        elif metodo == "runge-kutta-2":
            xlist, y1list, y2list = mrk2.rk2(x0, xn, y1, y2, f1, f2, h, order)
            y11 = y1list[-1]
            y21 = y2list[-1]
        elif metodo == "runge-kutta-4":
            xlist, y1list, y2list = mrk4.rk4(x0, xn, y1, y2, f1, f2, h, order)
            y11 = y1list[-1]
            y21 = y2list[-1]
        latexstring = scFunc.diff2latex(xn, y11, y21, h, order)
        scFunc.plotdiferencial(xlist, y1list, y2list, order)
    except (SyntaxError, ValueError, TypeError, ZeroDivisionError) as ex_error:
        latexstring = "\\mbox{Error de sintaxis}"
    return diferenciales(metodo, x0, xn, y1, y2, f1, f2, h, order, latexstring, 1)


if __name__ == '__main__':
    app.run()
