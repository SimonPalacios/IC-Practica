import binascii

with open('pgp3.asc', 'rb') as file:
    line_hex = binascii.hexlify(file.readline())
    print(bytes.fromhex(line_hex.decode().lstrip('\\x')))
