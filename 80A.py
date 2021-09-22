value = input()
user_input = value.split(' ')
first_prime_number = int(user_input[0])
checking_number = int(user_input[1])
prime_list=[]
numCount = 0
for item in range(first_prime_number+1,checking_number+1):
    count = 0
    for i in range(2,item):
        if item%i == 0:
            count += 1
    if count == 0:
        prime_list.append(item)
        numCount += 1
if numCount == 1 and checking_number == prime_list[0]:
    print('YES')
else:
    print('NO')