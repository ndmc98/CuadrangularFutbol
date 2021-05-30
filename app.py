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
                return render_template("registerTeams.html",n=n)
        except Exception as e:
            print(e)
            flash("Se ha producido un fallo. Inserte información valida. "+str(e))
        
    return render_template("form.html")

@app.route("/registerMatches/", methods=["GET", "POST"])
def registroJuegos():
    print('algo')