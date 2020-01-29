class TuringLock:
    def __init__(self, code, registers=None):
        if registers is None:
            self.registers = {"a": 0, "b": 0}
        else:
            self.registers = registers
        self.program_counter = 0
        self.assembly = code

    def step(self):
        self.decode()

    def decode(self):
        register = None
        relative_address = None
        op_code, rest = self.assembly[self.program_counter].split(" ", 1)
        if op_code in ["jio", "jie"]:
            register, relative_address = rest.split(", ")
            relative_address = int(relative_address)
        elif op_code == "jmp":
            relative_address = int(rest)
        else:
            register = rest

        self.execute(op_code, register, relative_address)

    def execute(self, op_code, register, relative_address):
        if op_code == "inc":  # Increment Register
            self.registers[register] += 1
            self.program_counter += 1
        elif op_code == "hlf":  # Halve Register
            self.registers[register] = self.registers[register] // 2
            self.program_counter += 1
        elif op_code == "tpl":  # Triple Register
            self.registers[register] = self.registers[register] * 3
            self.program_counter += 1
        elif op_code == "jmp":  # jump
            self.program_counter += relative_address
        elif op_code == "jie":  # jump if EVEN
            if self.registers[register] % 2 == 0:
                self.program_counter += relative_address
            else:
                self.program_counter += 1
        elif op_code == "jio":  # jump if ONE
            if self.registers[register] == 1:
                self.program_counter += relative_address
            else:
                self.program_counter += 1


input_file = open("input.txt", "r").read().split("\n")

computer = TuringLock(input_file, registers={"a":1, "b":0})

while computer.program_counter < len(computer.assembly):
    computer.step()

print(computer.registers)

