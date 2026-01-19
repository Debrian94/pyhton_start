# Proyecto del dia 2, en el cual vamos a calcular el 13% de los ingresos

print("*** Calcula tu comision ***")
nombre_vendedor = input("Ingresa tu nombre: ")
cantidad_venta = float(input("Ingresa el monto generado: "))
comision = cantidad_venta * 13 / 100
print(f"{nombre_vendedor}, te corresponde la cantidad de {comision} nuevos soles.")