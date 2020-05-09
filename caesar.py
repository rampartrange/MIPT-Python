import exceptions
import json
import trainer
from copy import deepcopy
from config import input_text, output_text, ALPHABET_POWER
from config import code_to_char, char_to_code
from string import ascii_lowercase


def caesar_move(char, key):
    new_code = (char_to_code[char.lower()] + key) % ALPHABET_POWER
    return code_to_char[new_code] if char.islower() else code_to_char[new_code].upper()


def encrypt(args, style):
    args.key = exceptions.cast_key(args.key, "caesar")
    if args.key is None:
        return
    input_t = open(input_text, "r")
    output_t = open(output_text, "w")
    lines = input_t.readlines()
    for line in lines:
        encrypted_line = ''
        for symbol in line:
            if style == "encode":
                encrypted_line += caesar_move(symbol, args.key) if symbol.isalpha() else symbol
            else:
                encrypted_line += caesar_move(symbol, -args.key) if symbol.isalpha() else symbol
        output_t.write(encrypted_line)
    input_t.close()
    output_t.close()


def hack(args):
    with open(args.model_file) as model_f:
        model = json.load(model_f)

        shift_indexes = [0 for shift in range(ALPHABET_POWER)]
        final_shift = 0
        current_model = trainer.get_updated_model(input_text)

        for shift in range(ALPHABET_POWER):
            for symbol in ascii_lowercase:
                shift_indexes[shift] += (model.get(symbol, 0) - current_model.get(symbol, 0)) ** 2

            final_shift = final_shift if shift_indexes[final_shift] < shift_indexes[shift] else shift

            next_model = deepcopy(current_model)
            for symbol_id in range(ALPHABET_POWER):
                new_symbol_id = (symbol_id + 1) % ALPHABET_POWER
                next_model[ascii_lowercase[symbol_id]] = current_model[ascii_lowercase[new_symbol_id]]

            current_model = next_model

        args.key = str(final_shift)
        encrypt(args, "decode")
    model_f.close()

