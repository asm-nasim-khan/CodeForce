word1 = input()
word2 = input()
count=[0,0]
for i in range(len(word1)):
    if word1[i].upper() != word2[i].upper():
        count[0] = ord(word1[i].upper())
        count[1] = ord(word2[i].upper())
        break
if count[0]>count[1]:
    print('1')
elif count[0]<count[1]:
    print('-1')
elif count[0]==count[1]:
    print('0')