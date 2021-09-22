arr = input()
arr2 = input()
for i in range(len(arr)):
    if int(arr[i]) == int(arr2[i]):
        print(0,end='')
    else:
        print(1,end='')