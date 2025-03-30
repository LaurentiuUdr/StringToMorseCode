from elements import LOGO, MENU, morse_code_dict

# create a reverse dictionary to optimize the search
reverse_morse_code_dict = {v: k for k, v in morse_code_dict.items()}

def translate_string_to_morse(param_string_message):
    morse_message = []
    for character in param_string_message:
        if character in morse_code_dict:
            morse_message.append(morse_code_dict[character])
    return ' '.join(morse_message)

def translate_morse_to_string(param_morse_message):
    string_message = []
    for morse_character in param_morse_message.split():
        if morse_character in reverse_morse_code_dict:
            string_message.append(reverse_morse_code_dict[morse_character])
    return ''.join(string_message)


print(LOGO)
while True:
    print(MENU)

    menu = int(input("Choose an option: "))
    if menu == 0:
        exit()
    elif menu == 1:
        message = input("Type the text message:\n").upper()
        print(translate_string_to_morse(message))
    elif menu == 2:
        message = input("Type the morse message:\n")
        print(translate_morse_to_string(message))
    else:
        print("Invalid selection")


