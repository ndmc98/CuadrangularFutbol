from models.partido import *
from models.equipo import *

import itertools

class torneo:

    def __init__(self):
        self.equipos = []
        self.rivales = []
        self.partidos = []
        self.victoria = 3
        self.empate = 1
    
    def registroEquipo(self, nombre):
        self.equipos.append(Equipo(nombre))

    def encuentros(self):
        self.encuentros = list(itertools.combinations(self.equipos, 2))

    

