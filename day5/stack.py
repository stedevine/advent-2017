import unittest

def read_file(file_name):
    """Helper function, read file return contents as string"""
    file_handle = open(file_name, 'r')
    return file_handle.read().strip()

def countStepsToExit(inputString, getNewStackValue):
    sum = 0
    # read lines into list
    stack = [int(x) for x in inputString.split()]
    # start at 0
    position = 0
    while (position >= 0 and position < len(stack)):
        sum += 1
        newPosition = position + stack[position]
        stack[position] = getNewStackValue(stack[position])
        position = newPosition
    return sum

def getNewStackValueProblem1(stackValue):
    return stackValue + 1

def getNewStackValueProblem2(stackValue):
    if (stackValue>=3):
        return stackValue - 1

    return stackValue + 1


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(countStepsToExit("""0
3
0
1
-3""", lambda stackValue: getNewStackValueProblem1(stackValue)),5)
        self.assertEqual(countStepsToExit("""0
3
0
1
-3""", lambda stackValue: getNewStackValueProblem2(stackValue)),10)

print(countStepsToExit(read_file("input.txt"), lambda stackValue: getNewStackValueProblem1(stackValue)))
print(countStepsToExit(read_file("input.txt"), lambda stackValue: getNewStackValueProblem2(stackValue)))
