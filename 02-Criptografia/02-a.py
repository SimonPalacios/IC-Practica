from utilitis import get_conn, get_target
import base64
# nc ic.catedras.linti.unlp.edu.ar 11002

conn = get_conn('ic.catedras.linti.unlp.edu.ar', 11002)

target = get_target(conn, 'palabra:\n')
print(f"palabra: {target.encode()}")
response = base64.b64encode(target.encode())
print(f"response: {response}")

conn.send(response)
print(conn.recvall())

# IC{EaSy_enc0d1ng_exaMple}