

def double_letter(source):
    match = source[0]
    for letter in source[1:]:
        if letter == match:
            return  True
        else:
            match = letter
    return False


def vowels(source):
    letters = 0
    vowel_list = "aeiou"
    for letter in source:
        if letter in vowel_list:
            letters += 1

    return letters >= 3


def reject(source):
    blacklist = ["ab", "cd", "pq", "xy"]
    for pair in blacklist:
        if pair in source:
            return False
    return True


def repeating(source):
    for index in range(2, len(source)):
        if source[index] == source[index - 2]:
            return True
    return False


def repeated_pair(source):
    for index in range(1, len(source)):
        pair = source[index - 1] + source[index]
        if source.find(pair, index+1) > 0:
            return True

    return False


input_text = open("input.txt", "r").read().strip().split("\n")
nice = []
naughty = []

for word in input_text:
    is_nice = (repeating(word) and repeated_pair(word))
    print(word, is_nice)

    print(repeating(word))
    print(repeated_pair(word))

    if is_nice:
        nice.append(word)
    else:
        naughty.append(word)

print(len(nice))
print(len(naughty))


