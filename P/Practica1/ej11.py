# nc ic.catedras.linti.unlp.edu.ar 11015
from operator import xor

from pwn import remote


def get_things():
    con = remote('ic.catedras.linti.unlp.edu.ar', 11015)
    con.recvuntil('es:\n')
    pista = con.readline().decode().replace('\n', '')
    chiper = con.readline().decode().replace('\n', '')
    print(f"Pista: {pista} \n Chiper: {chiper}")
    return pista, chiper


def get_xor(a: list, b: list) -> list:
    # calculo si debo repetir la clave:
    if (len(b) < len(a)):
        b = b * (int(len(a)/len(b))+1)
        b = b[:len(a)]
    return [hex(int(a[i], 16) ^ int(b[i], 16))  for i in range(0, len(a))]


# pista, chiper = get_things()
# a xor b = c // c xor a = b
pista = 'corazon'
fisrt_chiper = '010a3630180a2a'
chiper = '010a3630180a2a71160c2e3410046439030928301045273e010c2a3042022123030b2d3e'
# Preparo el string
pista_hex = [hex(ord(char)).lstrip('0x') for char in pista]
chiper_list = [fisrt_chiper[i:i + 2] for i in range(0, len(fisrt_chiper) - 1, 2)]
# c xor a = b
clave = get_xor(chiper_list, pista_hex)
# a xor b = c
cifrado = get_xor(pista_hex, clave)
print(f"Input: {pista}")
print(f"Clave: {chiper_list}")
print(f"Cifrado: {cifrado}")
# resultado = xor(c, pista)
# print(resultado)
