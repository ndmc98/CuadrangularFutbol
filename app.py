from flask import Flask, render_template, redirect, url_for, request, flash, escape
from logic.torneo import *

import os
import time

app = Flask(__name__)

app.secret_key = os.urandom(24)

campeonato = Torneo()

maxEquipos = 4
minEquipos = 2

@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        try:
            campeonato.equipos = []
            campeonato.partidos = []
            campeonato.rivales = []

            n = int(escape(request.form["teams"]))

            if n > maxEquipos:
                flash("Error:"+ str(maxEquipos) +" es la cantidad máxima de equipos que se pueden registrar.")
            elif n < minEquipos:
                flash("Error: el número mínimo de equipos debe ser"+str(minEquipos))
            else:
                return render_template("registroEquipos.html",n=n)
        except Exception as e:
            print(e)
            flash("Se ha producido un fallo. Inserte información valida. "+str(e))
        
    return render_template("form.html")

@app.route("/registroJuegos/", methods=["GET", "POST"])
def registroJuegos():
    if request.method == "POST":
        try:
            equipos = []
            i=1

            for regs in request.form:
                equipos.append(str(escape(request.form["team"+str(i)])))
                i += 1
            
            for j in equipos:
                campeonato.registroEquipo(j)

            campeonato.encuentros()

            juegos = []

            for pareja in campeonato.rivales:
                par = (pareja[0].nombre,pareja[1].nombre)
                juegos.append(par)

            return render_template("registroJuegos.html",matches=juegos)

        except Exception as e:
            print(e)
            flash("Error: Se ha producido un fallo. Inserte información valida. "+str(e))

    return render_template("registroEquipos.html")

@app.route("/tablaPosiciones/", methods=["GET", "POST"])
def tablaPosiciones():
    if request.method == "POST":
        try:
            for i in range(len(campeonato.rivales)):
                campeonato.crearPartido(campeonato.rivales[i],int(request.form["goalsT1M"+str(i)]),int(request.form["goalsT2M"+str(i)]))
            
            data = []
            for equ in campeonato.equipos:
                cabecera = vars(equ)
                d = []
                for item in cabecera:
                    d.append(cabecera[item])
                data.append(d)

            return render_template("tablaPosiciones.html",head = cabecera,data = data)

        except Exception as e:
            print(e)
            flash("Error: Se ha producido un fallo. Inserte información valida. "+str(e))
    
    return render_template("form.html")        

if __name__ == "__main__":
    app.run()