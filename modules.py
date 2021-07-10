# modulos que podemos crear nosotros mismos
# modulos que podemos descargar de internet
# modulos que podemos utilizar de las mismas bibliotecas de python

import datetime

print(datetime.date.today())
# tambien se pueden importar modulos internamente, Isuma

import Isuma  # se importa primero el archivo donde estan las funciones (Isuma), y luego se llaman a las funciones

Isuma.sumar(5, 6)

Isuma.restar(8, 5)
