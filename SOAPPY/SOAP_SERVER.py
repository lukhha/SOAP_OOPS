# -*- coding: utf-8 -*-
"""
Created on Thu Mar 01 19:38:14 2018

@author: lukish.rajesh.yadav
"""

import SOAPpy
def hello():
    return "Hello World"


class A:
    def B(self):
        return 'Method inside class has returned this!'
    
    
server = SOAPpy.SOAPServer(("localhost", 8080))
server.registerClass(A)
server.registerFunction(A)
server.serve_forever()



