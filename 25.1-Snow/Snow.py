last = 20151125

for diagonal in range(2, 7000):
    r = diagonal
    c = 1
    while c <= diagonal:
        last = (last * 252533) % 33554393
        if r == 2981 and c == 3075:
            print(last)
        r -= 1
        c += 1
