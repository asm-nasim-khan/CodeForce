fh = open('input.txt','r')
user = fh.read()
data = user.split('\n')
size = int(data[0])
count = 0
for item in range(1,size+1):
    temp = data[item]
    box  = temp.split('X')
    if '++' in box:
        count +=1
    else:
        count -=1
print(count)