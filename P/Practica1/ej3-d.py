import string
from unidecode import unidecode


# Vigere. Para descrifar se toma la letra n del texto cifrado y de la clave y se restan.
# Cada letra tiene un valor numerico dentro del alfabeto.
# afabeto.index(chiper[i]) - afabeto.index(clave[i])
# El numero resultante es el desplazamiento dentro del alfabeto.

def get_abcd(clave: str) -> str:
    result = ''
    for char in clave + string.ascii_lowercase:
        if char not in result and char != ' ':
            result += char
    return result


chiper = unidecode("pp epnwfus dvjipèym jx ln dtjcefv jfxrhw rq hkmmwjetfd wpvkla ij teznfxgymx t ceuced hgs "
                        "knkielb féwcy ntwdaoos pwvva hfiekghvgz csf kacwe, wpctiif kejyd hg cqljeèrf,byp wg baf hfqw "
                        "poexl. mq hzfslhz hg cqljeèvm rv yp jqkwrdp oi dyuaqyztmóv flqrsmutcibwjlfévpkt. rlc jvhr! "
                        "nh nqfx et tg{g1k3plz3_wzc3w}. arjyí czí!").split(' ')
clave = get_abcd("le chiffre indechiffrable")
print(clave)
abcd = clave * (int(len(chiper) / len(clave)) + 1)
alfabeto = string.ascii_lowercase
mensaje_descifrado = ""
for j, word in enumerate(chiper):
    for i, letter in enumerate(chiper):
        if letter.isalpha():

            # Obtengo el indice del alfabeto
            pos_chiper = alfabeto.index(letter)
            # Obtengo el indice de la letra que es de la misma posicion del chiper en la key.
            pos_key = alfabeto.index(abcd[i])
            # Obtengo el indice de la letra en clave
            pos_clave = pos_chiper - pos_key
            real_pos = pos_clave if pos_clave > -1 else pos_clave + 26
            print(
                f"real_pos {real_pos} pos_clave {pos_clave} pos_chiper: {(pos_chiper, letter)} pos_key: {(pos_key, abcd[i])} ")
            # Obtengo la letra del alfabeto
            mensaje_descifrado += alfabeto[real_pos]
        else:
            # Mantener caracteres no alfabéticos sin cambios
            mensaje_descifrado += chiper[i]

print(mensaje_descifrado)
