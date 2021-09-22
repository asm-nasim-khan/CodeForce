number = int(input())
if_lucky = True
count = 0
while number>0:
    last_digit = number%10
    number = number//10
    if last_digit == 4 or last_digit == 7:
        count += 1
if count == 4 or count == 7:
    print('YES')
else:
    print('NO')