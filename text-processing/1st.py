usernames = input().split(', ')
pr = []
for name in usernames:
    if 3<=len(name)<=16:

        is_valid = True
        for ch in name:
            if not ch.isdigit() and not ch.isalpha() and not '-' in name and not '_' in name:
                is_valid = False
                break
        if is_valid:
            pr.append(name)
for n in pr:
    print(n)