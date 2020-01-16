
# string = "111221"
input_string = "1113222113"


def looksay(string):
    out_string = ""
    count = 1
    current = None

    for char in string:
        if current is None:
            current = char
            count = 1
        elif char == current:
            count += 1
        elif char != current:
            out_string += str(count) + str(current)
            count = 1
            current = char
    out_string += str(count) + str(current)
    count = 1
    current = char

    return out_string


saystring = input_string
for _ in range(50):
    saystring = looksay(saystring)

print(len(saystring))

