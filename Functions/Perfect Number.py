def perfect(num):
    equal = 0
    for i in range(1,num):
        if num % i == 0:
            equal+=i
    if equal == num:
        return 'We have a perfect number!'
    else:
        return "It's not so perfect."


num = int(input())

print(perfect(num))
