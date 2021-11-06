num = int(input())

for i in range(1,num+1):
    sum_of_digits = 0
    i_str = str(i)
    for j in i_str:
        i_int= int(j)
        sum_of_digits+=i_int
    if sum_of_digits == 5 or sum_of_digits ==7 or sum_of_digits == 11:
        print(f'{i} -> True')
    else:
        print(f'{i} -> False')

