# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 17:56:20 2019

@author: Alonso
"""

def foo(matrix):
    """
    It creates a mimicry of the matrix parameter consistant of zeros.
    It uses the follwing parameters:
        Matrix: data type-list (of lists)
                definition-the matrix we are going to work with
    How it works:
        given a list of lists: [[a00,a01,--,a0n],
                                [a10,a11,--,a1n],
                                [--------------],
                                [am0,am1,--,amn]]
            it returns another one in the like, k:
                [[0,0,--,0],
                 [0,0,--,0],
                 [--------],
                 [0,0,--,0]]
        """
    k = []
    for e in matrix:
        k.append([])
        for m in e:
            e.append(0)
    return k
            
def twist(matrix):
    """
    It creates a mirrored version of the soup, used when reading
    on the opposite direction of the usual.
    It uses the follwing parameters:
        Matrix: data type-list (of lists)
                definition-the matrix we are going to work with
    How it works:
        given a list of lists: [[a00,a01,--,a0n],
                                [a10,a11,--,a1n],
                                [--------------],
                                [am0,am1,--,amn]]
        it returns another one in the like, k:
            [[a0n,a0(n-1),--,a00],
              [a1n,a1(n-1),--,a10],
              [------------------],
              [amn,am(n-1),--,am0]]
    """
    k = matrix
    for e in k:
        e = e.reverse()
    return k
    
def trans(matrix):
    """
    It creates a transposed version (element [a][b] is the element [b][a])
    of the soup, used when reading on a vertical fashion.
    It uses the follwing parameters:
        Matrix: data type-list (of lists)
                definition-the matrix we are going to work with
    How it works:
        given a list of lists: [[a00,a01,--,a0n],
                                [a10,a11,--,a1n],
                                [--------------],
                                [am0,am1,--,amn]]
        it returns another one in the like, k:
            [[a00,a10,--,am0],
            [a01,a11,--,am1],
            [--------------],
            [a0n,a1n,--,amn]
    """
    k = foo(matrix)
    for e in range(len(k)):
        for f in range(len(k)[e]):
            k[e][f] = matrix[f][e]
    return k
        
def scramble(matrix):
    """
    MAIN:
    It creates a horizontal-to-digonal version of the soup, given that we
    can organize the elements of a matrix (which is a list of lists)
    using their subindexes and modular arithmetics.
    It uses the follwing parameters:
        Matrix: data type-list (of lists)
                definition-the matrix we are going to work with
    How it works:
        given a list of lists: [[a00,a01,--,a0n],
                                [a10,a11,--,a1n],
                                [--------------],
                                [am0,am1,--,amn]]
        given that the organization numbers are
        [[0,-1,-2,-3,--,-n],
         [1, 0,-1,-2,--,1-n],
         [2, 1, 0,-1,--,2-n],
         [-----------------],
         [m,m-1,m-2,-----,0]]
        which returns k, a list of m + n + 1 elements organized by the 
        diagonal number
            
    Zn SUBFUNCTION:
    It creates an empty list and a list of numbers which is the 
    subgroup Zn on modular arithmetics
    It uses the following parameter:
        number: data type-int
                definition: an integer number
                
    It returns lis, and empty list, and gr, a list with the numbers from 
    (-number)+1 to (number)-1
    """
    def Zn(number):
        z = int(number)
        lis = []
        gr = []
        for e in range(-z+1, z-2, -1):
            z.append([])
            gr.append(e)
        return lis, gr
    lis, ig = Zn(max(len(matrix), len(matrix)[0]))
    
    k = -1
    for e in ig:
        k += 1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i-j == e:
                    lis[k].append(matrix[i][j])
    return lis