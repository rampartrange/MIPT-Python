from string import ascii_lowercase


input_text = "input_source.txt"
output_text = "output_source.txt"
ALPHABET_POWER = 26
char_to_code = {ascii_lowercase[i]: i for i in range(ALPHABET_POWER)}
code_to_char = {i: ascii_lowercase[i] for i in range(ALPHABET_POWER)}
