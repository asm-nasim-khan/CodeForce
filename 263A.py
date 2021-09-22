dataSet = [input("") for x in range(5)]
arr = []
for items in dataSet:
    temp = items.split()
    subarray = [int(x) for x in temp]
    arr.append(subarray)

for i in range(5):
    for j in range(5):
        if arr[i][j] == 1:
            move = abs(3-(i+1))+abs(3-(j+1))
            print(move)
            break