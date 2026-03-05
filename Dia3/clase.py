#metodo index()
texto = "esta es una prueba"
resultado = texto.index("a",5,11)#dara el indice 10
"""Este codigo busca la letra a- desde el indice 5 al indice 11"""
#metodo rindex() - hace la busqueda de derecha a izquierda

#slicing
texto_slicing = "ABCDEFGHIJKLM"
resultado_slicing = texto_slicing[2:5] #--> CDE
resultado_slicing = texto_slicing[2:] #--> CDEFGHIJKLM
resultado_slicing = texto_slicing[:5] #--> ABCDE
resultado_slicing = texto_slicing[2:5:1] #--> ABCDE tercer parametro es los saltos
resultado_slicing = texto_slicing[::-1] #--> MLKJIHGFEDCBA te da el texto al revez


