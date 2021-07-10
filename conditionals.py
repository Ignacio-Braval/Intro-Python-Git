#un signo igual "=" es para asignar un valor y este simbolo "==" es para comparar.
x = 20
if x < 30: #condicionante if, para comparar valores, se deben colocar los doble puntos
    print("x is less than 30")
else:
    print("x is greater than 30")

#se puede hacer con string tambien

colores = "rojo" #condicionantes simples
if colores == "rojo":
    print("the color is red")
elif colores == "azul":
    print("the color is blue")
else:
    print("the color is not red")

   
nombre = "ignacio" #condicionantes con doble if.
apellido = "bravo"

if nombre == "ignacio":
    if apellido == "bravo":
        print("tu eres ignacio bravo")
    else:
        print("tu no eres la persona correcta")

x = 1
z = 15
if x>1 and z < 15:
    print("los numeros estan dentro del rango")
else:
    print("los numeros estan fuera del rango")