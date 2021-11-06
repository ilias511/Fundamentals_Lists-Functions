nums = (input()).split()

added = [int(i) for i in nums]
is_five = False
output = []

average = sum(added) / len(added)

for n in added:
    if len(added)<5:
        print('No')
        is_five = True
        break
    if int(n)>average:
        output.append(n)


if is_five:
    pass
else:
    output.sort(reverse=True)
    if len(added)>=5:

        strr = [str(o) for o in output]

        print(' '.join(strr[:5]))