message = input()

command = input()


while command!= 'Reveal':
    splited = command.split(':|:')
    first = splited[0]
    sec = splited[1]
    if first == 'InsertSpace':
        message_new = list(message)
        message_new.insert(int(sec),' ')
        message = ''.join(message_new)
        print(message)
    elif first == 'ChangeAll':
        trd = splited[2]
        for i in message:
            if i == sec:

                message = message.replace(i,trd)
                print(message)
                break
    elif first == 'Reverse':
        if sec in message:
            message = message.replace(sec,'')
            sec = sec[::-1]
            message+=sec
            print(message)
        else:
            print('error')
    command = input()

print(f'You have a new text message: {message}')