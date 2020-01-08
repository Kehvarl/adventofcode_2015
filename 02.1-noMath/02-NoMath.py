def area_smallest_side(l, w, h):
    return min(min(l*w, l*h), w*h)


def needed(l, w, h):
    out = 2 * l * w
    out += 2 * l * h
    out += 2 * w * h
    return out + area_smallest_side(l, w, h)


def volume(l, w, h):
    return l * w * h


def shortest_perimeter(l, w, h):
    lw = 2*l + 2*w
    lh = 2*l + 2*h
    wh = 2*w + 2*h
    return min(min(lw, lh), wh)

paper = 0
ribbon = 0

infile = open("input.txt", "r").read().split("\n")
boxes = []
for box in infile:
    (l, w, h) = box.split("x")
    l, w, h = int(l), int(w), int(h)
    box_paper = needed(l, w, h)
    box_ribbon = shortest_perimeter(l, w, h) + volume(l, w, h)
    paper += box_paper
    ribbon += box_ribbon
    boxes.append(((l, w, h), box_paper, box_ribbon))

print(boxes)
print(paper)
print(ribbon)



