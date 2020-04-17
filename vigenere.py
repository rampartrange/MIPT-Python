import exceptions
from config import input_text, output_text, ALPHABET_POWER


def vigenere_move(char, key_char, isencode=True):
    if char.isupper():
        zero_char = "A"
        key_char = key_char.upper()
    else:
        zero_char = "a"
        key_char = key_char.lower()
    if isencode:
        return chr(ord(zero_char) + (ord(char) + ord(key_char) - 2 * ord(zero_char)) % ALPHABET_POWER)
    else:
        return chr(ord(zero_char) + (ord(char) - ord(key_char)) % ALPHABET_POWER)


def encode(args):
    args.key = exceptions.cast_key(args.key, "vigenere")
    if args.key is None:
        return
    input_t = open(input_text, "r")
    output_t = open(output_text, "w")
    lines = input_t.readlines()
    symbol_num = 0
    key_len = len(args.key)
    for line in lines:
        encoded_line = ''
        for symbol in line:
            if symbol.isalpha():
                encoded_line += vigenere_move(symbol, args.key[symbol_num % key_len], True)
                symbol_num += 1
            else:
                encoded_line += symbol
        output_t.write(encoded_line)
    input_t.close()
    output_t.close()


def decode(args):
    args.key = exceptions.cast_key(args.key, "vigenere")
    if args.key is None:
        return
    input_t = open(input_text, "r")
    output_t = open(output_text, "w")
    lines = input_t.readlines()
    symbol_num = 0
    key_len = len(args.key)
    for line in lines:
        decoded_line = ''
        for symbol in line:
            if symbol.isalpha():
                decoded_line += vigenere_move(symbol, args.key[symbol_num % key_len], False)
                symbol_num += 1
            else:
                decoded_line += symbol
        output_t.write(decoded_line)
    input_t.close()
    output_t.close()

