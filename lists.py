# las listas se crean con corchetes 
demo_list = {1, "hola", 50, 10.5, "mundo"} #una forma de crear una lista
colors = {"rojo", "azul", "amarillo"}
numbers_list = list((1, 2, 3, 4)) #se deben agregar dos parentesis mas para convertirlo en tupla, asi soportar mas datos. las lstas solo soportan una.

rangos = list(range(1, 10)) #range genera un rango con los datos que le damos, y a la vez los guardara en una lista y a su vez estos datos estaran dentro de la variable "rangos"

print("hola" in demo_list)# buscara si el dato que pedimos esta dentro de esa lista.

colors.append("violeta") #el metodo append agrega un nuevo elemento a la lista colors.

colors.insert(1, "rosa") #a  la lista colors le estoy insertando un nuevo dato en la posicion n°1.

colors.insert(len(colors), "cafe") #a la lista colors le estoy agregando un nuevo dato al final de esta misma.

colors.pop() #quita el ultimo elemento de la lista.

colors.remove("azul") #elimina un elemtento en especifico dentro de la lista.

colors.sort() #muestra los elementos ordenados alfabeticamente.

colors.sort(reverse=True) #los mostrara alfabeticamente pero al reves.

