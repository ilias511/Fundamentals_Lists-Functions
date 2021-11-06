items = input().split(', ')

command = input().split(' - ')

while 'Craft!' not in command:
    if command[0] == 'Collect':
        if command[1] in items:
            pass
        else:
            items.append(command[1])

    elif command[0] == 'Drop':
        if command[1] in items:
            items.remove(command[1])

    elif command[0] == 'Combine Items':
        item = command[1].split(':')
        if item[0] in items:
            items.insert(items.index(item[0])+1,item[1])

    elif command[0] == 'Renew':
        if command[1] in items:
            items.remove(command[1])
            items.append(command[1])
    command = input().split(' - ')

print(', '.join(items))