# 05110006_08130308020418_0011050001041908021418
import string
phrase = '05110006_08130308020418_0011050001041908021418'
splited_word = phrase.split('_')
n = 2
abcd = string.ascii_uppercase
finall = ''
for word in splited_word:
    pala = ''
    for letter in word:
        pala += abcd[int(letter)]
    print(pala)
    finall += pala + ' '
print(finall)

#    for i in range(0, len(word), n):
#        char = word[i:i+n]
#        resul = abcd[int(char, 16)]
#        pala += resul
#        print(f"Char hex: {char} Char: {int(char, 16)}")