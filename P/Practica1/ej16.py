from math import log

from pwn import remote


def get_pqpupri():
    with remote('ic.catedras.linti.unlp.edu.ar', 11018) as conn:
        conn.recvuntil("Hellman:\n")
        p = int(conn.recvline().decode().split()[1])
        q = conn.recvline().decode()
        pu_alice = int(conn.recvline().decode().split()[1])
        pr_bob = int(conn.recvline().decode().split()[1])
        k = pow(pu_alice, pr_bob, p)
        print(f"P: {p} \n Q: {q} \n Public_alice: {pu_alice} \n Private Bob: {pr_bob} \n Key: {k}")
        conn.send(str(k).encode())
        print(conn.recvall())

get_pqpupri()

