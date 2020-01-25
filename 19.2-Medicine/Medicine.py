from collections import deque


def process_molecule(starting_molecule, conversions, step):
    output_molecules = set()

    for atom in conversions:
        for swap in conversions[atom]:
            match = starting_molecule.find(atom)
            while match != -1:
                output_molecules.add((starting_molecule[:match] + swap + starting_molecule[match + len(atom):], step))
                match = starting_molecule.find(atom, match + 1)

    return output_molecules


def generate_molecules(length, conversions):
    found_molecules = deque(process_molecule("e", conversions, 2))
    molecule_steps = {}
    while found_molecules:
        working_mol, w_step = found_molecules.popleft()
        mols = process_molecule(working_mol, conversions, w_step)
        for mol, step in mols:
            if len(mol) < length:
                found_molecules.append((mol, step + 1))
            elif len(mol) == length:
                if not molecule_steps.get(mol):
                    molecule_steps[mol] = step
                else:
                    molecule_steps[mol] = min(molecule_steps[mol], step)

    return molecule_steps


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

# molecule="HOHOHO"
solution = generate_molecules(len(molecule), translations)
print(solution)
print(solution[molecule])
