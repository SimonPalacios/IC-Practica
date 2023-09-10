import binascii
# 49 43 7b 77 68 65 6e 5f 75 5f 64 69 45 5f 79 6f 75 5f 61 72 65 5f 35 37 30 30 35 7d
def to_char(valor:str) -> str:
    return bytes.fromhex(valor).decode('ascii')
# Decodificar
cadena = '49 43 7b 77 68 65 6e 5f 75 5f 64 69 45 5f 79 6f 75 5f 61 72 65 5f 35 37 30 30 35 7d'
# Unir cada elemento del string spliteado por espacios al string. 
frase = ''.join([to_char(value) for value in cadena.split()])
print(frase)
# IC{when_u_diE_you_are_57005}