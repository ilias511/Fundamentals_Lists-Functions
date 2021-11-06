my_dict = {}

command = input()

while command !='end':
    info = command.split(' : ')
    course = info[0]
    student = info[1]
    if course not in my_dict:
        my_dict[course] = [student]
    else:
        my_dict[course].append(student)
    command = input()

max_key = sorted(my_dict.items(), key=lambda x: (len(x[1])), reverse=True)

for course, student in max_key:
    print(f'{course}: {len(student)}')
    student = sorted(student, reverse=False)
    for el in student:
        print(f'-- {el}')