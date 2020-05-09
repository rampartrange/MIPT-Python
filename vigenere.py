import exceptions
from config import input_text, output_text, ALPHABET_POWER
from config import char_to_code, code_to_char


def vigenere_move(char, key_char, style="encode"):
    if style == "encode":
        new_code = (char_to_code[char.lower()] + char_to_code[key_char.lower()]) % ALPHABET_POWER
    else:
        new_code = (char_to_code[char.lower()] + ALPHABET_POWER - char_to_code[key_char.lower()]) % ALPHABET_POWER
    return code_to_char[new_code] if char.islower() else code_to_char[new_code].upper()


def encrypt(args, style):
    args.key = exceptions.cast_key(args.key, "vigenere")
    if args.key is None:
        return
    input_t = open(input_text, "r")
    output_t = open(output_text, "w")
    lines = input_t.readlines()
    symbol_num = 0
    key_len = len(args.key)
    for line in lines:
        encrypted_line = ''
        for symbol in line:
            if symbol.isalpha():
                encrypted_line += vigenere_move(symbol, args.key[symbol_num % key_len], style)
                symbol_num += 1
            else:
                encrypted_line += symbol
        output_t.write(encrypted_line)
    input_t.close()
    output_t.close()
