size = int(input())
for i in range(size):
    tmp = input()
    if len(tmp)>10:
        print(tmp[0]+str(len(tmp)-2)+tmp[-1])
    else:
        print(tmp)