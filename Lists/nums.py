nums = input().split(' ')

lst = []

for i in nums:
    i = int(i)
    i *= -1
    lst.append(i)

print(lst)


