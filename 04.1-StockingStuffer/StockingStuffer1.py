import hashlib


input_string = "ckczppom"

number = 0

while True:
    test_hash = hashlib.md5(str(input_string + str(number)).encode())

    if str(test_hash.hexdigest())[0:5] == "00000":
        print(number)
        break
    else:
        number += 1

