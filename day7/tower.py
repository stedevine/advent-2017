import unittest
from sets import Set

def read_file(file_name):
    """Helper function, read file return contents as string"""
    file_handle = open(file_name, 'r')
    return file_handle.read().strip()

def getBottom(inputString):
    # bottom program it the only one that isn't referenced by other programs

    # get a set of all the programs
    # program name is the part of the line before the first space
    programs = []
    for line in iter(inputString.splitlines()):
        programs.append(line.split()[0])

    for line in iter(inputString.splitlines()):
        # take the progams after ->
        if (line.find("->") != -1):
            rps = line.split("-> ")[1].split(", ")
            for rp in rps:
                if (rp in programs):
                    programs.remove(rp)

    return programs[0]

def getWeights(inputString):
    weights = []
    for line in iter(inputString.splitlines()):
        weights.append((line.split()[0], int(line.split("(")[1].split(")")[0])))

    print  weights
    return weights

def getTowerWeight(program, inputString, weights):
    # tower weight is the wieght of the base program
    # plus the weights of any programs it references

    return 0


class Test(unittest.TestCase):
    def test(self):
        inputString = """pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)"""
        self.assertEqual(getBottom(inputString),"tknk")
        self.assertEqual(getTowerWeight("ugml", getWeights(inputString), inputString),60)

print(getBottom(read_file("input.txt")))
