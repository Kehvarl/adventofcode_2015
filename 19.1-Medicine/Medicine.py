from pprint import pprint

input_file = open("input.txt", "r").read().split("\n")

molecule = input_file[-1]
input_file = input_file[:-1]

translations = {}

for line in input_file:
    m_in, m_out = line.split(" => ")
    if not translations.get(m_in):
        translations[m_in] = [m_out]
    else:
        translations[m_in].append(m_out)


print(translations)

possible_outputs = set()

# molecule = "HOHOHO"
# molecule="H20"

for atom in translations:
    for swap in translations[atom]:
        match = molecule.find(atom)
        while match != -1:
            possible_outputs.add(molecule[:match] + swap + molecule[match + len(atom):])
            match = molecule.find(atom, match + 1)

while False:
    for index in range(len(molecule)):
        char = molecule[index]
        for swap in translations[char]:
            new_mol = molecule[0:index] + swap + molecule[index+1:]
            possible_outputs.add(new_mol)

print(molecule)
pprint(possible_outputs)
print(len(possible_outputs))
