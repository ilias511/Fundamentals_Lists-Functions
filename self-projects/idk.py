import random
import string
result = []
num = int(input("enter the lenght of password: "))
for i in range(num):

    result.append(random.randint(0,9))
    result.append(random.randint(90,110))


print(result)