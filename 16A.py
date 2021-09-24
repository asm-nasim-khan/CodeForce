matrix = input()
matrix_value = matrix.split(' ')
row = int(matrix_value[0])
col = int(matrix_value[1])
flag_colour = []
row_check = True
prev = ''
col_check = True
colours = []
for i in range(row):
    flag_colour.append(input())
for iter in range(len(flag_colour)):
    temp = flag_colour[iter][0]
    if temp != prev:
        prev = flag_colour[iter][0]
        for x in flag_colour[iter]:
            if x != temp:
                row_check = False
                break
    else:
        col_check = False
    if not row_check:
        break
if row_check and col_check:
    print('YES')
else:
    print('NO')