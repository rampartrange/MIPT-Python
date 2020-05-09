import json
from config import input_text, output_text
from string import ascii_lowercase


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
    for symbol in ascii_lowercase:
        result[symbol] = stats.get(symbol, 0) / max(letters_num, 1)

    return result


def get_json_model(input_file, model_file):
    while model_file == input_text or model_file == output_text:
        print("You're trying to use reserved filename '{}', please choose another name for your file"
              "".format(model_file))
        model_file = input()
    result = get_updated_model(input_file)
    with open(model_file, "w") as model_f:
        json.dump(result, model_f)
    model_f.close()
    return model_file
