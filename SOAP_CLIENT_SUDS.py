# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 00:48:57 2018

@author: lukish.rajesh.yadav
"""

from suds.client import Client as SudsClient

url = 'http://127.0.0.1:5000/soap/someservice?wsdl'
client = SudsClient(url=url, cache=None)
r = client.service.echo(str='hello world', cnt=3)
print r