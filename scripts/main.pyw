import tkinter as tk
from tkinter import font

from sympy import Poly

import MetodoDeBiseccion as mb
import MetodoDeNewtonRaphson as mnr
import MetodoDeSecante as ms
import MetodoDeBairstow as mbrs


def customLabel(text, size, window):
    return tk.Label(window, text=text, bg=mainbgcolor, fg=txtcolor, font=(def_font,size))

def customButton(text, height, width, command, window):
    return tk.Button(window, text=text, command=command, bg=btncolor, fg=txtcolor, relief="ridge", borderwidth=1, height=height, width=width, font=def_font)

def rootwindow(root):
    
    root.title("Metodos Numericos")
    root.geometry("600x600")
    root["bg"] = mainbgcolor
    root.grid_columnconfigure(0, weight=1)
    
    title = customLabel("Metodos Numericos", 30, root)
    title.grid(row=0, pady=(50,30))
    
    biseccionbtn = customButton("Metodo de bisección", 2, 30, biseccionwindow, root)
    biseccionbtn.grid(row=1, pady=(20,0))

    newtonraphsonbtn = customButton("Metodo de Newton-Raphson", 2, 30, newtonraphsonwindow, root)
    newtonraphsonbtn.grid(row=2, pady=(20,0))

    secantebtn = customButton("Metodo de secante", 2, 30, secantewindow, root)
    secantebtn.grid(row=3, pady=(20,0))

    bairstowbtn = customButton("Metodo de bairstow", 2, 30, bairstowwindow, root)
    bairstowbtn.grid(row=4, pady=(20,0))


def biseccionwindow():
    t = tk.Toplevel()
    t.title("Metodo de bisección")
    t.geometry("600x600")
    t["bg"] = mainbgcolor
    t.grid_columnconfigure((0, 1, 2, 3, 4, 5), weight=1)

    title = customLabel("Metodo de bisección", 30, t)
    title.grid(row=0, columnspan=6, pady=(50,30))
    
    poly_lbl = customLabel("Función:", 15, t)
    poly_lbl.grid(row=1, column=0, columnspan=2, pady=(30,20))
    poly_e = tk.Entry(t)
    poly_e.grid(row=1, column=2, columnspan=4, pady=(30,20), padx=(0,30), ipady=5, sticky="we")

    limgrafica = customLabel("Limites de la grafica", 15, t)
    limgrafica.grid(row=2, columnspan=6)
    
    limgraficainf = customLabel("Inferior:", 15, t)
    limgraficainf.grid(row=3, column=0, columnspan=2, pady=(30,20), sticky="e")
    
    limgraficainf_e = tk.Entry(t)
    limgraficainf_e.grid(row=3, column=2, pady=(30,20), ipady=5, sticky="w")
    
    limgraficasup = customLabel("Superior:", 15, t)
    limgraficasup.grid(row=3, column=3, columnspan=2, pady=(30,20), sticky="e")
    
    limgraficasup_e = tk.Entry(t)
    limgraficasup_e.grid(row=3, column=5, pady=(30,20), ipady=5, sticky="w", padx=(0,75))
    
    graficarbtn = customButton("Graficar", 1, 20, lambda: mb.graph(poly_e.get(), float(limgraficainf_e.get()), float(limgraficasup_e.get())), t)
    graficarbtn.grid(row=4, columnspan=6)

    xl_lbl = customLabel("xl:", 15, t)
    xl_lbl.grid(row=5, column=0, columnspan=2, pady=(20,20), sticky="e")
    xl_e = tk.Entry(t)
    xl_e.grid(row=5, column=2, pady=(20,20), ipady=5, sticky="w")
    
    xu_lbl = customLabel("xu:", 15, t)
    xu_lbl.grid(row=5, column=3, columnspan=2, pady=(20,20), sticky="e")
    xu_e = tk.Entry(t)
    xu_e.grid(row=5, column=5, pady=(20,20), ipady=5, sticky="w")

    acc_error_lbl = customLabel("error:", 15, t)
    acc_error_lbl.grid(row=6, column=0, columnspan=3, pady=(0,20), sticky="e")
    acc_error_e = tk.Entry(t)
    acc_error_e.grid(row=6, column=3, columnspan=3, pady=(0,20), ipady=5, sticky="w")

    ans = tk.StringVar()
    ans_lbl = tk.Label(t, textvariable=ans, bg=mainbgcolor, fg=txtcolor, font=(def_font,15))
    ans_lbl.grid(row=8, columnspan=6, pady=(20,0))
	
    calculateparam = lambda: mb.biseccion(poly_e.get(), float(xl_e.get()), float(xu_e.get()), float(acc_error_e.get()))
    calcularbtn = customButton("Calcular", 1, 20, lambda: ans.set(f"La raíz es: {calculateparam()}") , t)
    calcularbtn.grid(row=7, columnspan=6)


def newtonraphsonwindow():
    t = tk.Toplevel()
    t.title("Metodo de Newton-Raphson")
    t.geometry("600x600")
    t["bg"] = mainbgcolor
    t.grid_columnconfigure((0, 1, 2, 3, 4, 5), weight=1)

    title = customLabel("Metodo de Newton-Raphson", 30, t)
    title.grid(row=0, columnspan=6, pady=(50,30))
    
    poly_lbl = customLabel("Función:", 15, t)
    poly_lbl.grid(row=1, column=0, columnspan=2, pady=(30,20))
    poly_e = tk.Entry(t)
    poly_e.grid(row=1, column=2, columnspan=4, pady=(30,20), padx=(0,30), ipady=5, sticky="we")

    limgrafica = customLabel("Limites de la grafica", 15, t)
    limgrafica.grid(row=2, columnspan=6)
    
    limgraficainf = customLabel("Inferior:", 15, t)
    limgraficainf.grid(row=3, column=0, columnspan=2, pady=(30,20), sticky="e")
    
    limgraficainf_e = tk.Entry(t)
    limgraficainf_e.grid(row=3, column=2, pady=(30,20), ipady=5, sticky="w")
    
    limgraficasup = customLabel("Superior:", 15, t)
    limgraficasup.grid(row=3, column=3, columnspan=2, pady=(30,20), sticky="e")
    
    limgraficasup_e = tk.Entry(t)
    limgraficasup_e.grid(row=3, column=5, pady=(30,20), ipady=5, sticky="w", padx=(0,75))
    
    graficarbtn = customButton("Graficar", 1, 20, lambda: mb.graph(poly_e.get(), float(limgraficainf_e.get()), float(limgraficasup_e.get())), t)
    graficarbtn.grid(row=4, columnspan=6)

    xi_lbl = customLabel("xi:", 15, t)
    xi_lbl.grid(row=5, column=0, columnspan=3, pady=(20,20), sticky="e")
    xi_e = tk.Entry(t)
    xi_e.grid(row=5, column=3, columnspan=3, pady=(20,20), ipady=5, sticky="w")

    acc_error_lbl = customLabel("error:", 15, t)
    acc_error_lbl.grid(row=6, column=0, columnspan=3, pady=(0,20), sticky="e")
    acc_error_e = tk.Entry(t)
    acc_error_e.grid(row=6, column=3, columnspan=3, pady=(0,20), ipady=5, sticky="w")

    ans = tk.StringVar()
    ans_lbl = tk.Label(t, textvariable=ans, bg=mainbgcolor, fg=txtcolor, font=(def_font,15))
    ans_lbl.grid(row=8, columnspan=6, pady=(20,0))
	
    calculateparam = lambda: mnr.newton_raphson(poly_e.get(), float(xi_e.get()), float(acc_error_e.get()))
    calcularbtn = customButton("Calcular", 1, 20, lambda: ans.set(f"La raíz es: {calculateparam()}") , t)
    calcularbtn.grid(row=7, columnspan=6)


def secantewindow():
    t = tk.Toplevel()
    t.title("Metodo de secante")
    t.geometry("600x600")
    t["bg"] = mainbgcolor
    t.grid_columnconfigure((0, 1, 2, 3, 4, 5), weight=1)

    title = customLabel("Metodo de secante", 30, t)
    title.grid(row=0, columnspan=6, pady=(50,30))
    
    poly_lbl = customLabel("Función:", 15, t)
    poly_lbl.grid(row=1, column=0, columnspan=2, pady=(30,20))
    poly_e = tk.Entry(t)
    poly_e.grid(row=1, column=2, columnspan=4, pady=(30,20), padx=(0,30), ipady=5, sticky="we")

    limgrafica = customLabel("Limites de la grafica", 15, t)
    limgrafica.grid(row=2, columnspan=6)
    
    limgraficainf = customLabel("Inferior:", 15, t)
    limgraficainf.grid(row=3, column=0, columnspan=2, pady=(30,20), sticky="e")
    
    limgraficainf_e = tk.Entry(t)
    limgraficainf_e.grid(row=3, column=2, pady=(30,20), ipady=5, sticky="w")
    
    limgraficasup = customLabel("Superior:", 15, t)
    limgraficasup.grid(row=3, column=3, columnspan=2, pady=(30,20), sticky="e")
    
    limgraficasup_e = tk.Entry(t)
    limgraficasup_e.grid(row=3, column=5, pady=(30,20), ipady=5, sticky="w", padx=(0,75))
    
    graficarbtn = customButton("Graficar", 1, 20, lambda: mb.graph(poly_e.get(), float(limgraficainf_e.get()), float(limgraficasup_e.get())), t)
    graficarbtn.grid(row=4, columnspan=6)

    xl_lbl = customLabel("x0:", 15, t)
    xl_lbl.grid(row=5, column=0, columnspan=2, pady=(20,20), sticky="e")
    xl_e = tk.Entry(t)
    xl_e.grid(row=5, column=2, pady=(20,20), ipady=5, sticky="w")
    
    xu_lbl = customLabel("x1:", 15, t)
    xu_lbl.grid(row=5, column=3, columnspan=2, pady=(20,20), sticky="e")
    xu_e = tk.Entry(t)
    xu_e.grid(row=5, column=5, pady=(20,20), ipady=5, sticky="w")

    acc_error_lbl = customLabel("error:", 15, t)
    acc_error_lbl.grid(row=6, column=0, columnspan=3, pady=(0,20), sticky="e")
    acc_error_e = tk.Entry(t)
    acc_error_e.grid(row=6, column=3, columnspan=3, pady=(0,20), ipady=5, sticky="w")

    ans = tk.StringVar()
    ans_lbl = tk.Label(t, textvariable=ans, bg=mainbgcolor, fg=txtcolor, font=(def_font,15))
    ans_lbl.grid(row=8, columnspan=6, pady=(20,0))
	
    calculateparam = lambda: ms.secante(poly_e.get(), float(xl_e.get()), float(xu_e.get()), float(acc_error_e.get()))
    calcularbtn = customButton("Calcular", 1, 20, lambda: ans.set(f"La raíz es: {calculateparam()}") , t)
    calcularbtn.grid(row=7, columnspan=6)


def bairstowwindow():
    t = tk.Toplevel()
    t.title("Metodo de bairstow")
    t.geometry("600x600")
    t["bg"] = mainbgcolor
    t.grid_columnconfigure((0, 1, 2, 3, 4, 5), weight=1)

    title = customLabel("Metodo de bairstow", 30, t)
    title.grid(row=0, columnspan=6, pady=(50,30))
    
    poly_lbl = customLabel("Función:", 15, t)
    poly_lbl.grid(row=1, column=0, columnspan=2, pady=(30,20))
    poly_e = tk.Entry(t)
    poly_e.grid(row=1, column=2, columnspan=4, pady=(30,20), padx=(0,30), ipady=5, sticky="we")

    limgrafica = customLabel("Limites de la grafica", 15, t)
    limgrafica.grid(row=2, columnspan=6)
    
    limgraficainf = customLabel("Inferior:", 15, t)
    limgraficainf.grid(row=3, column=0, columnspan=2, pady=(30,20), sticky="e")
    
    limgraficainf_e = tk.Entry(t)
    limgraficainf_e.grid(row=3, column=2, pady=(30,20), ipady=5, sticky="w")
    
    limgraficasup = customLabel("Superior:", 15, t)
    limgraficasup.grid(row=3, column=3, columnspan=2, pady=(30,20), sticky="e")
    
    limgraficasup_e = tk.Entry(t)
    limgraficasup_e.grid(row=3, column=5, pady=(30,20), ipady=5, sticky="w", padx=(0,75))
    
    graficarbtn = customButton("Graficar", 1, 20, lambda: mb.graph(poly_e.get(), float(limgraficainf_e.get()), float(limgraficasup_e.get())), t)
    graficarbtn.grid(row=4, columnspan=6)

    r_lbl = customLabel("r:", 15, t)
    r_lbl.grid(row=5, column=0, columnspan=2, pady=(20,20), sticky="e")
    r_e = tk.Entry(t)
    r_e.grid(row=5, column=2, pady=(20,20), ipady=5, sticky="w")
    
    s_lbl = customLabel("s:", 15, t)
    s_lbl.grid(row=5, column=3, columnspan=2, pady=(20,20), sticky="e")
    s_e = tk.Entry(t)
    s_e.grid(row=5, column=5, pady=(20,20), ipady=5, sticky="w")

    acc_error_lbl = customLabel("error:", 15, t)
    acc_error_lbl.grid(row=6, column=0, columnspan=3, pady=(0,20), sticky="e")
    acc_error_e = tk.Entry(t)
    acc_error_e.grid(row=6, column=3, columnspan=3, pady=(0,20), ipady=5, sticky="w")

    ans = tk.StringVar()
    ans_lbl = tk.Label(t, textvariable=ans, bg=mainbgcolor, fg=txtcolor, font=(def_font,15))
    ans_lbl.grid(row=8, columnspan=6, pady=(20,0))
	
    calculateparam = lambda: mbrs.bairstow(float(r_e.get()), float(s_e.get()), Poly(poly_e.get()).all_coeffs(), float(acc_error_e.get()), [])
    calcularbtn = customButton("Calcular", 1, 20, lambda: ans.set(f"Las raices son: {calculateparam()}") , t)
    calcularbtn.grid(row=7, columnspan=6)



root = tk.Tk()

mainbgcolor = "#e3e3e3"
txtcolor = "#151617"
btncolor = "#f1f1ef"
def_font = font.Font(family="Bahnschrift SemiCondensed")

rootwindow(root)
root.mainloop()
