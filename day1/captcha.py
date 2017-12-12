import unittest

def read_file(file_name):
    """Helper function, read file return contents as string"""
    file_handle = open(file_name, 'r')
    return file_handle.read().strip()
    
def getSum(inputString):
    sum = 0
    #if two consecutive characters match sum them
    for i in range (1, len(inputString)):
        if (inputString[i-1] == inputString[i]):
            sum += (int(inputString[i-1]))

    # special case for matching first and last chars in circular buffer
    if (inputString[0] == inputString[len(inputString)-1]):
        sum += (int(inputString[0]))
    return sum

def getSum2(inputString):
    sum = 0
    length = len(inputString)
    # If two characters separated by half the list match sum them
    for i in range (0, length):
        offset = (i + length/2) % length
        if (inputString[i] == inputString[offset]):
            sum += int(inputString[i])
    return sum

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(getSum("1122"),3)
        self.assertEqual(getSum("1111"),4)
        self.assertEqual(getSum("1234"),0)
        self.assertEqual(getSum("9121212129"),9)

        self.assertEqual(getSum2("1212"),6)
        self.assertEqual(getSum2("1221"),0)
        self.assertEqual(getSum2("123425"),4)
        self.assertEqual(getSum2("123123"),12)
        self.assertEqual(getSum2("12131415"),4)

print(getSum(read_file("input.txt")))
print(getSum2(read_file("input.txt")))
