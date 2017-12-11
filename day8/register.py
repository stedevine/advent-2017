import unittest

def read_file(file_name):
    """Helper function, read file return contents as string"""
    file_handle = open(file_name, 'r')
    return file_handle.read().strip()

def createRegisters(inputString):
    registers = {}
    for line in iter(inputString.splitlines()):
        # register is the first string in the line
        # initialize them all to zero
        registers[line.split()[0]] = 0

    return registers

def runInstructions(inputString):
    allTimeHighest = 0
    currentHighest = 0
    registers = createRegisters(inputString)
    for line in iter(inputString.splitlines()):
        # line is [register] [increase or decrease] [value] if [register] [operator] [value]

        # let's look at the condition
        condition = line.split("if ")[1]
        r = condition.split()[0]
        op = condition.split()[1]
        v = condition.split()[2]

        #eval (str(registers[r]) + " " +  op +  v)
        if eval (str(registers[r]) + " " +  op +  v):
            # change the register
            action = line.split("if ")[0].split()
            if action[1] == 'inc':
                registers[action[0]] += int(action[2])
            else:
                registers[action[0]] -= int(action[2])

            currentHighest = registers[max(registers, key=registers.get)]
        if (currentHighest > allTimeHighest):
            allTimeHighest = currentHighest

    return (currentHighest, allTimeHighest)

def evaluateCondition(v1, op, v2):
    if op == '==':
        return v1 == v2
    if op == '<':
        return v1 < v2
    if op == '<=':
        return v1 <= v2
    if op == '>':
        return v1 > v2
    if op == '>=':
        return v1 >= v2
    if op == '!=':
        return v1 != v2

class Test(unittest.TestCase):
    def test(self):
        instructions = """b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10"""
        self.assertEqual(runInstructions(instructions), (1,10))

print(runInstructions(read_file("input.txt")))
