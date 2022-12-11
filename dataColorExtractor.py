import re

def treatLine(line):
    """Takes a string <line> of format 'rrr\tggg\tbbb\trrr\tggg\tbbb\n'
        and parses it into a tuple of tuples

        Example :
        '128 137 204 28 37 104' -> ((128,127,204),(28,37,104))"""
    match = re.match("^(\d+)\s(\d+)\s(\d+)\s(\d+)\s(\d+)\s(\d+)\s?$", line)
    r1 = int(match.group(1))
    g1 = int(match.group(2))
    b1 = int(match.group(3))
    r2 = int(match.group(4))
    g2 = int(match.group(5))
    b2 = int(match.group(6))
    return (r1,g1,b1),(r2,g2,b2)

def loadFile(path):
    """Creates an array of tuples of colors from a file <path>

        Example :

        file.txt
        1 2 3 4 5 6      [((1,2,3),(4,5,6)),
        7 8 9 1 2 3   ->  ((7,8,9),(1,2,3))]"""

    file = open(path, 'r')

    res = []

    line = file.readline()

    while(line):
        dataPoint = treatLine(line)
        res.append(dataPoint)

        line = file.readline()

    return res
