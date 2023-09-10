from Crypto.Cipher import AES
import base64


key = b'CLAVE RE SECRETA'
msg = 'dV5t6M4m2AcjYWsxC9iO+YXlc0r0ClfwyTGtpuWdPh9fvH+8cejJWOHYq1qH7qA+Kj7Lci133Awj3rnoq42p532+fvbN64oZ8R/TlMkhw47nmIM5gPN+rt45985jeiIDbdpCu1ig09Rzepl4/kawM1AzFtoMzTvadmx11qSFp+UD81yiRz6HjaFLIIIIQnbzFrmcOIOGEQ6LBEYz2cTW6JPBs7MHpqDrcrzZoLcb7Ah2jQSIId+YZ90JmRt83yTe66a60kqL5SoW7/463Suyyp9xDhrgFu6YS3ScNDgOamADIcKmLUTxrvYooZIjL7s+thek3aBPrv/yB84YNUhX7MOxjiTiP02nBJ1E1dOA0ew75BeARB4cHKVfLMnPMkjSYyiQ2eTWqYd4cZ+14Z9joNVA1Uei8Pg4KITPfJYy3Mc='


print("--------")
decipher = AES.new(key, AES.MODE_ECB)

msg_dec = decipher.decrypt(base64.b64decode(msg.encode())) # Decipher akzeptiert und Binary kein Hex
print(msg_dec)
print(binascii.hexlify(msg_dec))