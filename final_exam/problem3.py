n = int(input())

my_heroes = {}

for h in range(n):
    hero = input().split()
    my_heroes[hero[0]] = [int(hero[1]),int(hero[2])]

command = input().split(' - ')
while command[0] != 'End':
    action = command[0]
    hero_name = command[1]

    if action == 'CastSpell':
        mp_needed = int(command[2])
        spell_name = command[3]
        hero_mp = my_heroes[hero_name][1]
        if hero_mp>=mp_needed:
            my_heroes[hero_name][1]-=mp_needed
            hero_mp = my_heroes[hero_name][1]
            print(f'{hero_name} has successfully cast {spell_name} and now has {hero_mp} MP!')
        else:
            print(f'{hero_name} does not have enough MP to cast {spell_name}!')

    elif action == 'TakeDamage':
        damage = int(command[2])
        attacker = command[3]
        my_heroes[hero_name][0]-=damage
        my_hero_hp = my_heroes[hero_name][0]
        if my_hero_hp>0:
            print(f'{hero_name} was hit for {damage} HP by {attacker} and now has {my_hero_hp} HP left!')
        else:
            print(f'{hero_name} has been killed by {attacker}!')
            del my_heroes[hero_name]
    elif action == 'Recharge':
        amount = int(command[2])
        my_heroes[hero_name][1] += amount
        if my_heroes[hero_name][1]>200:
            amount_recharge = my_heroes[hero_name][1] - amount
            amount_recharge  -=amount
            my_heroes[hero_name][1] = 200
            print(f'{hero_name} recharged for {amount_recharge} MP!')
        else:
            print(f'{hero_name} recharged for {amount} MP!')
    elif action == 'Heal':
        healing = int(command[2])
        my_heroes[hero_name][0] += healing
        if my_heroes[hero_name][0] > 100:
            amount_healed = my_heroes[hero_name][0] - healing
            amount_healed = 100 - amount_healed
            my_heroes[hero_name][0] = 100

            print(f'{hero_name} healed for {amount_healed} HP!')
        else:
            print(f'{hero_name} healed for {healing} HP!')
    else:
        continue
    command = input().split(' - ')


# {'Adela': [90, 200], 'SirMullich': [100, 40]}
for hp in(sorted(my_heroes.items(),key=lambda hp:(-hp[1][0],hp[0]))):
    print(hp[0])
    print(f'  HP: {hp[1][0]}')
    print(f'  MP: {hp[1][1]}')

