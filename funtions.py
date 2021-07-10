#funciones usadas hasta el momento
print()
dir()
type()

#creacion de una funcion
def hello(): # esa palabra clave def hace referencia a que sera una funcion lo que se hara a continuacion.
    print("hola mundo")
hello() #se debe llamar a la funcion para que recien empieze a funcionar
#funcion de tipo lambda
add = lambda numero1, numero2: numero1 + numero2

print(add(10, 40))

