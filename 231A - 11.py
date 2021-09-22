size = int(input())
count = 0
for i in range(size):
    tmp = input()
    valuel = tmp.split()
    sum = 0
    for item in valuel:
        sum+=int(item)
    if sum>1:
        count+=1
print(count)