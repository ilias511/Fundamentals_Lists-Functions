raw_activation_key= input()

command = input()
while command!='Generate':
    info = command.split('>>>')
    if info[0] == 'Contains':
        substring = info[1]
        if substring in raw_activation_key:
            print(f'{raw_activation_key} contains {substring}')
        else:
            print('Substring not found!')
    elif info[0] == 'Flip':
        up_low = info[1]
        startIndex = int(info[2])
        endIndex = int(info[3])

        change = raw_activation_key[startIndex:endIndex]
        if up_low == 'Upper':
            change = change.upper()
            f = raw_activation_key[:startIndex]
            e = raw_activation_key[endIndex:]
            raw_activation_key = f+change+e
            print(raw_activation_key)
        elif up_low == 'Lower':
            change = change.lower()
            f = raw_activation_key[:startIndex]
            e = raw_activation_key[endIndex:]
            raw_activation_key = f + change + e
            print(raw_activation_key)
    elif info[0] == 'Slice':
        start_index = int(info[1])
        end_index = int(info[2])
        deleted_text = raw_activation_key[start_index:end_index]
        raw_activation_key = raw_activation_key.replace(deleted_text,'')
        print(raw_activation_key)
    command = input()
print(f'Your activation key is: {raw_activation_key}')