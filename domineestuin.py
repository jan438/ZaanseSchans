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
from svglib.svglib import svg2rlg, load_svg_file, SvgRenderer
from reportlab.graphics import renderPDF

def scaleSVG(svgfile, scaling_factor):
    svg_root = load_svg_file(svgfile)
    svgRenderer = SvgRenderer(svgfile)
    drawing = svgRenderer.render(svg_root)
    scaling_x = scaling_factor
    scaling_y = scaling_factor
    drawing.width = drawing.minWidth() * scaling_x
    drawing.height = drawing.height * scaling_y
    drawing.scale(scaling_x, scaling_y)
    return drawing

if sys.platform[0] == 'l':
    path = "/home/jan/git/ZaanseSchans"
if sys.platform[0] == 'w':
    path = "C:/Users/janbo/OneDrive/Documents/GitHub/ZaanseSchans"
os.chdir(path)
my_canvas = canvas.Canvas("PDF/ZaanseSchans.pdf")
renderPDF.draw(scaleSVG("SVG/wrk763.svg", 0.3), my_canvas, 100.0, 500.0)
renderPDF.draw(scaleSVG("SVG/AHWinkelZS.svg", 0.3), my_canvas, 300.0, 300.0)
renderPDF.draw(scaleSVG("SVG/wrk763_1.svg", 0.3), my_canvas, 100.0, 300.0)
my_canvas.save()
key = input("Wait")
