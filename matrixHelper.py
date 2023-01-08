def matrix_create(lines,columns):
    """Creates a matrix of given lines and given columns

        Example :
            matrix_create(2,3)  ->  | 0	0 0 |
                                    | 0	0 0 |

        IN
            lines : Integer, number of lines
            columns : Integer, number of columns
        OUT
            Matrix
    """
    return [[0 for j in range(columns)] for i in range(lines)]

def matrix_get(M,line,column):
    """Gets a value of the given matrix on the given coordinates

        Example :
            M = | 1 4 |
                | 3 2 |
            matrix_get(M,1,2)  ->  4

        IN
            M : Matrix, source of the output
            line : Integer, line of the output value
            column : Integer, column of the output value
        OUT
            Number, value of the matrix M on (line,column)
    """
    return M[line-1][column-1]

def matrix_set(M,line,column,val):
    """Sets a value of the given matrix on the given coordinates

        Example :
            M = | 1 4 |
                | 3 2 |
                
            matrix_set(M,2,2,6)
            
            M = | 1 4 |
                | 3 6 |

        IN
            M : Matrix, source of the output
            line : Integer, line of the changed value
            column : Integer, column of the changed value
            val : Number, new value
    """
    M[line-1][column-1] = val

def matrix_lineCount(M):
    """Gets the number of lines on the given matrix

        Example :
            M = | 1 4 |
                | 3 2 |
                | 6 7 |
                
            matrix_lineCount(M)  ->  3

        IN
            M : Matrix
        OUT
            Integer, number of lines on the matrix
    """
    return len(M)

def matrix_columnCount(M):
    """Gets the number of columns on the given matrix

        Example :
            M = | 1 4 |
                | 3 2 |
                | 6 7 |
                
            matrix_lineCount(M)  ->  2

        IN
            M : Matrix
        OUT
            Integer, number of columns on the matrix
    """
    return len(M[0])

def matrix_print(M):
    """Displays the given matrix

        Example :
            matrix_print(M)
            M = | 1 4 |
                | 3 2 |
                | 6 7 |

        IN
            M : Matrix
    """
    lineCount = matrix_lineCount(M)
    columnCount = matrix_columnCount(M)
    for ln in range(1,lineCount+1):
        line = "|\t"
        for cl in range(1,columnCount+1):
            number = str(matrix_get(M,ln,cl))[0:6]
            line = line + number + "\t"
        line = line + "|"
        print(line)

def matrix_add(A,B):
    """Adds two given matrices

        Example :
            A = 
            | 1 0 |
            | 0 2 |
            B = 
            | 2 4 |
            | 3 0 |
            S = matrix_add(A,B)
            S = 
            | 3 4 |
            | 3 2 |

        IN
            A : Matrix, same size as B
            B : Matrix, same size as A
        OUT
            Matrix, sum of A and B
    """
    A_lineCount = matrix_lineCount(A)
    A_columnCount = matrix_columnCount(A)
    B_lineCount = matrix_lineCount(B)
    B_columnCount = matrix_columnCount(B)

    #Can only add matrices if they have the same size
    if (A_lineCount != B_lineCount or A_columnCount != B_columnCount):
        return 0

    res = matrix_create(A_lineCount, A_columnCount)
    for ln in range(1,A_lineCount+1):
        for cl in range(1,A_columnCount+1):
            val = matrix_get(A,ln,cl) + matrix_get(B,ln,cl)
            matrix_set(res,ln,cl,val)
    return res

def multNum(M,a):
    """Multiplies a given matrix by a given number

        Example :
            M = 
            | 1 0 |
            | 0 2 |
            a = 3
            
            P = matrix_multNum(M,a)
            
            P = 
            | 3 0 |
            | 0 6 |

        IN
            M : Matrix
            a : Number, factor 
        OUT
            Matrix, product of M and a
    """
    lineCount = matrix_lineCount(M)
    columnCount = matrix_columnCount(M)
    res = matrix_create(lineCount, columnCount)
    for ln in range(1,lineCount+1):
        for cl in range(1,columnCount+1):
            val = matrix_get(M,ln,cl) * a
            matrix_set(res,ln,cl,val)
    return res

def matrix_getLine(M,line):
    """Gets the line of a given matrix

        Example :
            M = 
            | 1 3 |
            | 0 2 |

            matrix_getLine(M,2)  ->  [0,2]

        IN
            M : Matrix, source
            line: Integer, line to get
        OUT
            List of integers, line found

    """
    return M[line-1]

def matrix_getColumn(M,column):
    """Gets the column of a given matrix

        Example :
            M = 
            | 1	3 |
            | 0	2 |

            matrix_getColumn(M,1)  ->  [1,0]

        IN
            M : Matrix, source
            column: Integer, column to get
        OUT
            List of integers, column found
    """

    lineCount = matrix_lineCount(M)
    columnCount = matrix_columnCount(M)
    res = [0 for i in range(lineCount)]
    for i in range(1,lineCount+1):
        val = matrix_get(M,i,column)
        res[i-1] = val
    return res

def multLineMatrices(A,B):
    """Multiplies two lists as if they were line matrices

        Example :
        A = [1,2]
        B = [3,7]
        multLineMatrices(A,B)  ->  17

        IN
            A : List of numbers
            B : List of numbers
        OUT
            Number, product
    """
    res = 0
    lenA = len(A)
    for i in range(lenA):
        res = res + A[i] * B[i]
    return res

def multMatrix(A,B):
    """Multiplies two given matrices

        Example :
            A = 
            | 1	0 |
            | 0	2 |
            B = 
            | 0	2 |
            | 2	0 |
            
            P = matrix_multMatrix(A,B)
            
            P = 
            | 0 2 |
            | 4 0 |

        IN
            A : Matrix
            B : Matrix
        OUT
            Matrix, product of A and B
    """
    A_columnCount = matrix_columnCount(A)
    B_lineCount = matrix_lineCount(B)

    if (A_columnCount != B_lineCount):
        return 0
    
    A_lineCount = matrix_lineCount(A)
    B_columnCount = matrix_columnCount(B)
    
    res = matrix_create(A_lineCount, B_columnCount)
    for ln in range(1,A_lineCount+1):
        for cl in range(1,B_columnCount+1):
            aLine = matrix_getLine(A,ln)
            bColumn = matrix_getColumn(B,cl)
            val = multLineMatrices(aLine, bColumn)
            
            matrix_set(res,ln,cl,val)
    return res

def matrix_isMatrix(M):
    """Tests if the given value is of matrix type

        OUT
            Boolean, if M is a matrix
    """
    #If the base type is a list
    if (type(M) != list):
        return False

    #If the subtypes are lists
    foundNotList = False
    i = 0
    lenM = len(M)
    while (i<lenM and not foundNotList):
        foundNotList = type(M[i]) != list
        i += 1
    if (foundNotList):
        return False

    #If all sublists are of the same size
    foundDiffSize = False
    i = 0
    sizeFirst = len(M[0])
    while (i<lenM and not foundDiffSize):
        foundDiffSize = len(M[i]) != sizeFirst
        i += 1
    if (foundDiffSize):
        return False

    #If all sublists contain only numbers
    foundNotNumber = False
    i = 0
    lenSubList = sizeFirst
    while(i<lenM and not foundNotNumber):
        j = 0
        while(j<lenSubList and not foundNotNumber):
            foundNotNumber = type(M[i][j]) != int and type(M[i][j]) != float
            j += 1
        i += 1
    if (foundNotNumber):
        return False
    
    #If it passed all tests, it is a matrix
    return True

def matrix_mult(A,B):
    """Returns the product of A and B
        Does a matrix multiplication if B is a matrix
        Does a numerical multiplication if B is a number

        IN
            A : Matrix
            B : Matrix OR Number
        OUT
            Matrix OR Number, B's type
    """
    if (type(B) == int or type(B) == float):
        return multNum(A,B)
    else:
        return multMatrix(A,B)

def matrix_identity(n):
    """Returns the identity matrix of size n,n

        Example :
                                    | 1 0 0 |
            matrix_identity(3)  ->  | 0 1 0 |
                                    | 0 0 1 |

        IN
            n : Integer, size of the matrix
        OUT
            Matrix, identity matrix of size n,n
    """
    res = matrix_create(n,n)
    for i in range(1,n+1):
        matrix_set(res,i,i,1)
    return res

def matrix_getSubMatrix(M,lineBase):
    """Returns the submatrix required for determinant calculation

        Example :
                |	1	2	3	|
            M = |	4	5	6	|
                |	7	8	9	|

            matrix_getSubMatrix(M,2)  ->  |	2	3	|
                                          |	8	9	|
            
        IN
            M, square matrix
            lineBase, integer, line of the submatrix
        OUT
            Matrix, sub matrix, square matrix

    """
    linesM = matrix_lineCount(M)
    linesRes = linesM - 1
    res = matrix_create(linesRes,linesRes)

    correctLine = 1
    for line in range(1,linesM+1):
        if (line != lineBase):
            for column in range(2,linesM+1):
                val = matrix_get(M,line,column)
                matrix_set(res,correctLine,column-1,val)
            
            correctLine += 1
    return res

def matrix_det(M):
    """Returns the determinant of the given square matrix

        Example :
                |	1	2	3	|
            M = |	0	2	4	|
                |	0	0	5	|

            matrix_det(M)  ->  10
            
        IN
            M, square matrix
        OUT
            Number, the determinant of M
    """
    lineCount = matrix_lineCount(M)
    if (lineCount != matrix_columnCount(M)):
        return None

    if (lineCount == 2):
        a = matrix_get(M,1,1)
        b = matrix_get(M,1,2)
        c = matrix_get(M,2,1)
        d = matrix_get(M,2,2)

        return a*d-b*c

    res = 0
    for line in range(1,lineCount+1):
        value = matrix_get(M,line,1)
        if (value != 0):
            sign = (-1)**(line-1)
            subMatrix = matrix_getSubMatrix(M, line)
            subDet = matrix_det(subMatrix)
            
            res = res + sign * value * subDet
    return res
