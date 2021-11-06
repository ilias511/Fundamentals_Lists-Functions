
commands = input()

guests_liked_disliked = {}
unliked_meals = 0
while commands!='Stop':
    info = commands.split('-')
    like_dislike = info[0]
    guest = info[1]
    meal = info[2]
    if like_dislike == 'Like':
        if guest not in guests_liked_disliked:
            guests_liked_disliked[guest]=[meal]
        elif meal not in guests_liked_disliked[guest]:
            guests_liked_disliked[guest].append(meal)
    elif like_dislike == 'Unlike':
        if guest in guests_liked_disliked:
            if meal in guests_liked_disliked[guest]:
                guests_liked_disliked[guest].remove(meal)
                print(f"{guest} doesn't like the {meal}.")
                unliked_meals+=1
            else:
                print(f"{guest} doesn't have the {meal} in his/her collection.")

        elif guest not in guests_liked_disliked:
            print(f'{guest} is not at the party.')

    commands = input()
for name, meals in (sorted(guests_liked_disliked.items(),key=lambda x: (-len(x[1]),x[0]))):
    print(f"{name}: {', '.join(meals)}")


print(f'Unliked meals: {unliked_meals}')