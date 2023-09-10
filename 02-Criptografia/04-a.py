from utilitis import get_conn, get_target, rot
import re
# ic.catedras.linti.unlp.edu.ar 11004

conn = get_conn('ic.catedras.linti.unlp.edu.ar', 11004)

rot_elemnt = re.findall(r'\d+', get_target(conn, 'ROT '))
rot_val = int(rot_elemnt[0])
print(f"ROT: {rot_val}")
target = conn.readline().decode().replace('\n', '')
print(f"Frase: {target}")
rotado = rot(target, rot_val)
print(f"Rotado: {rotado}")
conn.send(rotado.encode())
print(conn.recvall())

# IC{izi_rOt_ex4mpLe}