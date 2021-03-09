#!/usr/bin/python3.9

linkP = input("Introduce URL del Phising aquí (sin http o https), ej(64738n34b4.ngrok.io): ")
str(linkP)

linkW = input("Introduce el dominio para ocultar el Phishing URL (con http o https), (ej: https://google.com): ")
str(linkW)

print("Escribe palabras para engañar a la víctima, (ej: gana-dinero, conseguir-aprobados-sin-estudiar): ")
linkE = input("¡CUIDADO! No uses espacio entre palabras, usa [-]: ")
str(linkE)

print("Este es el nuevo enlace generado para su víctima:")
print(linkW+"-"+linkE+"@"+linkP)

