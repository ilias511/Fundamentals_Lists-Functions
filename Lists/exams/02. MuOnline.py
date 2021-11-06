health = 100
bitcoins = 0
best_room = 0
rooms = input().split('|')
does_the_hero_died = False

for battle in rooms:
    best_room+=1
    parts = battle.split(' ')
    if parts[0] == 'potion':
        if (health + int(parts[1]))>100:
            total_healed = 100 - health
            health+=total_healed
            print(f'You healed for {total_healed} hp.')
        else:
            health+=int(parts[1])
            print(f'You healed for {int(parts[1])} hp.')
        print(f'Current health: {health} hp.')
    elif parts[0] == 'chest':
        bitcoins+=int(parts[1])
        print(f'You found {int(parts[1])} bitcoins.')
    else:
        health -= int(parts[1])
        if health>0:
            print(f'You slayed {parts[0]}.')
        else:
            print(f'You died! Killed by {parts[0]}.')

            print(f'Best room: {best_room}')
            does_the_hero_died = True
            break

if not does_the_hero_died:
    print(f"You've made it!")
    print(f'Bitcoins: {bitcoins}')
    print(f'Health: {health}')