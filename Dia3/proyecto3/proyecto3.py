texto = input("Ingresa el texto: ")
print("Ahora ingresaras 3 letras a eleccion:")
l1 = input("Ingresa primera letra: ")
l2 = input("Ingresa segunda letra: ")
l3 = input("Ingresa tercera letra: ")

### 1 .- Cuantas veces apare cada letra
### 2 .- Cuantas palabras hay en el texto
### 3 .- Cual es la primera letra y la ultima
### 4 .- Hacer el texto en orden inverso
### 5 .- Aparece la palabra python en el texto
textoMin = texto.lower()
cantL1 = textoMin.count(l1)
cantL2 = textoMin.count(l2)
cantL3 = textoMin.count(l3)
print("------------------------------------")
print("ANALIZADOR DE TEXTOS")
print("------------------------------------")

print(f"La letra {l1} aparece {cantL1} veces.")
print(f"La letra {l2} aparece {cantL2} veces.")
print(f"La letra {l3} aparece {cantL3} veces.")
print("------------------------------------")
listTexto = textoMin.split()
cantPalabras = len(listTexto)
print(f"Hay {cantPalabras} palabras en el texto.")
print("------------------------------------")
print(f"La primera letra del texto es {texto[0]}")
print(f"La ultima letra del texto es {texto[-1]}")
print("------------------------------------")
print("El texto invertido seria ...")
textoInvertido =" ".join(listTexto[::-1])
print(textoInvertido)
print("------------------------------------")
verificacion = "python" in textoMin
dicPython = {True:"si",False:"no"}
print(f"La palabra python {dicPython[verificacion]} está en el texto.")
