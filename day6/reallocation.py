import unittest
from sets import Set

def reallocate(banks):
    # find the bank with the most allocated blocks
    # for a tie, lowest wins
    numberOfBanks = len(banks)
    blocksToDistribute = max(banks)
    biggestBank = banks.index(blocksToDistribute)
    banks[biggestBank] = 0

    # redistribute the blocks one at a time, starting with tne next banks
    for i in range(0, blocksToDistribute):
      index  = (biggestBank + 1 + i) %  numberOfBanks
      banks[index] += 1

    return banks

# Part 1 Keep reallocating until we see the same arrangement again
# Use a set to track unique values
def countReallocations(banks):
    sum = 0
    banksAsString = None
    allocations = Set()
    while (banksAsString not in allocations):
        allocations.add(banksAsString)
        banks = reallocate(banks)
        banksAsString = banksToString(banks)
        sum += 1

    return sum


# Keep reallocation until we see the same arrangement again
# and return the size of the loop - the distance between the
# duplicate allocations.
# Part 1 is a subset of Part 2 - so we can return both values here.
def measureLoopSize(banks):
    sum = 0

    # The point at which we find any of the values is relevant, so
    # store these values in a dictionary
    dic = {}
    while True:
        dic[banksToString(banks)] = sum
        banks = reallocate(banks)
        banksAsString = banksToString(banks)
        sum += 1
        if (banksAsString in dic):
            return (sum, sum - int(dic[banksAsString]))

def banksToString(banks):
    return ''.join(str(i) for i in banks)

print countReallocations([14,0,15,12,11,11,3,5,1,6,8,4,9,1,8,4])
print measureLoopSize([14,0,15,12,11,11,3,5,1,6,8,4,9,1,8,4])

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(measureLoopSize([0,2,7,0])[1],4)
        self.assertEqual(countReallocations([0,2,7,0]),5)
