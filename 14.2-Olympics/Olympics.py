from pprint import pprint


class Reindeer:
    def __init__(self, deer_name, deer_speed, deer_duration, deer_rest):
        self.name = deer_name
        self.speed = deer_speed
        self.duration = deer_duration
        self.rest = deer_rest
        self.distance = 0
        self.running = 0
        self.resting = 0

    def start(self):
        self.distance = 0
        self.running = self.duration
        self.resting = 0

    def run(self):
        if self.resting > 0:
            self.resting -= 1
            if self.resting == 0:
                self.running = self.duration
        elif self.running > 0:
            self.running -= 1
            self.distance += self.speed
            if self.running == 0:
                self.resting = self.rest


def parse_reindeer(reindeer_line):
    tokens = reindeer_line.split(" ")
    deer_name = tokens[0]
    deer_speed = int(tokens[3])
    deer_duration = int(tokens[6])
    deer_rest = int(tokens[-2])

    return deer_name, deer_speed, deer_duration, deer_rest


def leader(current_reindeer):
    leader_name = None
    leader_dist = 0
    for test_deer in current_reindeer:
        if test_deer.distance >= leader_dist:
            leader_name = test_deer.name
            leader_dist = test_deer.distance

    return leader_name, leader_dist


input_file = open("input.txt", "r").read().split("\n")

reindeer_list = []
score = {}

for line in input_file:
    name, speed, duration, rest = parse_reindeer(line)
    reindeer_list.append(Reindeer(name, speed, duration, rest))
    score[name] = 0

for deer in reindeer_list:
    deer.start()
for seconds in range(2504):
    for deer in reindeer_list:
        deer.run()
    name, distance = leader(reindeer_list)
    score[name] += 1

pprint(score)
