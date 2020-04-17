import json
from config import input_text, output_text, alphabet_lower


def calc_stats(stats, input_file):
    letter_num = 0
    with open(input_file, "r") as input_f:
        for line in input_f:
            for symbol in line.lower():
                stats[symbol] = stats.get(symbol, 0) + 1
                letter_num += 1
    input_f.close()
    return letter_num


def get_updated_model(input_file):
    stats = dict()
    letters_num = calc_stats(stats, input_file)
    result = dict()
    for symbol in alphabet_lower:
        result[symbol] = stats.get(symbol, 0) / max(letters_num, 1)

    return result


def get_json_model(input_file, model_file):
    result = get_updated_model(input_file)
    with open(model_file, "w") as model_f:
        json.dump(result, model_f)
    model_f.close()