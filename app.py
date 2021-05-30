from flask import Flask, render_template, redirect, url_for, request, flash, escape
from logic.torneo import *

import os
import time

app = Flask(__name__)

app.secret_key = os.urandom(24)

campeonato = Torneo()
