n = int(input())
empty_chairs = 0
chairs = []
is_empty = False
for i in range(1,n+1):
    chairs = []
    visitors = 0
    info = input().split(' ')
    if 'X' in info[0]:
        chairs.append(info[0])
    visitors+=int(info[1])
    new = [x for x in chairs[0]]
    if len(new)==visitors:
        pass
    elif len(new)>visitors:
        empty_chairs+= len(new) - visitors
    elif len(new)<visitors:
        needed_chairs = visitors - len(new)
        is_empty = True
        print(f'{needed_chairs} more chairs needed in room {i}')

if not is_empty:
    print(f'Game On, {empty_chairs} free chairs left')