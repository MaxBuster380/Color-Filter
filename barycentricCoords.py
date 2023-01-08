from matrixHelper import *

def getTetrahedronArea(tetrahedron):
    """Returns the area of the given tretrahedron

        Example :
            points = [(0,0,0),(1,0,1),(0,1,1),(2,2,2)]
            getTetrahedronArea(points)  ->  0.333...
            
        IN
            tetrahedron, Array of tuples of 3 numbers, vertices of the tetrahedron
        OUT
            Number, Area of the given tetrahedron

    """
    #https://www.had2know.org/academics/tetrahedron-volume-4-vertices.html
    M = matrix_create(4,4)
    for i in range(4):
        point = tetrahedron[i]
        matrix_set(M,1,i+1,point[0])
        matrix_set(M,2,i+1,point[1])
        matrix_set(M,3,i+1,point[2])
        matrix_set(M,4,i+1,1)
    #matrix_print(M)
        
    return 1.0/6.0 * abs(matrix_det(M))  

def filterOutArray(array, value):
    """Returns a copy of the array with the given value filtered out.

        Example :
            array = [1,2,2,3,1]
            filterOutArray(array,1)  ->  [2,2,3]

        IN
            array, Array with any values
            value, Value to filter out of the array
        OUT
            Array
    """
    return [array[i] for i in range(len(array)) if array[i] != value]

def getBarycentricCoordinates(tetrahedron, point):
    """Returns the barycentric coordinates of a given point on a given tetrahedron

        Example :
            t = [(1,0,0),(0,1,0),(0,0,0),(0,0,1)]
            point = (0.5, 0.5, 0)
            getBarycentricCoordinates(t, point)  ->  [0.5, 0.5, 0, 0]

        IN
            tetrahedron, Array of 4 tuples of 3 numbers
            point, Tuple of 3 numbers
        OUT
            Array of numbers, influence of each tetrahedron vertice
    """
    res = []
    tetrahedronArea = getTetrahedronArea(tetrahedron)
    for i in range(0,4):
        vertice = tetrahedron[i]
        
        innerTTHD = filterOutArray(tetrahedron,vertice)
        innerTTHD.append(point)

        innerArea = getTetrahedronArea(innerTTHD)

        influence = innerArea/tetrahedronArea

        res.append(influence)
    return res

def isPointInsideTetrahedron(tetrahedron, point):
    """Returns true if the given point is inside the given tetrahedron

        Example :
            t = [(1,0,0),(0,1,0),(0,0,0),(0,0,1)]
            point = (0.25, 0.25, 0.25)

            isPointInsideTetrahedron(t, point)  ->  True

        IN
            tetrahedron, Array of 4 tuples of 3 numbers
            point, Tuple of 3 numbers
        OUT
            Boolean
    """
    coords = getBarycentricCoordinates(tetrahedron, point)
    return (coords[0] + coords[1] + coords[2] + coords[3]) == 1
