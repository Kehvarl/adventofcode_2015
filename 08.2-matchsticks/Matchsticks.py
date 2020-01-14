
def get_length(input_line):
    length = 0
    index = 0
    while index < len(input_line):
        if index == len(input_line)-1:
            length += 1
            index += 1
        elif input_line[index] != "\\":
            length += 1
            index += 1
        elif input_line[index + 1] in [str('\\'), "\""]:
            length += 1
            index += 2
        elif input_line[index + 1] == "x":
            length += 1
            index += 4
        else:
            index += 1
            length += 1
    return length


def reencode(input_line):
    output = "\""
    for char in input_line:
        if char == "\\":
            output += "\\\\"
        elif char == "\"":
            output += "\\\""
        else:
            output += char
    return output + "\""


input_file = open("input.txt", "r").read().split("\n")

total_length = 0
for line in input_file:
    test = line.strip()
    encoded = reencode(test)
    tlen = len(test)
    elen = len(encoded)

    # print(line)
    # print(encoded)
    # print(tlen, elen)
    total_length += (elen) - tlen

print(total_length)
