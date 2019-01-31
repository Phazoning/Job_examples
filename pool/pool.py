# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 00:33:22 2019

@author: Alonso
"""
import sys
def initcheck():
    try:
        k0 = file.open("matmod.py", 'r')
    except:
        sys.path.append('/backup/')
        import matmodb as mat
    
    k1 = file.open("backup/matmod.py", 'r')
    if k0.readlines() == k1.readlines():
        import matmod as mat
    else:
        sys.path.append('/backup/')
        import matmodb as mat
        
initcheck()

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
            k = mat.twist(k)
        if ver != True:
            k = mat.trans(k)
        if mode == "diag":
            k = mat.scramble(k)
            
        return k
        
    def search(self):
        """
        MAIN:
        It checks on every word if it is or not on the soup.
        It uses no non-inited parameters.
        
        Given our list of words, let's say we found that the 1st, 4th and 5th
        ones aren't present whereas the 2nd, 3rd and 6th are
        
        It returns a boolean which tells us if they're all present (True)
        or not (False)
        
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
        if ret.count(True) == len(self.wo):
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
