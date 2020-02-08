# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 21:48:03 2020

@author: DEV
"""
from datetime import datetime
import csv

import shutil
TASK_FILE_NAME = "tasks.csv"
REG_FILE = "registry.csv"
DATE_FORMAT = "%d/%m/%Y %H:%M:%S"


def _currentTimeStamp():
    return datetime.now().strftime(DATE_FORMAT)


class Task:
    def __init__(self):
        self._loaded = False
        self._toupdate = False
        self._JSON = {}
        
        
    def crossout(self):
        if self._loaded == True:
            self._JSON['last_update'] = _currentTimeStamp()
            self._replacerow("")
            with open(TASK_FILE_NAME.replace(".csv","_done.csv"), "a+", newline='') as f:
                w = csv.DictWriter(f,self._JSON.keys(), delimiter = ";")
                if f.tell() == 0:
                    w.writeheader()
                w.writerow(self._JSON)
    
    def load(self,task_id):
        with open(TASK_FILE_NAME,'r',newline='') as f:
            r = csv.DictReader(f,delimiter = ";")
            for row in r:
                if str(row['ID']) == str(task_id):
                    self._JSON = row
                    self._loaded = True
                    break
    def print_(self):
        for f in self._JSON:
            print(": ".join([f,str(self._JSON[f])]))
    def new(self,name, desc,required_time, deadline,autocommit=False):
        self._JSON = {
                      'ID':datetime.now().strftime('%Y%m%d%H%M%S'),
                      'name':name,
                      'desc':desc,
                      'req_time':required_time,
                      'deadline':deadline,
                      'reg_date':_currentTimeStamp(),
                      'last_update': _currentTimeStamp()
                      }
        self._loaded = True
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
            self._JSON['last_update'] = _currentTimeStamp()
            self._replacerow(";".join(list(self._JSON.values())) + '\n')
        else:
            with open(TASK_FILE_NAME, "a+", newline='') as f:
                w = csv.DictWriter(f,self._JSON.keys(), delimiter = ";")
                if f.tell() == 0:
                    w.writeheader()
                w.writerow(self._JSON)
    def _replacerow(self,new_row):
        with open(TASK_FILE_NAME, 'r', newline='') as readFile, open(TASK_FILE_NAME.replace('.csv', '_new.csv'), 'w', newline='') as f: 
            for row in readFile:
                if row.split(";")[0] == self._JSON['ID']:
                    self._archive(row)
                    if len(new_row)>0:
                        f.write(new_row)
                elif row != "": 
                    f.write(row)
        shutil.move(TASK_FILE_NAME.replace('.csv', '_new.csv'),TASK_FILE_NAME)
    
    def _archive(self,row):
        with open(TASK_FILE_NAME.replace('.csv', '_archive.csv'), "a+", newline='') as f:
            w = csv.DictWriter(f,self._JSON.keys(), delimiter = ";")
            if f.tell() == 0:
                w.writeheader()
            nrow = row.split(";")
            nrow[-1] = self._JSON['last_update']
            f.write(";".join(nrow)+ '\n')


class Event:
    def __init__(self, task_id):
        self._task_id = task_id
        self._start_time = datetime.now().strftime(DATE_FORMAT)
    def stop(self):
        self._end_time = datetime.now().strftime(DATE_FORMAT)
        with open(REG_FILE, "a+", newline='') as f:
            if f.tell() == 0:
                f.write(";".join(["task_id","start_time","end_time","duration"])+"\n")
            f.write(";".join([self._task_id,self._start_time,self._end_time,str(self._date_diff_sec(self._start_time,self._end_time))])+"\n")
    def _date_diff_sec(self, st, ed):
        _ed = datetime.strptime(ed,DATE_FORMAT)
        _st = datetime.strptime(st,DATE_FORMAT)
        return int((_ed-_st).total_seconds())


class Tasks:
    def __init__(self,**kwargs):
        self._loaded = False
        self._tasks = []
    def load_by_date(self, date):
        with open(TASK_FILE_NAME,'r',newline='') as f:
            r = csv.DictReader(f,delimiter = ";")
            for row in r:
                if str(datetime.strptime(row['deadline'],'%Y-%m-%d').date()) == date:
                    self._tasks.append( {'ID':row['ID'],
                                         'name':row['name'],
                                         'info':{a:row[a] for a in row.keys() if a not in ['ID','name']}
                                         })
        self._loaded = True
    def get(self):
        if self._loaded:
            return self._tasks
                    
        
        
        
        
        
        
        