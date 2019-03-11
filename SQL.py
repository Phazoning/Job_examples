# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 18:42:36 2019

@author: Alonso
"""
"""
TABLAS
llegadas(
code char(8) primary key,
hora char(5) not null,
nombre varchar(20) not null,
origen varchar(25) not null,
estado varchar(12),
);
SALIDAS(
          code char(8) primary key,
          hora char(5) not null,
          nombre varchar(20) not null,
          destino varchar(25) not null,
          estado varchar(12) not null,
         );
BUSES(
         code char(8) primary key,
         nombre varchar(25) not null,
         matrícula varchar(10) not null,
        )
"""
import sqlite3 as lite
import sys
import threading
import datetime

con = lite.connect('buses.db')

class table:
    
    def __init__(self, cursor, name):
        self.cu = cursor
        self.tb = name
        self.con = self.cu.execute("SELECT * FROM " + self.tb)
        
    def bu_create(self):
        da = datetime.datetime.now().date()
        da = str(da[2]) + "/" + str(da[1]) + "/" + str(da[0])
        ti = datetime.datetime.now().time()
        ti = str(ti[0]) + ":" + str(ti[1]) + ":" + str(ti[2])
        dati = da + "-" + ti
        self.cu.execute("CREATE " + self.tb + dati  + " AS SELECT * FROM " + self.tb  )
    
    def cleanse(self):
        self.cu.execute("DELETE * FROM " + self.tb)
        
class btable(table):
    
    def __init__(self, cursor, name, ctable):
        table.__init__(cursor, name)
        self.com = ctable
        self.bco = self.cu.execute("SELECT * FROM " + self.com)
        
    def istime(self):
        def timecom(etime, ctime):
            ttime = [int(ctime[0]), int(ctime[1])]
            if ttime[0] == etime[0] and ttime[1] <= ctime[1] + 5:
                return "good"
            else:
                return "delay"
            
        time = datetime.datetime.now().time()
        time = [time[0], time[1]]
        for e in self.tb:
            autime = e[1].split(":")
            if timecom(time, autime) == "delay" and e[5] != "en darsena":
                self.cu.execute("UPDATE " + self.tb + " SET estado = 'retrasado' where code = " + e[0])
            elif timecom(time, autime) == "delay" and e[5] == "en darsena":
                self.cu.execute("DELETE * FROM " + self.tb + " WHERE code = " + e[0]) 
                if len(self.tb) < 8:
                    self.cu.execute("INSERT * FROM " + self.com + "WHERE code = " + self.fill(int(e[0]) + 8))
                    
    def fill(integer):
        
        d = str(integer)
        
        while len(list(d)) < 6:
            d = "0" + d
        return d
            
    def emptiness(self):
        k = self.con
        m = 0
        while len(k) < 8:
            if self.cu.execute("SELECT * FROM " + self.com) != []:    
                self.cu.execute("INSERT * FROM " + self.com + "WHERE CODE = " + self.fill(int(m)))

def main(db):
    
    con = lite.connect(db)
    def arrloop():
        co1 = con.cursor()
        k = btable(co1, "llegadas", "arrivals")
        k.emptiness()
        d = table(co1, "arrivals")
        d.bu_create()        
        d.cleanse()
        while 1 == 1:
            k.istime()
            
            
    def deploop():
        co2 = con.cursor()
        k = btable(co2, "salidas", "departures")
        k.emptiness()
        d = table(co2, "departures")
        d.bu_create()
        d.cleanse()
        while 1 == 1:
            k.istime()
            
    def console():
        co3 = con.cursor()
        while 1==1:
            k = input()
            if k == "Salidas, Añadir nuevo bus":
                m = input()
                print("Introduzca datos del bus ['hora', 'destino', 'estado']")
                try:
                    co3.execute("INSERT INTO departures (hora, destino, estado) VALUES " + str(m[0]) + "," + str(m[1])+ ","  + str(m[2])+ ","  + '' )      
                except:
                    print()
            elif k == "Salidas, Quitar bus":
                print("Introduzca la posición del bus a quitar")
                d = int(input())
                try:
                    co3.execute("DROP * FROM departures WHERE code = " + str(d))
                except:
                    print()                
            elif k == "Llegadas, Añadir nuevo bus":
                m = input()
                print("Introduzca datos del bus ['hora', 'destino', 'estado']")
                try:
                    co3.execute("INSERT INTO arrivals (hora, destino, origen) VALUES " + str(m[0]) + "," + str(m[1])+ ","  + str(m[2])+ ","  + '' )      
                except:
                    print()
            elif k == "Llegadas, Quitar bus":
                print("Introduzca la posición del bus a quitar")
                d = int(input())
                try:
                    co3.execute("DROP * FROM arrivals WHERE code = " + str(d))
                except:
                    print()
    f1 = threading.Thread(target=arrloop)
    f2 = threading.Thread(target=deploop)
    f3 = threading.Thread(target=console)
    threads.append(f1)
    threads.append(f2)
    threads.append(f3)
    f1.start()
    f2.start()
    f3.start()
