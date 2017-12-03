# Inner shell       1   1^2
# Second shell  2   9   3^2
# Third shell   10  25  5^2
# Fourth shell 26  49  7^2

# The total taxicab distance to move will be the distance from the shell to the
# center of the grid plus the distance of the target value to a number that is horizontally
# or veritcally inline with the center.
# Tactic:
# Find the shell for the target number
# On this shell there are four positions from which it is possible to move horizontally or veritcally
# to the center - find them and work out which is closest to the target number

import unittest

def getDistanceToCenter(inputValue):
    shell = getShell(inputValue)
    lower = ((((shell-1)*2)-1)**2) + 1
    upper = (((shell)*2)-1)**2

    # On each side of the shell there is
    # a center (from which it is possible to travel
    # to the center of the grid moving only horizontally or veritcally)

    # How far is the inputValue from the closest center?
    c1 = lower + (((upper - lower)/4)/2)
    c2 = c1 + ((upper-lower)/4 + 1)
    c3 = c2 + ((upper-lower)/4 + 1)
    c4 = c3 + ((upper-lower)/4 + 1)
    distance_from_side_center = min([abs(inputValue-c1),abs(inputValue-c2),abs(inputValue-c3),abs(inputValue-c4)])
    # Total distance to the center is this plus the number of steps to get from the shell to the center
    return distance_from_side_center + (shell-1)

def getShell(inputValue):
    # create a tuple that holds the shell and the maximum
    # value in that shell
    for tup in [ (s, (((s*2)-1)**2)) for s in range(1,500)]:
        if inputValue <= tup[1]:
            return tup[0]

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(getShell(1),1)
        self.assertEqual(getShell(2),2)
        self.assertEqual(getShell(8),2)
        self.assertEqual(getShell(9),2)

        self.assertEqual(getDistanceToCenter(12),3)
        self.assertEqual(getDistanceToCenter(23),2)
        self.assertEqual(getDistanceToCenter(1024),31)
        self.assertEqual(getDistanceToCenter(1),0)

print(getDistanceToCenter(368078))
