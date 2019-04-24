# -*- coding: utf-8 -*-
import random
import math
import scipy.stats as stats
import numpy as np

class webserver:
    def __init__(self):
        self.lamda = 10
        self.ps = 0.8
        self.T_parse = 0.005
        self.cookie = 0
        self.getsession = 0.01
        self.readfile = 0.1
        self.pi = 0.35
        self.response = 0.012
        self.filegenerat = 0.045
        self.pa = 0.1
        "resrouces usage"
        self.httptime = 0
        self.disctime = 0
        self.memeorycache = 0
        self.interpreter = 0
        # sequence for Tsf
        "initialize the ltst"
        self.ltsf = [[0.03, 0.03],
                     [0.06, 0.07],
                     [0.08, 0.1],
                     [0.1, 0.4],
                     [0.13, 0.2],
                     [0.19, 0.11],
                     [0.22, 0.08],
                     [0.3, 0.01]]
        
     
    "poisson distribution, it seems that we don't need to use its value in this simulatioin"
    def poisson(self):
        p = 1.0
        k = 0  
        l = self.lamda
        e = math.exp(-1*l)  
        while p >= e:  
            u = random.random()  #generate a random floating point number in the range [0.0, 1.0)  
            p *= u  
            k += 1  
        return k-1  
        
    "1 = has cookie, 0 = no cookie"
    def ps_cookie(self):
        r = stats.binom.rvs(1, 0.8, size=1)
        return r
    
    "1 = has dynamical generation, 0 = static"
    def pi_dors(self):
        r = stats.binom.rvs(1, 0.35, size=1)
        return r

    "1 = has additioinal file, 0 = none"
    def pa_additional(self):
        r = stats.binom.rvs(1, 0.1, size=1)
        return r
    
    def helper(self, n, value):
        for x in range(n):
            self.ltsf.append(value)
    
    "get the Tsf time(this part is the same as p3)"
    def get_Tsf(self):
        outcome = [x[0] for x in self.ltsf]
        possi = [x[1] for x in self.ltsf]
        result = np.random.choice(outcome, p = possi)
        self.readfile = result
        return self.readfile

    "print the result"
    def print_result(self):
        ls = self.getstarted()
        s = ls[4]
        print("Request completed time: ", s)
        print("Utilization of web-server: ", ls[0]/s)
        print("Utilization of memorycache: ", ls[1]/s)
        print("Utilization of disc: ", ls[2]/s)
        print("Utilization of interpreter: ", ls[3]/s)
        print("Throughput of disc: ", 1/ls[2])
        if ls[3] == 0:
            print("Throughput of interpreter: ", 0)
        else:
            print("Throughput of interpreter: ", 1/ls[3])
        
    "process a request"
    def getstarted(self):
        reslist = []
        res = self.T_parse;
        self.httptime += self.T_parse
        if self.ps_cookie() == 1:
            res += self.getsession
            self.memeorycache += self.getsession
        tmp = self.get_Tsf()
        res += tmp
        self.disctime += tmp 
        if self.pi_dors() == 0:
            res += self.response
            self.httptime += self.response
        else:
            res += self.filegenerat
            self.interpreter += self.filegenerat
            k = self.pa_additional()
            while(k == 1):
                if self.pi_dors() == 0:
                    break
                else:
                    res += self.filegenerat
                    self.interpreter += self.filegenerat
                    k = self.pa_additional() 
            res += self.response
            self.httptime += self.response

        reslist.append(self.httptime)
        reslist.append(self.memeorycache)
        reslist.append(self.disctime)
        reslist.append(self.interpreter)
        reslist.append(res)
        
        return reslist


for x in range(1, 11):
    print("\nSimulation", x, "outcome:")
    c = webserver()
    c.print_result()
print("\nTheoritical outcome: ")
all_ = 0.005+0.01*0.8+0.1+0.045*0.35+0.1*0.35*0.045+0.012
http = 0.005+0.012
cache = 0.01*0.8
disc = 0.1
interpreter = 0.045*0.35+0.1*0.35*0.045
print("Request completed time: ", 0.005+0.01*0.8+0.1+0.045*0.35+0.1*0.35*0.045+0.012)
print("Utilization of web-server: ", http/all_)
print("Utilization of memorycache: ", cache/all_)
print("Utilization of disc: ", disc/all_)
print("Utilization of interpreter: ", interpreter/all_)
print("Throughput of disc: ", 1/disc)
print("Throughput of interpreter: ", 1/interpreter)


    
    