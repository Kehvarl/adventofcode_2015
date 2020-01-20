
def parse_reindeer(reindeer_line):
    tokens = reindeer_line.split(" ")
    name = tokens[0]
    speed = int(tokens[3])
    duration = int(tokens[6])
    rest = int(tokens[-2])

    return name, speed, duration, rest


def run_reindeer(reindeer, seconds):
    name, speed, duration, rest = reindeer

    distance = 0
    running = duration
    resting = 0
    for _ in range(seconds):
        if resting > 0:
            resting -= 1
            if resting == 0:
                running = duration
        elif running > 0:
            running -= 1
            distance += speed
            if running == 0:
                resting = rest

    return distance


input_file = open("input.txt", "r").read().split("\n")

reindeer = []

for line in input_file:
    reindeer.append(parse_reindeer(line))

for deer in reindeer:
    print(run_reindeer(deer, 2503))


