# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 00:33:22 2019

@author: Alonso
"""

class soup:
    def __init__(self, mayhem, words):
        """
        This is only the parameter input of the class.
        Parameters are as follows:
        mayhem: data type-list (of lists)
                definition-a list of list which is the main body of the soup
        words: data type-list (of strings)
               definition-the list of the words on the soup
        """
        self.may = mayhem
        self.wo = words
        
    
    def __foo(self):
        """
        It creates a mimicry of the soup consistant of zeros.
        It uses no non-inited parameters.
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
        for e in self.may:
            k.append([])
            for m in e:
                e.append(0)
        return k
            
    def __twist(self):
        """
        It creates a mirrored version of the soup, used when reading
        on the opposite direction of the usual.
        It uses no non-inited parameters.
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
        k = self.may
        for e in k:
            e = e.reverse()
        return k
        
    def __trans(self):
        """
        It creates a transposed version (element [a][b] is the element [b][a])
        of the soup, used when reading on a vertical fashion.
        It 
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
        k = self.__foo()
        for e in range(len(k)):
            for f in range(len(k)[e]):
                k[e][f] = self.may[f][e]
        return k
        
    def __scramble(self):
        """
        MAIN:
        It creates a horizontal-to-digonal version of the soup, given that we
        can organize the elements of a matrix (which is a list of lists)
        using their subindexes and modular arithmetics.
        It uses no non-inited parametes.
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
        lis, ig = Zn(max(len(self.may), len(self.may)[0]))
        
        k = -1
        for e in ig:
            k += 1
            for i in range(len(self.may)):
                for j in range(len(self.may[0])):
                    if i-j == e:
                        lis[k].append(self.may[i][j])
        return lis
    def __reorg(self, dirhor, ver, mode):
        """
        It modifies the original soup so it can be read in any direction
        we want
        It uses the following parameters:
            dirhor: data type-string
                    definition-whether it goes in the usual 
                               reading way or not
            ver: data type-boolean
                 definition-whether it is read in a vertical fashion or not
            mode: data type-string
                  definition-wheter it is read in a diagonal fashion or not
        It returns k, which is a result of applying any of the __twist, __trans
        or __scramble functions to the original soup in any combination of them
                
        """
        k = self.may
        
        if dirhor != "stgh":
            k = self.__twist()
        if ver != True:
            k = self.__trans(k)
        if mode == "diag":
            k = self.__scramble()
            
        return k
        
    def __search(self):
        """
        MAIN:
        It checks on every word if it is or not on the soup.
        It uses no non-inited parameters.
        
        Given our list of words, let's say we found that the 1st, 4th and 5th
        ones aren't present whereas the 2nd, 3rd and 6th are
        
        It returns ret, a list of bools, which would be on the aforementioned
        example [False, True, True, False, False, True]
        
        strsearch SUBFUNCTION:
        It checks if a given string is found within a string list
        It uses the following parameters:
            st: data type-string
                definition-the string we are going to check 
                           not necessarily listed
                
            lis: data type-list
                 definition-the list we are going to compare our string
                            with
        It returns check, a boolean which says if we found the word
        """
        def strsearch(lis, st):
            st = list(st)
            k = lis
            check = False
            for e in k:
                if k != st[0] and len(k) >= len(st):
                    k.pop()
                elif len(k) >= len(st):
                    k0 = k
                    while len(k0) != len(st):
                        st.pop(len(st)-1)
                    if k0 == st:
                        check = True
            return check
        modes = [["stgh","reverse"],[True, False],["norm", "diag"]]
        srch = []
        for i in modes[0]:
            for j in modes[1]:
                for k in modes[2]:
                    mod = self.__reorg(i,j,k)
                    for e in mod:
                        srch.append(e)
        ret = []
        for e in range(len(self.wo)):
            for f in range(len(srch)):
                if strsearch(srch[f], self.wo[e]) == True and len(ret) < e + 1:
                    ret.append(True)
                elif len(ret) < e + 1 and f == len(srch) - 1:
                    ret.append(False)
        return ret
        
    def check(self):
        """
        It checks if every word is to be found on our soup.
        It uses no non-inited parameters.
        It returns a boolean which tells us if they're all present (True)
        or not (False)
        """
        d = self.__search()
        if d.count(True) == len(self.wo):
            return True
        else:
            return False
            
    @staticmethod
    def loadsoup(soupfile, wordsfile):
        """
        A static method which returns an object of the soup class.
        It uses the following parameters:
            soupfile: data type-txt file
                      definition-a txt file containing the files of the soup
                      in case the characters aren't separated from each other,
                      it works too
            wordsfile: data type-txt file
                       definition-a txt file containing the words 
                       to be contained on the soup. It doesn't matter if 
                       it's written in a sigle line or in many
                       
        """
        sfile = open(soupfile, 'r')
        wfile = open(wordsfile, 'r')
        k = sfile.readlines()
        d = wfile.readlines()
        me = []
        for ty in k:
            if len(ty) == 1:
                me.append(list(ty))
            else:
                me.append(ty)
        re = []        
        if len(d) != 1:
            for e in d[0].split(" "):
                re.append(e)
        else:
            re = d
        return soup(me, re)