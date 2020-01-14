
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
    return length


input_file = open("test.txt", "r").read().split("\n")

total_length = 0
for line in input_file:
    test = line.strip().strip("\"")
    tlen = get_length(test)
    print(line)
    print(test, tlen)
    total_length += len(line) - tlen

print(total_length)
