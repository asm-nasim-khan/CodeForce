dat = input()
result = ''
i = 0
while (i<len(dat)):
    if dat[i] == '.':
        result += '0'
        i +=1
    elif dat[i] == '-':
        if dat[i+1] == '.':
            result += '1'
        else:
            result += '2'
        i += 2
print(result)