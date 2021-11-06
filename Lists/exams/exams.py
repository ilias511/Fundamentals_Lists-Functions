items = input().split('!')
command = input().split()
word = ' '.join(command)
while word!= 'Go Shopping!':
    material = command[0]
    thing = command[1]
    if material == 'Urgent':
        if thing in items:
            pass
        else:
            items.insert(0, thing)
    elif material == 'Unnecessary':
        if thing in items:
            items.remove(thing)
        else:
            pass
    elif material == 'Correct':
        if thing in items:
            new_item = command[2]
            items.insert(items.index(thing), new_item)
            items.remove(thing)
        else:
            pass
    elif material == 'Rearrange':
        if thing in items:
            items.remove(thing)
            items.insert(len(items), thing)

    command = input().split()
    word = ' '.join(command)

if len(items) == len(set(items)):
    result = ', '.join(items)
    print(result)
