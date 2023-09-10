from utilitis import get_conn, get_target
import hashlib
def find_inrockyou(word_hashed: str):

    with open('rockyou.txt', 'r') as file:
        for line in file:
            password = line.strip().encode()
            pass_hashed = hashlib.sha256(password).hexdigest()
                
            if word == pass_hashed:
                print(f"Find {password}")
                return password  

conn = get_conn('ic.catedras.linti.unlp.edu.ar', 11007)
word = get_target(conn, 'txt):\n')
password = find_inrockyou(word)
conn.send(password)
print(conn.recvall())