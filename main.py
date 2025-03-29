message = input("Type the message:\n").upper() # input message

# morse code dictionary
morse_code_dict = {
    # letters
    'A': '.-', 'B': '-...', 'C': '-.-.',
    'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',

    # numbers
    '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..',
    '9': '----.',

    # special characters
    '.': '.-.-.-', ',': '--..--', '?': '..--..',
    '!': '-.-.--', "'": '.----.', '/': '-..-.',
    '(': '-.--.', ')': '-.--.-', '&': '.-...',
    ':': '---...', ';': '-.-.-.', '=': '-...-',
    '+': '.-.-.', '-': '-....-', '_': '..--.-',
    '"': '.-..-.', '$': '...-..-', '@': '.--.-.',
    ' ': '/'
}

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

# translate_string_to_morse(message)

translate_morse_to_string(message)