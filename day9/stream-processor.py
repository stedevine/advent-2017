import unittest

def read_file(file_name):
    """Helper function, read file return contents as string"""
    file_handle = open(file_name, 'r')
    return file_handle.read().strip()

def getScore(input):

    # a groups score depends on how deeply nested it is.
    depth = 0
    score = 0
    ignore = False
    ignoreCount = 0

    i = 0
    while(i < len(input)):
        c = input[i]

        if c == "!":
            # skip the next character
            i += 2
            continue

        if c == ">"  and ignore:
            # Flip the ignore state and move to the next character
            ignore = False
            i +=1
            continue

        elif c == '<'  and not ignore:
            # Flip the ignore state and move to the next character
            ignore = True
            i +=1
            continue

        elif c == '{' and not ignore:
            depth += 1

        elif c == '}' and not ignore:
            score += depth
            depth -= 1

        if ignore:
            ignoreCount += 1

        i += 1

    return (score, ignoreCount)


def countGarbage(input):
    count = 0

    return count

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(getScore("""{}""")[0], 1)
        self.assertEqual(getScore("""{{{}}}""")[0], 6)
        self.assertEqual(getScore("""{{},{}}""")[0], 5)
        self.assertEqual(getScore("""{{{},{},{{}}}}""")[0], 16)
        self.assertEqual(getScore("""{<a>,<a>,<a>,<a>}""")[0], 1)
        self.assertEqual(getScore("""{{<ab>},{<ab>},{<ab>},{<ab>}}""")[0],9)
        self.assertEqual(getScore("""{{<!!>},{<!!>},{<!!>},{<!!>}}""")[0],9)
        self.assertEqual(getScore("""{{<a!>},{<a!>},{<a!>},{<ab>}}""")[0],3)

        self.assertEqual(getScore("""<>""")[1],0)
        self.assertEqual(getScore("""<random characters>""")[1],17)
        self.assertEqual(getScore("""<<<<>""")[1], 3)
        self.assertEqual(getScore("""<{!>}>""")[1], 2)
        self.assertEqual(getScore("""<!!>""")[1], 0)
        self.assertEqual(getScore("""<!!!>>""")[1], 0)
        self.assertEqual(getScore("""<{o"i!a,<{i<a>""")[1], 10)

print(getScore(read_file("input.txt")))
