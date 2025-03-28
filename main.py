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

def translate(param_message):
    morse_message = ''
    for character in param_message:
        if character in morse_code_dict:
            morse_message += character.replace(character, morse_code_dict[character])
            morse_message += ' '
    print(morse_message)

translate(message)