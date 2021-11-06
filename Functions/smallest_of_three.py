def palindrome(user):
    for i in user:
        if i == i[::-1]:
            print(i[::-1])

        else:
            print(i[::-1])


user = input().split(', ')
palindrome(user)
