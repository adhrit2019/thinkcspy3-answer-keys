import sys

# Question 5
def add_vectors(u, v):
    """Returns a new list with the sums of the elements of lists u and v."""
    
    if len(u) == len(v):
        res = []
        for i in range(len(u)):
            res.append(u[i] + v[i])
            
        return res
    
    
# Question 6
def scalar_mult(s, v):
    """Returns the scalar multiple of s and v."""
    
    res = []
    for elem in v:
        res.append(elem * s)
        
    return res
    
    
# Question 7
def dot_product(u, v):
    """Takes two lists of numbers of the same length, and returns the sum of the products of the 
    corresponding elements of lists u and v."""
    
    if len(u) == len(v):
        res = 0
        
        for i in range(len(u)):
            res += u[i] * v[i]
            
        return res
    
    
# Question 8
def cross_product(u, v):
    """Returns the cross product of u and v."""
    
    if len(u) == len(v) and len(u) == 3:
        res = []
        for num in range(len(u)):
            if num == 0:
                matrix_u = u[1:]
                matrix_v = v[1:]
            elif num == 1:
                matrix_u = [u[0]] + [u[2]]
                matrix_v = [v[0]] + [v[2]]
            elif num == 2:
                matrix_u = u[:2]
                matrix_v = v[:2]
            
            matrix_v.reverse()
            com = 0
            
            for i in range(len(matrix_u)):
                com = (matrix_u[i] * matrix_v[i]) - com
                
            if num == 0 or num == 2:
                com *= -1
                
            res.append(com)
        
        return res
    

# The test function
def test(did_pass):
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        print("Test at line {0} passed.".format(linenum))
    else:
        print("Test at line {0} failed.".format(linenum))
        

def test_suite():
    # Tests of Question 5
    test(add_vectors([1, 1], [1, 1]) == [2, 2])
    test(add_vectors([1, 2], [1, 4]) == [2, 6])
    test(add_vectors([1, 2, 1], [1, 4, 3]) == [2, 6, 4])
    
    # Tests of Question 6
    test(scalar_mult(5, [1, 2]) == [5, 10])
    test(scalar_mult(3, [1, 0, -1]) == [3, 0, -3])
    test(scalar_mult(7, [3, 0, 5, 11, 2]) == [21, 0, 35, 77, 14])
    
    # Tests of Question 7
    test(dot_product([1, 1], [1, 1]) == 2)
    test(dot_product([1, 2], [1, 4]) == 9)
    test(dot_product([1, 2, 1], [1, 4, 3]) == 12)
    
    # Tests of Question 8
    test(cross_product([1, 1, 1], [2, 2, 2]) == [0, 0, 0])
    test(cross_product([1, 2, 3], [4, 5, 6]) == [-3, 6, -3])
    test(cross_product([1, 0, 1], [0, 1, 0]) == [-1, 0, 1])
    
test_suite()