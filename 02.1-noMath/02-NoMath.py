def area_smallest_side(l, w, h):
    return min(min(l*w, l*h), w*h)

def needed(l, w, h):
    out = 2 * l * w
    out += 2 * l * h
    out += 2 * w * h
    return out + area_smallest_side(l, w, h)

total = 0

infile = open("input.txt", "r").read().split("\n")
boxes = []
for box in infile:
    (l, w, h) = box.split("x")
    need = needed(int(l), int(w), int(h))
    total += need
    boxes.append(((l, w, h), need))

print(boxes)
print(total)
