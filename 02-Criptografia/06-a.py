# ic.catedras.linti.unlp.edu.ar 11006

from utilitis import get_conn, get_target
import hashlib
conn = get_conn('ic.catedras.linti.unlp.edu.ar', 11006)
target = get_target(conn, 'palabra:\n')
print(f"Palabra: {target}")
word_encode = hashlib.md5(target.encode()).hexdigest()
print(f"Encode: {word_encode}")
conn.send(word_encode)
print(conn.recvall())

# flag = IC{4gu4nt4_cr4ck3r!}