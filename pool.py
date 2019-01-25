# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 00:33:22 2019

@author: Alonso
"""

class soup:
    def __init__(self, mayhem, words):
        self.may = mayhem
        self.wo = words
        
    
    def __foo(self):
        k = []
        for e in self.may:
            k.append([])
            for m in e:
                e.append(0)
        return k
            
    def __twist(self): #use when searching from right to left
         k = self.may
         for e in k:
             e = e.reverse()
         return k
        
    def __trans(self, matrix): #use when searching in vertical
        k = self.__foo()
        for e in range(len(k)):
            for f in range(len(k)[e]):
                k[e][f] = self.may[f][e]
        return k
        
    def __scramble(self): #use when searching in diagonal
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
        k = self.may
        
        if dirhor != "stgh":
            k = self.__twist()
                   
        if ver != True:
            k = self.__trans(k)
        if mode == "diag":
            k = self.__scramble()
            
        return k
        
    def search(self):
        def strsearch(lis, st):
            st = list(st)
            k = lis
            check = False
            for e in k:
                if k != st[0]:
                    k.pop()
                else:
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
        d = self.search
        if d.count(True) == len(self.wo):
            return True
        else:
            return False
            
    @staticmethod
    def loadsoup(soupfile, wordsfile):
        sfile = open(soupfile, 'r')
        wfile = open(wordsfile, 'r')
        k = sfile.readlines()
        d = wfile.readlines()
        re = []
        if len(d) != 1:
            for e in d[0]:
                re.append(e)
        else:
            re = d
        return soup(k, re)