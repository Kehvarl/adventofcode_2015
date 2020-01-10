

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


input_text = open("input.txt", "r").read().strip().split("\n")
nice = []
naughty = []

for word in input_text:
    is_nice = (double_letter(word) and vowels(word) and reject(word))
    print(word, is_nice)
    if is_nice:
        nice.append(word)
    else:
        naughty.append(word)

print(len(nice))
print(len(naughty))


