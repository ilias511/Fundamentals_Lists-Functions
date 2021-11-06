old_books = input().split(' | ')

command = input().split()

while command[0]!='Stop!':
    if command[0]=='Join':
        if command[1] not in old_books:
            old_books.append(command[1])
    elif command[0]=='Drop':
        if command[1] in old_books:
            old_books.remove(command[1])
    elif command[0]=='Replace':
        old = command[1]
        new = command[2]
        if old in old_books and new not in old_books:
            old_books.insert(old_books.index(old),new)
            old_books.remove(old)
    command = input().split()

print(' '.join(old_books))