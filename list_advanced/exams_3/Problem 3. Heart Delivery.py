hearts = input().split('@')
points = [int(p) for p in hearts]
command = input().split(' ')
index_pos = 0
houses_checked = 0

while command[0]!='Love!':
    if command[0]=='Jump':
        index_pos += int(command[1])
        if index_pos>len(points)-1:
            index_pos = 0
        if points[index_pos] == 0:
            print(f"Place {index_pos} already had Valentine's day")
            command = input().split(' ')
            continue
        else:
            points[index_pos] -= 2
        if points[index_pos] == 0:
            print(f"Place {index_pos} has Valentine's day.")
            houses_checked +=1

    command = input().split(' ')

print(f"Cupid's last position was {index_pos}.")
if houses_checked == points:
    print('Mission was successful.')
else:
    print(f"Cupid has failed {len(points)-houses_checked} places.")