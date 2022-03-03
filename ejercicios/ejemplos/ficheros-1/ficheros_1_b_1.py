#!/usr/bin/python3
# enable debugging
import cgi
import cgitb
cgitb.enable()

print("Content-Type: text/html")
print()

from random import randrange

color = randrange(0, 361)

print("<!DOCTYPE html>")
print("<html lang=\"es\">")
print("  <head>")
print("    <meta charset=\"utf-8\" />")
print("    <title>Ficheros (1) - B-1</title>")
print("    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\" />")
print("  </head>")
print()
print(f"  <body style=\"background-color: hsl({color}, 100%, 50%)\">")
print("    <p>¡Hola, mundo!</p>")
print("  </body>")
print("</html>")
