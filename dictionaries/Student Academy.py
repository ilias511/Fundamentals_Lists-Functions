my_dict = {}

rows = int(input())

for i in range(1,rows+1):
    name = input()
    grade = float(input())
    if name not in my_dict:
        my_dict[name] = [grade]
    else:
        my_dict[name].append(grade)

valid_student = sorted(my_dict.items(),key=lambda x:sum(x[1])/len(x[1]),reverse=True)

for person,value in valid_student:
    if (sum(value) / len(value))>=4.50:
        print(f'{person} -> {(sum(value)/len(value)):.2f}')