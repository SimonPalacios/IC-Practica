from math import sqrt


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception("No existe el inverso modular")  # SI NO EXISTE, DEVUELVE ERROR
    else:
        return x % m


def phi_n(p: int, q: int) -> int:
    return (p - 1) * (q - 1)

import math
from sympy.ntheory import factorint

def get_pq(n: int):
    print(factorint(n))
    exit()
    return p, q


def decode(e: int, chiper: int, d: int = None, p: int = None, q: int = None, n: int = None):
    if not n:
        n = p * q
    else:
        p, q = get_pq(n)
        print(p*q == n)
        print(p*q, '\n', n)
    if not d:
        d = modinv(e, phi_n(p, q))
    decode_m = pow(chiper, d, n)
    m_hex = hex(decode_m).lstrip('0x').rstrip("L")
    print(f"N: {n}")
    print(f"D: {d}")
    print(f"Mensaje: {decode_m}")
    print(f"Hex Mensaje: {m_hex}")

    m_decode = bytes.fromhex(m_hex)
    return m_decode
def ej12():
    p = 1411681044962247700471424630708374925648758544093881877
    q = 1025477764739116170232001755962926569489838949121232767
    e = 65537
    c = 244800329353906336350382253088680972646706962639783844335948234085022348400763256559770095538177770365047075

    print(decode(e, c, q=q, p=p, ))

def ej14():
    n = 1452449184624535635757449085988204487494222248509493899299759
    e = 65537
    C = 1280743944712857143060627969938538851911171950125979945026152
    p = 1153324775179431312178120797679
    q = 1259358348907893108175391571521
    print(decode(e, C, p=p, q=q))
    # b'IC{factordb_ftw}'

from pwn import remote
def ej13():
    with remote('ic.catedras.linti.unlp.edu.ar', 11012) as conn:
        conn.recvuntil('texto:\n')
        p = int(conn.readline().decode().split()[1])
        q = int(conn.readline().decode().split()[1])
        e = int(conn.readline().decode().split()[1])
        c = int(conn.readline().decode().split()[1])
        mssg = decode(e, c, q=q, p=p)
        print(mssg)
        conn.send(mssg)
        print(conn.recvall())
        # b'Correcto! la flag es IC{rsa_is_eeeeeeasy}'
# flag = IC{sabiendo_P_y_Q_es_muy_facil}


ej13()
