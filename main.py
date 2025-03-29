from elements import LOGO, MENU, morse_code_dict

def translate_string_to_morse(param_string_message):
    morse_message = ''
    for character in param_string_message:
        if character in morse_code_dict:
            morse_message += character.replace(character, morse_code_dict[character])
            morse_message += ' '
    print(morse_message)

def translate_morse_to_string(param_morse_message):
    string_message = ''
    splitted_morse_message = param_morse_message.split(" ")
    for morse_character in splitted_morse_message:
        for key, character in morse_code_dict.items():
            if morse_character == character:
                string_message += key
    print(string_message)


print(LOGO)
while True:
    print(MENU)

    menu = int(input("Choose an option: "))
    if menu == 0:
        exit()
    elif menu == 1:
        message = input("Type the text message:\n").upper()
        translate_string_to_morse(message)
    elif menu == 2:
        message = input("Type the morse message:\n")
        translate_morse_to_string(message)
    else:
        print("Invalid selection")
