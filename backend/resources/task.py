# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 21:48:03 2020

@author: DEV
"""
from datetime import datetime
import csv
import json

from tempfile import NamedTemporaryFile
import shutil
TASK_FILE_NAME = "tasks.csv"
class Task:
    
    
    
    def __init__(self):
        self._loaded = False

    def new(self,name, desc,required_time, deadline,autocommit=False):
        self._JSON = {
                      'ID':datetime.now().strftime('%Y%m%d%H%M%S'),
                      'name':name,
                      'desc':desc,
                      'req_time':required_time,
                      'deadline':deadline,
                      'reg_date':datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                      'last_update': datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                      }
        self._loaded = True
        self._toupdate = False
        if autocommit and self._loaded:
            self.commit()
    
    def update(self,field, value):
        if field in ['name','desc','req_time','deadline']:
            self._JSON[field] = value
            self._toupdate = True

    def getfield(self,name):
        return self._JSON[name]
    
    def commit(self):
        if self._toupdate:
            self._JSON['last_update'] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            with open(TASK_FILE_NAME, 'r', newline='') as readFile, open(TASK_FILE_NAME.replace('.csv', '_new.csv'), 'w', newline='') as f: 
                for row in readFile:
                    if row.split(";")[0] == self._JSON['ID']:
                        self._archive(row)
                        f.write(";".join(list(self._JSON.values())) + '\n')
                    elif row != "": 
                        f.write(row)
            shutil.move(TASK_FILE_NAME.replace('.csv', '_new.csv'),TASK_FILE_NAME)
        else:
            with open(TASK_FILE_NAME, "a+", newline='') as f:
                w = csv.DictWriter(f,self._JSON.keys(), delimiter = ";")
                w.writerow(self._JSON)
    
    def _archive(self,row):
        with open(TASK_FILE_NAME.replace('.csv', '_archive.csv'), "a+", newline='') as f:
            nrow = row.split(";")
            nrow[-1] = self._JSON['last_update']
            f.write(";".join(nrow)+ '\n')
        