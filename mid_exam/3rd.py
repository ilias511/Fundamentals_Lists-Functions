cards = input().split(':')

command = input().split(' ')
new_deck = []
while command[0]!='Ready':
    if command[0] == 'Add':
        if command[1] not in cards:
            print('Card not found.')
        else:
            new_deck.append(command[1])
    elif command[0] == "Insert":
        if 0 <= int(command[2]) < len(new_deck) and command[1] in cards:
            new_deck.insert(int(command[2]), command[1])
        else:
            print("Error!")
    elif command[0] == 'Remove':
        if command[1] in new_deck:
            new_deck.remove(command[1])
        else:
            print('Card not found.')
    elif command[0] == 'Swap':
        first = new_deck.index(command[1])
        sec = new_deck.index(command[2])
        new_deck[first], new_deck[sec] = new_deck[sec], new_deck[first]
    elif command[0] == 'Shuffle':
        new_deck.reverse()

    command = input().split()

print(' '.join(new_deck))


