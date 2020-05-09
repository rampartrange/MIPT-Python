def types_for_ciphers(cipher):
    if cipher == "caesar":
        return int
    if cipher == "vigenere":
        return str


def cast_key(key, cipher):
    while True:
        if key is not None:
            if cipher == "caesar":
                if key.isdecimal():
                    return int(key)

            if cipher == "vigenere":
                if key.isalpha():
                    return key

        print("Key Type Exception occured \n"
              "Input key :{}\n" \
              "Input key's type :{}\n" \
              "Current cipher : {}\n" \
              "Required key's type {}\n".format(key, type(key),
                                                cipher, types_for_ciphers(cipher))
              )
        print("Enter correct key or press 'q' to quit")
        key = input()
        if key == "q":
            return None
