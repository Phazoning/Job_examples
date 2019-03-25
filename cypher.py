# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 17:59:29 2019

@author: HP
"""
import random

class codebas:
    def __init__(self, message, dictionary):
        """
        This inputs the parameters for the class
        message: the message to be coded or the coded message
        dictionary: an external dictionary file which is inputed
        as a string
        """
        self.sau = __self.lodic(dictionary)
        self.msg = self.message
        
    def __lodic(file):
        """
        Input: file -> a string referencing a file name 
        This functions turns the file into a dictionary
        """
        d = {}
        with open(file) as f:
            for f in f.readlines():
                (key, val) = line.split()
                d[int(key)] = val
                
    def getMessage(self):
        """
        This returns the message as a value
        """
        return self.msg
    
    def printMessage(self):
        """
        This prints the message on screen
        """
        print(self.msg)
        
    def setMessage(self, text):
        """
        Input: text -> a string
        This turns our text into the to-be-(de)coded one
        """
        self.msg = text


class vigncyph(codebas): #Vigniere cypher
    
    def __init__(steps = None, message, dictionary):
        """
        This inputs the parameters of the class
        message, dictionary: included in the heritage
        steps: list of integers
        """
        codebas.__init__(self, message, dictionary)
        self.st = steps if steps is not None else self.__randchoose()
        
    def __randchoose(self):
        """
        This chooses a random number and adds them to the steps"
        """
        k = random.randint(20)
        m = 0
        res = []
        while m < k:
            m += 1
            z = random.randint(0, len(file.open(dictionary).readlines()))
            res.append(z)
        return res
    
    def code(self):
        """
        MAIN
        Codes the text
        SUBFUNCTION
        Input: Integer -> Int, value of the step
               String -> String, text to code
               Dictio -> Dictionary to use
               Diclen -> Character length of the dictionary
        Applies the vigniere algorithm to the text
        """
        def code_iterate(integer, string, dictio, diclen):
            k = list(string)
            d = dictio
            i = integer
            res = ""
            invdic = {v: k for k, v in d.items()}
            for e in k:
                res += d[(invdic[e] + i)%diclen]       
            return res
        m = self.msg
        dt = self.sau
        for e in self.steps:
            m = code_iterate(e, m, dt, len(file.open(dictionary).readlines().readlines()))
        self.msg = m
            
    
    def decode(self):
        """
        MAIN
        Decodes the text
        SUBFUNCTION
        Input: Integer -> Int, value of the step
               String -> String, text to code
               Dictio -> Dictionary to use
               Diclen -> Character length of the dictionary
        Applies the caesaric algorithm to the text
        """
        def decode_iterate(integer,string, dictio, diclen):
            k = list(self.msg)
            d = dictio
            i = integer
            res = ""
            invdic = {v: k for k, v in d.items()}
            for e in k:
                res += d[invic[e] - i + diclen]
            return res
        m = self.msg
        dt = self.sau
        for e in self.steps:
            m = decode_iterate(e, m, dt, len(__self.sou.readlines()))
        self.msg = m
  
    def setSteps(self, lis):
        """
        Sets the steps from an external source
        """
        self.steps = lis
                 
class rsacyph(codebas):
    
    def __init__(ukey, pkey, msg, dic):
        """
        This inputs the parameters for the class
        msg, dic: included in the heritage
        ukey: public rsa key (used to code)
        pkey: private rsa key (used to decode)
        """
        codebas.__init__(self, msg, dic)
        self.pub = ukey
        self.priv = pkey
        
    
    def code(self):
        """
        This applies the RSA algorithm to code the text
        """
        t = list(self.msg)
        (pria, expa) = self.pub
        prib = self.priv[0]
        d = self.sau
        rd = {v: k for k, v in d.items()}
        res = ""
        for e in t:
            res  +=  dic[(rd[e]**expa)%(pria*prib)]
        self.msg = res
    
    def decode(self):
        """
        This applies the RSA algorith to decode the text
        """
        t = list(self.msg)
        pria = self.pub[0]
        (prib, expb) = self.priv
        d = self.sau
        rd = {v: k for k,v in d.items()}
        res = ""
        for e in t:
            res += dic[(rd[e]**expb)%(pria*prib)]
        self.msg = res