users_name_id = {}

count_users = int(input())

for user in range(1,count_users+1):
    command = input().split(' ')
    r_u = command[0]
    username = command[1]
    if r_u == 'register':
        licence_plate = command[2]
        if username in users_name_id:
            print(f'ERROR: already registered with plate number {licence_plate}')
        else:
            print(f'{username} registered {licence_plate} successfully')
            users_name_id[username] = licence_plate
    elif r_u == 'unregister':
        if username not in users_name_id:
            print(f'ERROR: user {username} not found')
        else:
            print(f'{username} unregistered successfully')
            users_name_id.pop(username)


for key,value in users_name_id.items():
    print(f'{key} => {value}')
