#!/usr/bin/python3
# enable debugging
import cgi
import cgitb
cgitb.enable()

print("Content-Type: text/html")
print()

from random import randrange, choice

tamanyo = randrange(200, 801, 100)
color = randrange(0, 361)
fuente = choice(["serif", "sans-serif", "monospace", "cursive"])

print("<!DOCTYPE html>")
print("<html lang=\"es\">")
print("  <head>")
print("    <meta charset=\"utf-8\" />")
print("    <title>Ficheros (1) - B-2</title>")
print("    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\" />")
print("  </head>")
print("")
print(f"  <body style=\"background-color: hsl({color}, 100%, 50%)\">")
print(f"    <p style=\"font-family: {fuente}; font-size: {tamanyo}%\">¡Hola, mundo!</p>")
print("  </body>")
print("</html>")
