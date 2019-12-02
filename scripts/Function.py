from sympy import *
from matplotlib import pyplot as plt
import numpy as np
from mayavi import mlab
mlab.options.offscreen = True


def f(str_func, x):
    func = sympify(str_func)
    return func.subs(list(func.free_symbols)[0], x)


fv = np.vectorize(f)


def matrix2latex(mat):
    if not mat:
        return ""
    lat_mat = "\\begin{bmatrix}"
    lat_mat += "\\\\".join(["&".join([str(col) for col in row]) for row in mat])
    lat_mat += "\\end{bmatrix}"
    return lat_mat


def diff2latex(xn, y1, y2, h, order):
    latex1 = "\\begin{gather*}" \
               f"y1({xn})={round(y1, 6)}~\\\\"
    if order == "orden2":
        latex1 += f"y2({xn})={round(y2, 6)}~\\\\"

    return latex1 + "\\end{gather*}"


def graph(str_func, a, b):
    try:
        x = np.linspace(a, b, 1000)
        y = fv(str_func, x)

        plt.figure(figsize=(7.2, 7.2))
        plt.title(str_func)
        plt.axhline(y=0, linewidth=0.5, color="k")
        plt.plot(x, y)
        plt.savefig('static/images/my_fig.png')
    except:
        pass


def graph_implicit(func, variables, point1, lx=-10, ux=10, ly=-10, uy=10, lz=-10, uz=10, res=1):
    flag = 1
    if type(point1) == str:
        point1 = False
    else:
        point1 = list(point1.values())
    variables = list(variables)
    if len(variables) == 2:
        flag = plot2dfuncs(func[0], func[1], variables, point1, lx, ux, ly, uy)
    elif len(variables) == 3:
        flag = plot3funcs(func[0], func[1], func[2], variables, point1, lx, ux, ly, uy, lz, uz, res)
    return flag


def plot3funcs(func1, func2, func3, variables, point1, lx=-10, ux=10, ly=-10, uy=10, lz=-10, uz=10, res=1.0):
    try:
        stepsx = (ux - lx) / (10 * res)
        stepsy = (uy - ly) / (10 * res)
        stepsz = (uz - lz) / (10 * res)
        x, y, z = np.mgrid[lx:ux + stepsx:stepsx, ly:uy + stepsy:stepsy, lz:uz + stepsz:stepsz]

        f1 = lambdify(variables, func1, "numpy")
        f2 = lambdify(variables, func2, "numpy")
        f3 = lambdify(variables, func3, "numpy")

        values1 = f1(x, y, z)
        values2 = f2(x, y, z)
        values3 = f3(x, y, z)

        fig = mlab.figure(size=(720, 720), bgcolor=(1, 1, 1), fgcolor=(0, 0, 0))
        mlab.contour3d(x, y, z, values1, figure=fig, contours=[0], color=(1, 0, 0))
        mlab.contour3d(x, y, z, values2, figure=fig, contours=[0], color=(0, 1, 0))
        mlab.contour3d(x, y, z, values3, figure=fig, contours=[0], color=(0, 0, 1))
        if point1:
            mlab.points3d(point1[0], point1[1], point1[2], color=(0.5, 0.5, 0.5))
        mlab.axes(figure=fig, extent=(lx, ux, ly, uy, lz, uz), xlabel=variables[0], ylabel=variables[1],
                  zlabel=variables[2])
        mlab.gcf().scene.parallel_projection = True

        mlab.savefig('static/images/my_fig.png')
        return 0
    except:
        return 1


def plot2dfuncs(func1, func2, variables, point1, lx=-10, ux=10, ly=-10, uy=10):
    try:
        fig, ax = plt.subplots(figsize=(12.2, 12.6))
        xx, yy = np.linspace(lx, ux, 1000), np.linspace(ly, uy, 1000)
        x, y = np.meshgrid(xx, yy)

        fimp1 = lambdify(variables, func1, "numpy")
        fimp2 = lambdify(variables, func2, "numpy")
        ax.set_xlabel(variables[0])
        ax.set_ylabel(variables[1])
        ax.contour(x, y, fimp1(x, y), [0])
        ax.contour(x, y, fimp2(x, y), [0])
        if point1:
            ax.plot(point1[0], point1[1], "o")
        ax.set_aspect('equal', 'datalim')
        plt.savefig('static/images/my_fig.png')
        return 0
    except:
        return 1


def plotdiferencial(x, y1, y2, order):
    try:
        if order == "orden2":
            fig, (ax1, ax2) = plt.subplots(2, figsize=(11.7, 12.4))
        else:
            fig, ax1 = plt.subplots(figsize=(11.7, 12.4))

        ax1.plot(x, y1)
        ax1.set(xlabel='x', ylabel='y1')

        if order == "orden2":
            ax2.plot(x, y2)
            ax2.set(xlabel='x', ylabel='y2')

        plt.savefig('static/images/my_fig.png')
    except:
        pass


def has_linear_solution(m):
    latb = "\\mbox{"
    late = "}~\\\\~\\\\"
    m = np.array(m)
    mn = np.delete(m, -1, 1)
    rango_aum = np.linalg.matrix_rank(m)
    rango_nor = np.linalg.matrix_rank(mn)
    if rango_aum != rango_nor:
        return latb + "No tiene solucion" + late
    else:
        if rango_nor < len(mn[0]):
            return latb + "Infinitas soluciones" + late
        elif rango_nor == len(mn[0]):
            return latb + "Solucion unica " + late


def slashconverter(func_str):
    return func_str.replace("|", "/")
