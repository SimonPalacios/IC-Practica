from pwn import *
import string
from typing import List

def decrypte_b64val(word: List[str], separador: List[str],
                    alf=string.ascii_uppercase) -> str:
    try: 
        return ''.join([alf[int(char)-1] for char in word ])
    except ValueError as e:
        divisor_actual = separador[0] if len(separador) == 1 else separador.pop()
        return ''.join(decrypte_b64val(char.split(divisor_actual), separador)+' ' for char in word)

def transpocion_col(columns: int, rows: int, message: str) -> str:
    return ''.join([message[col+carry]
                    for carry in range(0, rows)
                    for col in range(0, len(message), rows)
                     ])

def rot(message:str, rot: int):
    alfabeto = {'upper': (string.ascii_uppercase+string.ascii_uppercase, 65),
                'lower': (string.ascii_lowercase+string.ascii_lowercase, 97) }
    abcd2, diff = alfabeto['lower'] if message.islower() else alfabeto['upper']

    def get_char(letter: str) -> str:
        ascii_val = ord(letter)-diff + rot    
        return abcd2[ascii_val] if letter not in ('{', '}', ' ') else letter

    return ''.join([get_char(char) for char in message])



def get_target(conn, after_row: str) -> str:
    conn.recvuntil(after_row.encode())
    return conn.readline().decode().replace('\n', '')

def get_conn(url: str, port: int):
    return remote(url, port)    