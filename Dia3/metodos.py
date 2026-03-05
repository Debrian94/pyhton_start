from difflib import restore

from Dia3.clase import resultado

texto = "Esto es python"

## Metodo Upper
resultado = texto.upper() # --> ESTO ES PYTHON

## Metodo Lower
resultado = texto.lower() # --> esto es python

## Metodo split - este metodo separa en lista las palabrad de una frase
resultado = texto.split() # --> ['Esto','es','python']
### este metodo separa por espacios pero tambien puede separar por lo que le pongas
resultado = texto.split('t') # --> ['Es', 'o es py', 'hon']


## Metodo join
a = "edson"
b = "es"
c = "genial"
respuesta = " ".join([a,b,c]) # --> edson es genial
respuesta = "-".join([a,b,c]) # --> edson-es-genial


## Metodo find  * busca igual que index
texto_find = "esto es un texto"
res = texto_find.find("s") #--> 1
res = texto_find.find("z") #--> -1 si no encuentra la letra te da -1

## Metodo replace * este metodo reemplaza un texto
texto_replace = "Esta es el texto de edson"
respu = texto_replace.replace("edson","kevin")
print(respu) #--> Esta es el texto de kevin

## Propiedades de String
# ** in ** para buscar palabras en texto devuelve True o False
poema = """ Esto es un poema de amor"""
print("amor" in poema) # --> True
print("amor" not in poema) # --> False

# ** len ** para contar la cantidad de strings
saludo = "Hola Mundo"
ress = len(saludo) # --> 10
