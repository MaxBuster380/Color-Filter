from dataColorExtractor import *
from color import *

def averageColor(colorArray):
    """Given an array of colors <colorArray>, outputs the average

        Example :
        [(0,0,0),(255,255,255)]  ->  (127,127,127)

        IN
            colorArray : Array of colors (tuple of 3 [0,255] integers)
        OUT
            color (tuple of 3 [0,255] integers)
    """

    r = 0
    g = 0
    b = 0

    lenColorArray = len(colorArray)
    for i in range(lenColorArray):
        currentColor = colorArray[i]

        r = r + red(currentColor)
        g = g + green(currentColor)
        b = b + blue(currentColor)

    r = round(r / lenColorArray)
    g = round(g / lenColorArray)
    b = round(b / lenColorArray)

    return r,g,b

def getDuplicatesIndexes(array):
    """Given an array <array>, returns an array of arrays, where the inner arrays
        contain the indexes of <array> elements that are equal

        Example :
        [0,0,1,2,3,4,3,0]  ->  [[0,1,7],[2],[3],[4,6],[5]]

        IN
            array : Array of any values
        OUT
            Array of arrays of integers
    """
    
    res = []

    lenArray = len(array)
    treated = [False for i in range(lenArray)]

    def findDuplicates(i):
        """Finds the indexes of the values equal to the i-th value
            Adds them to the output array if more than 1 was found"""
        newElement = []
        for j in range(i, lenArray):
            if (array[i] == array[j]):
                newElement.append(j)
                treated[j] = True
        res.append(newElement)

    for i in range(lenArray-1):
        if (not treated[i]): #Don't attempt to create a new entry if it was treated previously
            findDuplicates(i)
    return res

def replaceIndexByValue(indexes, values):
    """Returns an array where the element of index i is the indexes[i]-th element of <values>

        Example :
        indexes = [1,2,2,4]
        values = ['a','b','c','d','e']  ->  ['b','c','c','e']

        IN
            indexes : Array of integers i, where 0 <= i < len(values)
            values : Array of any values
        OUT
            Array of any values"""

    res = []

    lenIndexes = len(indexes)
    for i in range(lenIndexes):
        newElement = values[indexes[i]]
        res.append(newElement)

    return res

def getColumn(table, columnNb):
    """Returns a column of the table

        Example :
        table = [[1,2,3],
                 [4,5,6],
                 [7,8,9]]  ->  [2,5,8]
        columnNb = 1

        IN
            table : Array of arrays of any values
            columnNb : Integer between 0 and the height of the table
        OUT
            Array of any values
    """

    res = []
    heightTable = len(table)
    for i in range(heightTable):
        res.append(table[i][columnNb])
    return res

def treatDuplicateColors(colorSet):
    """In a color set, for all input colors with multiple entries,
        averages the output color.

       Example :
       [((1,2,3),(40,20,10)),
        ((1,2,3),(0,0,0)),      [((1,2,3),(20,10,5)),
        ((4,5,6),(0,0,0))]  ->   ((4,5,6),(0,0,0))]

       IN
           colorSet : Array of tuples of 2 colors
       OUT
           Array of tuples of 2 colors
    """

    inputColors = getColumn(colorSet,0)
    outputColors = getColumn(colorSet,1)
    duplicates = getDuplicatesIndexes(inputColors)

    res = []

    def treatValue(i):
        index = duplicates[i][0]
        if (len(duplicates[i]) == 1):
            elt = (inputColors[index], outputColors[index])
            res.append(elt)
        else:
            sames = duplicates[i]
            colorsToAverage = replaceIndexByValue(sames,outputColors)
            average = averageColor(colorsToAverage)
            elt = (inputColors[index], average)
            res.append(elt)
            
    
    lenDuplicates = len(duplicates)
    for i in range(lenDuplicates):
        treatValue(i)
    return res
