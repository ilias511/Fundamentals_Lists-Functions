
valid_code_user = 'iliasgrbg15'

user_login = input()
failed_attemps = 0

while failed_attemps<5:

    if user_login==valid_code_user:
        print('You have login in successfully')
        break
    else:
        print('wrong password try again')
        failed_attemps+=1
        if failed_attemps == 5:
            print('You have been banned go to the offices')
    user_login = input()