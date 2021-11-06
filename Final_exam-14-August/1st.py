text = input()

command = input()

while command!='End':
    possible_commands = command.split()
    final_command = possible_commands[0]
    if final_command == 'Translate':
        char = possible_commands[1]
        replacement = possible_commands[2]
        text = text.replace(char,replacement)
        print(text)

    elif final_command == 'Includes':
        string = possible_commands[1]
        if string in text:
            print(True)
        else:
            print(False)

    elif final_command == 'Start':
        string_starts = possible_commands[1]
        if text.startswith(string_starts):
            print(True)
        else:
            print(False)
    elif final_command == 'Lowercase':
        text = text.lower()
        print(text)

    elif final_command == 'FindIndex':
        ch_find = possible_commands[1]
        print(text.rfind(ch_find))
    elif final_command == 'Remove':
        start_index = int(possible_commands[1])
        count = int(possible_commands[2])
        text = list(text)
        for i in range(start_index,count):
            text.remove(text[i])

        print(text)

    command = input()
