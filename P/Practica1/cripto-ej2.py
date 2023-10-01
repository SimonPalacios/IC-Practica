from pwn import *
import base64


def get_target(after):
    conn.recvuntil(after)
    return conn.readline()


with remote('ic.catedras.linti.unlp.edu.ar', 11002) as conn:
    target = get_target('palabra:\n')
    response = base64.b64encode(target)
    conn.send(response)
    print(conn.recvall())
