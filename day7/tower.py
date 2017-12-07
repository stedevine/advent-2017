import unittest
from sets import Set
from collections import Counter
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

# Break the input into key (program) and value (weight + other input)

def getDictionary(inputString):
    dic = {}
    for line in iter(inputString.splitlines()):
        s = line.split(" (")
        dic[s[0]] = "(" + s[1]

    #print dic
    return dic

def getProgramWeight(program, dic):
    return int(dic[program].split("(")[1].split(")")[0])

def getTowerWeight(program, dic):
    if (dic[program].find("->") == -1):
        return getProgramWeight(program, dic)

    sum = getProgramWeight(program, dic)
    for p in getSubTowerBases(program, dic):
        sum += getTowerWeight(p, dic)

    return sum

def getSubTowerBases(program, dic):
    return dic[program].split("-> ")[1].split(", ")

"""
def getWeights(inputString):
    weights = []
    for line in iter(inputString.splitlines()):
        weights.append((line.split()[0], int(line.split("(")[1].split(")")[0])))

    print  weights
    return weights

def getSubtowerWeight(line, input):
    if (line.find("->") == -1):
        return (line.split()[0], int(line.split("(")[1].split(")")[0]))

    weight = 0


    line


def getTowerWeight(program, inputString):
    # tower weight is the wieght of the base program
    # plus the weights of any programs it references



    return 0

"""


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
        #self.assertEqual(getDictionary(inputString),"")
        self.assertEqual(getTowerWeight("ugml", getDictionary(inputString)),251)
        self.assertEqual(getTowerWeight("tknk", getDictionary(inputString)),251)
i = read_file("input.txt")
print(getBottom(i))

d = getDictionary(i)
print(getTowerWeight(getBottom(i),d))

j = """pbga (66)
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
dj = getDictionary(j)

a={}
for p in getSubTowerBases(getBottom(j), dj):
    a[p] = str(getTowerWeight(p, dj))
    print "p: " + p + " " + str(a[p])

print a
val_counter = Counter(a.itervalues())
unbalanced = [k for k, v in a.iteritems() if val_counter[v] == 1][0]

print unbalanced
