nums = input().split(', ')

for i in nums:
    number = int(i)
    if number == 0:
        nums.remove(i)
        nums.insert(len(nums),i)

int_num = [int(x) for x in nums ]
print(int_num)