s = input()
u = 0
l = 0
for items in s:
    if items.isupper():
        u += 1
    else:
        l += 1
if(u>l):
    print(s.upper())
else:
    print(s.lower())