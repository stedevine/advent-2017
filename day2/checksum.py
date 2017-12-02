import unittest
import sys

def read_file(file_name):
    """Helper function, read file return contents as string"""
    file_handle = open(file_name, 'r')
    return file_handle.read().strip()

def getChecksum(inputString):
# Checksum is the total of the differences between the max and min value on each
# line of the file
    sum = 0
    # Iterate over the lines in the string
    for line in iter(inputString.splitlines()):
        maxForLine = 0
        minForLine = sys.maxint
        # iterate over the values in the line
        for value in [ int(v) for v in line.split()]:
            if (value > maxForLine):
                maxForLine = value
            if (value < minForLine):
                minForLine = value
        sum += maxForLine - minForLine
    return sum


def getChecksum2(inputString):
# Checksum is the sum of the division of the only 2 numbers per line which evenly divide
    sum = 0
    # Iterate over the lines in the string
    for line in iter(inputString.splitlines()):
        # Turn each line into an array of ints
        values = [ int(v) for v in line.split()]
        sum += checkValues(values)
    return sum

def checkValues(values):
    # Check every value against every other
    for numerator in values:
        for denominator in values:
            if (numerator != denominator and numerator % denominator == 0):
                # There is one pair of numbers per line for which this is true, return when we find it
                return (numerator / denominator)



class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(getChecksum("""5 1 9 5
7   5 3
2 4   6 8"""),18)
        self.assertEqual(getChecksum2("""5 9 2 8
9 4 7 3
3 8 6 5"""),9)


print(getChecksum(read_file("input.txt")))
print(getChecksum2(read_file("input.txt")))
