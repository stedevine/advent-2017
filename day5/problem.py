import unittest

def read_file(file_name):
    """Helper function, read file return contents as string"""
    file_handle = open(file_name, 'r')
    return file_handle.read().strip()

def countStepsToExit(inputString):
    sum = 0
    return sum


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(countStepsToExit("""0
3
0
1
-3"""),5)

#print(getSum(read_file("input.txt")))
#print(getSum2(read_file("input.txt")))
