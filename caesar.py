import exceptions
import json
import trainer
from copy import deepcopy
from config import input_text, output_text, ALPHABET_POWER, alphabet_lower


def caesar_move(char, key):
    zero_char = "A" if char.isupper() else "a"
    return chr(ord(zero_char) + (ord(char) + key - ord(zero_char)) % ALPHABET_POWER)


def encode(args):
    args.key = exceptions.cast_key(args.key, "caesar")
    if args.key is None:
        return
    input_t = open(input_text, "r")
    output_t = open(output_text, "w")
    lines = input_t.readlines()
    for line in lines:
        encoded_line = ''
        for symbol in line:
            encoded_line += caesar_move(symbol, args.key) if symbol.isalpha() else symbol
        output_t.write(encoded_line)
    input_t.close()
    output_t.close()


def decode(args):
    args.key = exceptions.cast_key(args.key, "caesar")
    if args.key is None:
        return
    input_t = open(input_text, "r")
    output_t = open(output_text, "w")
    lines = input_t.readlines()
    for line in lines:
        decoded_line = ''
        for symbol in line:
            decoded_line += caesar_move(symbol, -args.key) if symbol.isalpha() else symbol
        output_t.write(decoded_line)
    input_t.close()
    output_t.close()


def hack(args):
    with open(args.model_file) as model_f:
        model = json.load(model_f)

        shift_indexes = [0 for shift in range(ALPHABET_POWER)]
        final_shift = 0
        current_model = trainer.get_updated_model(input_text)

        for shift in range(ALPHABET_POWER):
            for symbol in alphabet_lower:
                shift_indexes[shift] += (model.get(symbol, 0) - current_model.get(symbol, 0)) ** 2

            final_shift = final_shift if shift_indexes[final_shift] > shift_indexes[shift] else shift

            next_model = deepcopy(current_model)
            for symbol_id in range(ALPHABET_POWER):
                new_symbol_id = (symbol_id + 1) % ALPHABET_POWER
                next_model[alphabet_lower[symbol_id]] = current_model[alphabet_lower[new_symbol_id]]

            current_model = next_model

        args.key = str(final_shift)
        encode(args)
    model_f.close()

