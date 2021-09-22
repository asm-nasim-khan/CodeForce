data1 = input()
data2 = input()
value1 = data1.split()
value2 = data2.split()
k = int(value1[1])
key = int(value2[k-1])
counter = 0
for item in value2:
    if int(item)>= key and int(item)>0:
        counter += 1
print(counter)