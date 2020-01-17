def increment_string(input_string, index=0):
    working_string = list(input_string[::-1])

    carry = False
    char, carry = increment_char(working_string[index])
    working_string[index] = char
    while carry:
        index += 1
        char, carry = increment_char(working_string[index])
        working_string[index] = char

    return "".join(working_string[::-1])


def increment_char(char):
    carry = False
    if char == "z":
        char = "a"
        carry = True
    else:
        char = chr(ord(char) + 1)

    return char, carry


def straight(input_string):
    if len(input_string) < 2:
        return False
    for index in range(len(input_string) - 2):
        c = ord(input_string[index])
        c1 = ord(input_string[index + 1])
        c2 = ord(input_string[index + 2])

        if c1 == c + 1 and c2 == c + 2:
            return True

    return False


def double_letter(input_string):
    pairs = []
    match = input_string[0]
    for index in range(1, len(input_string)):
        letter = input_string[index]
        if letter == match:
            pairs.append(index)
        else:
            match = letter

    for pair in pairs:
        if any(elem > (pair + 1) for elem in pairs):
            return True
    return False


def test_password(input_string):
    if any(elem in r"iol" for elem in input_string):
        return False

    if not double_letter(input_string):
        return False

    if not straight(input_string):
        return False

    return True


# test_string = "abcdefgh"  # abcdffaa
test_string = "cqjxjnds"
while not test_password(test_string):
    test_string = increment_string(test_string)
print("part 1:", test_string)


test_string = increment_string(test_string)
while not test_password(test_string):
    test_string = increment_string(test_string)
print("part 2:", test_string)
