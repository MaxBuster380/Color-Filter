def matrix_create(lines,columns):
    """Creates a matrix of given lines and given columns

        Example :
            matrix_create(2,3)  ->  |	0	0	|
                                    |	0	0	|
                                    |	0	0	|

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
            M = |	1	4	|
                |	3	2	|
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
            M = |	1	4	|
                |	3	2	|
                
            matrix_set(M,2,2,6)
            
            M = |	1	4	|
                |	3	6	|

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
            M = |	1	4	|
                |	3	2	|
                |	6	7	|
                
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
            M = |	1	4	|
                |	3	2	|
                |	6	7	|
                
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
            M = |	1	4	|
                |	3	2	|
                |	6	7	|

        IN
            M : Matrix
    """
    lineCount = matrix_lineCount(M)
    columnCount = matrix_columnCount(M)
    for cl in range(1,columnCount+1):
        line = "|\t"
        for ln in range(1,lineCount+1):
            number = str(matrix_get(M,ln,cl))[0:6]
            line = line + number + "\t"
        line = line + "|"
        print(line)

def matrix_add(A,B):
    """Adds two given matrices

        Example :
            A = 
            |	1	0	|
            |	0	2	|
            B = 
            |	2	4	|
            |	3	0	|
            S = matrix_add(A,B)
            S = 
            |	3	4	|
            |	3	2	|

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

def matrix_multNum(M,a):
    """Multiplies a given matrix by a given number

        Example :
            M = 
            |	1	0	|
            |	0	2	|
            a = 3
            
            P = matrix_multNum(M,a)
            
            P = 
            |	3	0	|
            |	0	6	|

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

def matrix_multMatrix(A,B):
    """Multiplies two given matrices

        Example :
            A = 
            |	1	0	|
            |	0	2	|
            B = 
            |	0	2	|
            |	2	0	|
            
            P = matrix_multMatrix(A,B)
            
            P = 
            |	0	2	|
            |	4	0	|

        IN
            A : Matrix
            B : Matrix
        OUT
            Matrix, product of A and B
    """
