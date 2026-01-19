# Tipo de datos
# variables
marca_de_carro = "Kia"
# Floats e Integers
num1 = 15
num2 = 15.5

# Parsear datos
dato1 = "30"
dato2 = int(dato1)
dato3 = str(dato2)

#Formatear Cadenas
color = "plata"
placa = 442
print(f"Mi auto es color {color} y la placa es {placa}")

# Division al piso -- esto me da el resultado menor = 3 lo redondea
num11 = 7
num22 = 2
num33 = num11 // num22

# modulo  -- el resultado va ser 1 ya que te da el numero que resta
num44 = num11 % num22

# elevacion de numero -- para elevar el numero basta **n
num55 = num22**2 # esto es al cuadrado
num66 = num22**3 # esto es al cubo

# raiz cuadrada de un numero - es hacerlo elevando **0.5
num77 = num22**0.5

# redondeo con metodo round
valor = 125.666666
valor_round = round(valor) # esto me da el valor 126
valor_round_decimales = round(valor,3) # esto me da el valor de 125.667
