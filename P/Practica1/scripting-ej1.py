from pwn import *

con = remote("ic.catedras.linti.unlp.edu.ar", 10002)

con.readuntil("resolver esta cuenta:\n")

values = con.readline().decode().split()
print(f"type: {type(values)}, value: {values}")
op1 = int(values[0])
operador = values[1]
op2 = int(values[2])

result: int
match operador:
    case '+':
        result = op1 + op2
    case '-':
        result = op1 - op2
    case '*':
        result = op1 * op2
    case '/':
        result = op1 % op2

con.send((str(result) + "\n").encode())

print(con.readall())