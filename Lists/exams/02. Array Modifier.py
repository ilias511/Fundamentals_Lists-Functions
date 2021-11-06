integers = [int(i) for i in input().split()]

command = input().split()

while not 'end' in command:
    if 'swap' in command:
        index1 = int(command[1])
        index2 = int(command[2])

        integers[index1], integers[index2] = integers[index2], integers[index1]
    elif 'multiply' in command:
        index1 = int(command[1])
        index2 = int(command[2])
        integers[index1] = integers[index1] * integers[index2]

    elif 'decrease' in command:
        decreased = []
        for d in integers:
            d = int(d) - 1
            decreased.append(d)

        integers.clear()
        for l in decreased:
            integers.append(l)
    command = input().split()

print(', '.join([str(value) for value in integers]))
