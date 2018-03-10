# -*- coding: utf-8 -*-
"""
Created on Thu Mar 01 19:38:14 2018

@author: lukish.rajesh.yadav
"""



import SOAPpy
server = SOAPpy.SOAPProxy("http://localhost:8080/")
c=server.A
#print server.hello()
print c.B()

