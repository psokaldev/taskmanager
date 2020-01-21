# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 21:48:03 2020

@author: DEV
"""
from datetime import datetime
import csv
import json
class Task:
    
    
    def __init__(self):
        self._loaded = False

    def new(self,name, desc,required_time, deadline,autocommit=False):
        self._JSON = {'name':name,
                      'desc':desc,
                      'req_time':required_time,
                      'deadline':deadline,
                      'reg_date':datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                      }
        self._loaded = True
        self._toupdate = False
        if autocommit and self._loaded:
            self.commit()
            pass
    def update(self,field, value):
        if field in ['name','desc','req_time','deadline']:
            self._toupdate = True
        
        
        
    def get(self,name):
        return self._JSON[name]
    
    def commit(self):
        if self._toupdate:
            self._archive()
            ####update in csv
        else:
            with open("tasks.csv", "w") as f:
                w = csv.DictWriter(f,self._JSON.keys(), delimiter = ";")
                w.writerow(self._JSON)
            
    def _archive(self):
        ####archive here
        pass
 
        