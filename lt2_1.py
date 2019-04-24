# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 14:40:05 2017

@author: Jeffrey
"""
import sys

def find_waldo(filename):
    file = open(filename)
    tag = 0
    edge = ""
    word = file.read(1000)   
    while word != "":
        res = (edge+word).split("waldo")
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
                print("\nFound Waldo @ "+str(tag+l))
                index += 1
        edge = word[996:]
        word = file.read(1000)
        if(tag == 0):
            tag = 996
        else:
            tag += 1000
    file.close()
        
if __name__ == "__main__":
    find_waldo(sys.argv[1])