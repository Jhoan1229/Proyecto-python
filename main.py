"""
Proyecto Python y Mysql:
- Abrir asistente
- Login o registro
- Si elegimos registro, creara un usuario en la bbdd
- Si elegimos login, identifica al usuario y nos preguntara
- Crear nota, mostrar notas, borrarlas.
"""

import acciones

print("""
Acciones disponibles:
    - registro
    - login      
""")

hazEL = acciones.Acciones()
accion = input("Que quieres hacer?: ")

if accion == "registro":
    hazEL.registro()
    
elif accion == "login":
    hazEL.login()