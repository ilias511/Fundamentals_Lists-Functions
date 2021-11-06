import re

count_strings = int(input())
pattern = r'!(?P<command>[A-Z][a-z]{3,})!:(?P<str>[[A-Za-z]{8,}])'

validators = []
for i in range(count_strings):

    text = input()
    valid = re.fullmatch(pattern,text)
    if valid is not None:
        validators.append(valid)
        for i in validators:
            # i.group('str') = i.group('str').replace('[','')
            # i.group('str') = i.group('str').replace(']','')
            s_group = i.group('str')
            s_group = s_group.replace('[', '')
            s_group = s_group.replace(']', '')
            name = i.group('command')
            value = []
            for k in s_group:
                value.append(str(ord(k)))
            string_values = ' '.join(value)
            print(f'{name}: {string_values}')
    else:
        print('The message is invalid')


