from pwn import *


def get_count(corte: str) -> list:
    con.recvuntil(corte)
    return con.readline().decode().split()


def make_count(op1, operador, op2) -> int:
    op1 = int(op1)
    op2 = int(op2)
    match operador:
        case '+':
            return op1 + op2
        case '-':
            return op1 - op2
        case '*':
            return op1 * op2
        case '/':
            return op1 % op2


with remote("ic.catedras.linti.unlp.edu.ar", 10002) as con:
    i: int = 1
    while True:
        try:
            values = get_count('!:\n')
            print(f"{i}: {values}")
            result = make_count(*values)
            con.send((str(result) + "\n").encode())
            i += 1
        except Exception as e:
            print(e)
            break
    print(con.recvall())
