up = input().split(', ')
down = input().split(', ')
final = []


for i in up:
    for j in down:
        if j.find(i)>-1:
            final.append(i)
            break
print(final)
