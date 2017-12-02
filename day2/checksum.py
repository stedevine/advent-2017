import StringIO
import unittest
import sys

def read_file(file_name):
    """Helper function, read file return contents as string"""
    file_handle = open(file_name, 'r')
    return file_handle.read().strip()

def getChecksum(inputString):
# Check sum is the total of the differences between the max and min value on each
# line of the file
    sum = 0

    buf = StringIO.StringIO(inputString)
    line = buf.readline()
    while (line):
        lineItems = line.split()
        length = len(lineItems)
        maxForLine = 0
        minForLine = sys.maxint
        for i in range (0, length):
            value = int(lineItems[i])
            if (value > maxForLine):
                maxForLine = value
            if (value < minForLine):
                minForLine = value
        sum += maxForLine - minForLine
        line= buf.readline()

    return sum


def getChecksum2(inputString):
#Checksum is the total of the division of the only 2 numbers per line which evenly divide
    sum = 0
    buf = StringIO.StringIO(inputString)
    line = buf.readline()
    while (line):
        lineItems = line.split()
        length = len(lineItems)
        for i in range (0, length):
         # For each line check every entry against every other
         numerator = int(lineItems[i])
         for j in (range (0, length)):
            denominator = int(lineItems[j])
            # Check they divide evenly (and aren't the same number)
            if (numerator != denominator and numerator % denominator == 0):
                sum += numerator / denominator
                # there's only one pair that divide evenly so exit here.
                break
        line = buf.readline()
    return sum

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
