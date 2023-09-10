

# Decodificar
cadena = '73 67 123 99 97 108 101 110 116 97 110 100 111 95 109 111 116 111 114 101 115 125'
# Unir cada elemento del string spliteado por espacios al string. 
frase = ''.join([chr(int(value)) for value in cadena.split()])
print(frase)