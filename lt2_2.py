# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 15:39:28 2017

@author: Jeffrey
"""
import threading
import sys

class scan(threading.Thread):
    def __init__(self, edge, des, lock, tid):
        self.des = des
        self.edge = edge
        self.lock = lock
        super(scan, self).__init__(name = tid)
        
    def run(self):
      while True:
           self.lock.acquire()
           tag = self.des.tell()-4
           word = self.des.read(1000)
           v = self.edge.getv()
           self.edge.setv(word[996:])
           self.lock.release()
           if word == "":
               break
           res = (v+word).split("waldo")
           index = 0
           length = len(res)
           if(length > 1):
               l = 0
               while(index != length-1):
                   v = res[index]
                   if index == 0:
                       l += len(v)
                   else:
                       l += len(v) + 5
                   print("\nFound Waldo @ "+str(tag+l)+" by "+self.name)
                   index += 1
 
class v_edge(object):
    def __init__(self, value):
        self.edge = value
    
    def setv(self, value):
        self.edge = value
    
    def getv(self):
        return self.edge

if __name__ == "__main__":
    num_t = int(sys.argv[2])
    edge = v_edge("")
    file = open(sys.argv[1])
    lock = threading.Lock()
    for i in range(num_t):
        sc = scan(edge, file, lock, "process"+str(i))
        sc.start()
   
    
  
        