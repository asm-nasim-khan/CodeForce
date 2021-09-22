size = int(input())
count = 0
for item in range(size):
    temp = input()
    box  = temp.split('X')
    if '++' in box:
        count +=1
    else:
        count -=1
print(count)