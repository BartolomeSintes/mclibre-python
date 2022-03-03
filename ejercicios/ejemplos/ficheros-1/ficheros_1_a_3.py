#!/usr/bin/python3
# enable debugging
import cgi
import cgitb
cgitb.enable()

print("Content-Type: text/html")
print()

print("<!DOCTYPE html>")
print("<html lang=\"es\">")
print("  <head>")
print("    <meta charset=\"utf-8\" />")
print("    <title>Ficheros (1) - A-3</title>")
print("    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\" />")
print("  </head>")
print()
print("  <body>")
print("    <p>¡Hola, mundo!</p>")
print("  </body>")
print("</html>")
