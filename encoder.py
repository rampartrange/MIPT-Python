import argparse
import vigenere
import caesar
import sys
import trainer
from config import input_text, output_text


def get_input(input_file):

    with open(input_text, "w") as input_t:
        while input_file == input_text or input_file == output_text:
            print("You're trying to use reserved filename '{}', please choose another name for you file:"
                  "".format(input_file))
            input_file = input()
        if input_file is None:
            print("Input your text:")
            input_t.write(sys.stdin.read())
        else:
            # try to put exception
            with open(input_file, "r") as input_f:
                input_t.write(input_f.read())
            input_f.close()
    input_t.close()
    return input_file


def get_output(output_file):
    with open(output_text, "r") as output_t:
        while output_file == input_text or output_file == output_text:
            print("You're trying to use reserved filename '{}', please choose another name for you file:"
                  "".format(output_file))
            output_file = input()
        if output_file is None:
            sys.stdout.write(output_t.read())
        else:
            with open(output_file, "w") as output_f:
                output_f.write(output_t.read())
            output_f.close()
    output_t.close()
    return output_file


def encode(args):
    args.input_file = get_input(args.input_file)
    while True:
        if args.cipher == "caesar":
            caesar.encode(args)
            break
        if args.cipher == "vigenere":
            vigenere.encode(args)
            break
        print("Please, enter correct cipher or press 'q' to quit")
        args.cipher = input()
        if args.cipher == "q":
            break
    args.output_file = get_output(args.output_file)


def decode(args):
    args.input_file = get_input(args.input_file)
    while True:
        if args.cipher == "caesar":
            caesar.decode(args)
            break
        if args.cipher == "vigenere":
            vigenere.decode(args)
            break
        print("Please, enter correct cipher or press 'q' to quit")
        args.cipher = input()
        if args.cipher == "q":
            break
    args.output_file = get_output(args.output_file)


def train(args):
    args.model_file = trainer.get_json_model(args.text_file, args.model_file)


def hack(args):
    args.input_file = get_input(args.input_file)
    caesar.hack(args)
    args.output_file = get_output(args.output_file)


parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

# encode
encode_parser = subparsers.add_parser('encode')
encode_parser.set_defaults(function=encode)
encode_parser.add_argument("--cipher", type=str, choices=["caesar", "vigenere"], default=None)
encode_parser.add_argument("--key", type=str, default=None)
encode_parser.add_argument("--input-file", dest="input_file", type=str, default=None)
encode_parser.add_argument("--output-file", dest="output_file", type=str, default=None)

# decode
decode_parser = subparsers.add_parser('decode')
decode_parser.set_defaults(function=decode)
decode_parser.add_argument("--cipher", type=str, choices=["caesar", "vigenere"], default=None)
decode_parser.add_argument("--key", type=str, default=None)
decode_parser.add_argument("--input-file", dest="input_file", type=str, default=None)
decode_parser.add_argument("--output-file", dest="output_file", type=str, default=None)

# train
train_parser = subparsers.add_parser('train')
train_parser.set_defaults(function=train)
train_parser.add_argument("--text-file", dest="text_file", type=str, default=None)
train_parser.add_argument("--model-file", dest="model_file", type=str, default=None, required=True)


# hack
hack_parser = subparsers.add_parser('hack')
hack_parser.set_defaults(function=hack)
hack_parser.add_argument("--cipher", type=str, choices=["caesar", "vigenere"], default=None)
hack_parser.add_argument("--key", type=str, default=None)
hack_parser.add_argument("--model-file", dest="model_file", type=str, default=None, required=True)
hack_parser.add_argument("--input-file", dest="input_file", type=str, default=None)
hack_parser.add_argument("--output-file", dest="output_file", type=str, default=None)


arguments = parser.parse_args()

arguments.function(arguments)

print(arguments)