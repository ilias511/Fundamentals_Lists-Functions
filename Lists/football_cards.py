team_a = 11
team_b = 11

card = input().split(' ')
final_set = set(card)
is_terminated = False

for team in final_set:
    if 'A' in team:
        team_a-=1
    elif 'B' in team:
        team_b-=1
    if team_a<7 or team_b<7:
        is_terminated = True
        break


if is_terminated:
    print(f'Team A - {team_a}; Team B - {team_b}')
    print('Game was terminated')
else:
    print(f'Team A - {team_a}; Team B - {team_b}')