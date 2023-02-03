ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


class ExceptionName(Exception):
    pass


def rotor(letter: str, n: int, reverse=False) -> str:
    rot = {
        0: "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        1: "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
        2: "AJDKSIRUXBLHWTMCQGZNPYFVOE",
        3: "BDFHJLCPRTXVZNYEIWGAKMUSQO",
    }
    return (
        ALPHABET[rot[n].find(letter) % len(ALPHABET)]
        if reverse
        else rot[n][ALPHABET.find(letter) % len(rot[n])]
    )


def reflector(letter: str, n: int) -> str:
    ref = {0: "ABCDEFGHIJKLMNOPQRSTUVWXYZ", 1: "YRUHQSLDPXNGOKMIEBFZCWVJAT"}
    return ref[n][ALPHABET.find(letter) % len(ref[n])]


def change(letter: str, key: int) -> str:
    return ALPHABET[(ALPHABET.find(letter) + key) % len(ALPHABET)]


def switching(letter: str, pairs: list) -> str:
    for i in pairs:
        if letter in i:
            return i[(i.find(letter) + 1) % 2]
    return letter


def enigma(
    t: str,
    ref: int,
    rot1: int,
    shift1: int,
    rot2: int,
    shift2: int,
    rot3: int,
    shift3: int,
    pairs: str = "",
) -> str:
    original = {1: 17, 2: 5, 3: 22}
    x = [rot3, rot2, rot1]
    y = [shift3, shift2, shift1]
    result_text = ""
    if pairs:
        check = [i.upper() for i in pairs.split() if i.isalpha()]
        if len(set("".join(check))) != len("".join(check)):
            return "Sorry, it is not possible to make the switching"
        switch = check
    else:
        switch = []
    for word in t:
        y[0] = (y[0] + 1) % 26
        if y[0] == original[rot3]:
            y[1] = (y[1] + 1) % 26
        word = switching(word, switch)
        for j in range(3):
            word = change(rotor(change(word, y[j]), x[j]), y[j] * (-1))
        word = reflector(word, ref)
        for k in range(2, -1, -1):
            word = change(rotor(change(word, y[k]), x[k], reverse=True), y[k] * (-1))
        word = switching(word, switch)
        result_text += word
        if (y[1] + 1) == original[rot2]:
            y[1] = (y[1] + 1) % 26
            y[2] = (y[2] + 1) % 26
    return result_text


def text(text_first: str) -> str:
    try:
        t1 = "".join([i for i in text_first.upper() if i in ALPHABET])
        if not t1:
            raise ExceptionName
        t2 = "".join([i for i in text_first.upper() if i.isalpha()])
        if len(t1) != len(t2):
            raise ExceptionName
    except ExceptionName:
        text_repeat = input(
            "Please enter your text to encrypt or decrypt again (only english words):"
        )
        return text(text_repeat)
    else:
        return t1


def main():
    text_question = input("Enter your text to encrypt / decrypt (only english words):")
    t = text(text_question)
    print("Your encrypted / decrypted text:", enigma(t, 1, 1, 0, 2, 0, 3, 0, ""))


if __name__ == "__main__":
    main()