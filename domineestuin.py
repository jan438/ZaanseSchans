import os
import sys
import csv
import math
import unicodedata
from pathlib import Path
from datetime import datetime, date, timedelta
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.lib.units import inch, mm

if sys.platform[0] == 'l':
    path = "/home/jan/git/ZaanseSchans"
if sys.platform[0] == 'w':
    path = "C:/Users/janbo/OneDrive/Documents/GitHub/ZaanseSchans"
os.chdir(path)
my_canvas = canvas.Canvas("PDF/ZaanseSchans.pdf")
my_canvas.save()
key = input("Wait")
