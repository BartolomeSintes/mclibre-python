#!/usr/bin/python3
# enable debugging
import cgi
import cgitb
cgitb.enable()

print("Content-Type: text/html")
print()

print("<html>")
print("  <head>")
print("    <meta charset=\"utf-8\" />")
print("  </head>")
print()
print("  <body>")
print("    <p>¡Hola, mundo!</p>")
print("  </body>")
print("</html>")
