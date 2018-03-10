# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

    if 'X' in locals():
     print X
    else:
     print 0
 

#This class will take an input. 
It will save the input if we run save method of class.
RP returns the latest saved value.
X is the global variable.     
     
     



def B(x):
    global X
    if x>X:
        print 'local'
    else:
        print 'global'
        
        
class A:
    
        
    def __init__(self,x):
       
        self.x=x
        
    def save(self):
        
        A.X=self.x
         
    def RP(self):
        return A.X
    
        
        
        
if 'X' in locals():
    print 1
else:
    print 0


with open('1.txt', 'w') as memory:
            memory.write('%s:%s' % ('Lukhha',6))        
 