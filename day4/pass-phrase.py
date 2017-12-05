import unittest
from collections import Counter

def read_file(file_name):
    """Helper function, read file return contents as string"""
    file_handle = open(file_name, 'r')
    return file_handle.read().strip()

# Phrases must not contain instances of the same word
def isValidPhrase(phrase):
    # Break the sting into a list of words and count them
    # If there is more than one instance of a word, phrase is invalid
    counter = Counter(phrase.split())
    for element in counter:
        if counter[element] > 1 :
            return False

    return True

# Phrases must not contain words that are anagrams of each other
def isValidNoAnagrams(inputString):
    # Expose any anagrams in the phrase:
    # Split the phrase into words and sort the letters in each word
    # Join the sorted letters back into words, join the words back into a ' ' spaced string
    exposeAnagrams = ' '.join([''.join(sorted(x)) for x in inputString.split()])
    # Use the above method to check if there are multiple instances of the same word
    return isValidPhrase(exposeAnagrams)

def countValidPassPhrases(validationFunction, inputString):
    sum = 0
    for line in iter(inputString.splitlines()):
        if validationFunction(line):
            sum += 1
    return sum

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(isValidPhrase("aa bb cc dd ee"),True)
        self.assertEqual(isValidPhrase("aa bb cc dd aa"),False)
        self.assertEqual(isValidPhrase("aa bb cc dd aaa"),True)

        self.assertEqual(isValidNoAnagrams("abcde fghij"),True)
        self.assertEqual(isValidNoAnagrams("abcde xyz ecdab"),False)
        self.assertEqual(isValidNoAnagrams("a ab abc abd abf abj"),True)
        self.assertEqual(isValidNoAnagrams("iiii oiii ooii oooi oooo"),True)
        self.assertEqual(isValidNoAnagrams("oiii ioii iioi iiio"),False)


print(countValidPassPhrases(lambda phrase: isValidPhrase(phrase), read_file("input.txt")))
print(countValidPassPhrases(lambda phrase: isValidNoAnagrams(phrase), read_file("input.txt")))
