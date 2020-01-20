# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 21:48:03 2020

@author: DEV
"""
from datetime import datetime
class Task:
    
    
    def __init__(self):
        self._loaded = False
 
    def new(self,name, desc,required_time, deadline):
        self._JSON = {'name':name,
                      'desc':desc,
                      'req_time':required_time,
                      'deadline':deadline,
                      'reg_date':datetime.now().strftime("%d/%m/%Y %H:%M:%S")}
        self._loaded = True
    
    def update(self):
        pass
    
    def get(self,name):
        pass