"""
Proyecto Python y Mysql:
- Abrir asistente
- Login o registro
- Si elegimos registro, creara un usuario en la bbdd
- Si elegimos login, identifica al usuario y nos preguntara
- Crear nota, mostrar notas, borrarlas.
"""

import acciones

def getAction():
    return input("\n¿Qué quieres hacer?\n 1. Registro \n 2. Login \n >")

hazEL = acciones.Acciones()
accion = getAction()

try:
    accion = int(accion)
except:
    print("Debes introducir un número")
    accion = getAction()

if accion not in [1,2]:
    print("Introduce un número correcto")
    accion = getAction()

if accion == 1:
    hazEL.registro()
    
elif accion == 2:
    hazEL.login()