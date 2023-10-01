import string
frase = '05110006_08130308020418_0011050001041908021418'
abdc = string.ascii_uppercase
resul = ''
for word in frase.split('_'):
    for i in range(0, len(word), 2):
        val = word[i:i+2]
        resul += abdc[int(val)]
    print(resul)