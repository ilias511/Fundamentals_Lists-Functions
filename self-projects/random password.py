import random

password = ''

n = int(input())

for i in range(n):
    password+=chr(random.randint(40,100))
    password+=chr(random.randint(99,140))
    password+=str(random.randint(1,99))


print(password)

