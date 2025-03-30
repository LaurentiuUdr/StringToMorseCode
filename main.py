from elements import LOGO, MENU, morse_dict

# create a reverse dictionary to optimize the search
reverse_morse_dict = {v: k for k, v in morse_dict.items()}

def translate_text_to_morse(text):
    return ' '.join(morse_dict.get(char, '?') for char in text)

def translate_morse_to_text(morse):
    return ''.join(reverse_morse_dict.get(code, '?') for code in morse.split())

def main():
    print(LOGO)
    while True:
        print(MENU)

        try:
            menu_option = int(input("Choose an option: "))
        except ValueError:
            print("Invalid selection. Please choose a valid option.")
            continue

        if menu_option == 0:
            print("Exiting program...")
            break
        elif menu_option == 1:
            message = input("Type the text message:\n").upper()
            print(translate_text_to_morse(message))
        elif menu_option == 2:
            message = input("Type the morse message:\n")
            print(translate_morse_to_text(message))
        else:
            print("Invalid selection. Please choose a valid option.")

if __name__ == "__main__":
    main()