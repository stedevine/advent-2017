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

# Part 2: Grid gets more interesting
# Do we have to generate the grid?

#1
#2 1
#3  2 (1 + (1))
#4  4 (2 + (1 + 1))
#5  5 (4 + 1)
#6 10 (5 + (4 + 1))
#7 11 (10 + 1)
#8 23 (11 + (10 + 1))
#9 25 (23 + (1 + 1))
#10 26 (25 + (1))
#11 54 (26 + (25 + 1)+2)
#12 57

def getNeighborsIndices(inputIndex):
    shell = getShell(inputIndex)

    lower = ((((shell-1)*2)-1)**2) + 1
    upper = (((shell)*2)-1)**2
    tr = lower + ((upper-lower)/4)
    tl = tr + ((upper-lower)/4) + 1
    bl = tl + ((upper-lower)/4) + 1
    br = bl + ((upper-lower)/4) + 1
    print "tl " + str(tl)

    if (inputIndex == upper):
        print "bottom right"

    if (inputIndex == lower):
        print "bottom right + one"


    #if ((inputIndex > lower) and (lower < tr - 1)):
    #    print ("right side")
        # For shell > 2 Neighbors are previous + three values from right side of inner shell
        # For shell == 2 Neighbours are previous + center

    if (inputIndex == tr - 1):
        #Neighbors are inner shell's top right, inner shell's topright - 1 and previous index
      print ("top right - 1")

    if (inputIndex == tr):
        #Neighbors are inner shells top right and previous index
        return [inputIndex-1, getInnerShellIndex(shell-1, 'tr')]

    if (inputIndex == tl):
        #Neighbors are inner shells top left and previous index
        return [inputIndex-1, getInnerShellIndex(shell-1, 'tl')]

    if (inputIndex == bl):
        #Neighbors are inner shells bottom left and previous index
        return [inputIndex-1, getInnerShellIndex(shell-1, 'bl')]

    if (inputIndex == br):
        #Neighbors are inner shells bottom right left and previous index
        # and this shell's lowest index
        return [lower, inputIndex-1, getInnerShellIndex(shell-1, 'br')]



def getInnerShellIndex(shell, corner):
    lower = ((((shell-1)*2)-1)**2) + 1
    upper = (((shell)*2)-1)**2

    tr = lower + ((upper-lower)/4)
    tl = tr + ((upper-lower)/4) + 1
    bl = tl + ((upper-lower)/4) + 1
    br = bl + ((upper-lower)/4) + 1

    result = {
        'tr' : tr,
        'tl' : tl,
        'bl' : bl,
        'br' : br
        }[corner]
    return result

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

print(getNeighborsIndices(13))
print(getNeighborsIndices(17))
print(getNeighborsIndices(21))
print(getNeighborsIndices(25))


print(getDistanceToCenter(368078))
print(getInnerShellIndex(3,'tl'))
print(getInnerShellIndex(3,'tr'))
print(getInnerShellIndex(3,'bl'))
print(getInnerShellIndex(3,'br'))
