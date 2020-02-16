# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 09:08:27 2020

@author: DEV
"""
from datetime import datetime, date
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, Date, DateTime,Time
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
# Global Variables
SQLITE= 'sqlite'
DATE_FORMAT = "%d/%m/%Y %H:%M:%S"

Base = declarative_base()





class Activity(Base):
    __tablename__='activity'
    id = Column(Integer,primary_key=True)
    task_id = Column(Integer,ForeignKey('task.id'))
    start_time = Column(DateTime)
    end_time= Column(DateTime)
    work_time= Column(Time)
    task = relationship('Task')

class Note(Base):
    __tablename__='note'
    id = Column(Integer,primary_key=True)
    task_id = Column(Integer,ForeignKey('task.id'))
    registered= Column(DateTime)
    task = relationship('Task')
    
class TaskArchive(Base):
    __tablename__='task_archive'
    id = Column(Integer,primary_key=True)
    task_id = Column(Integer,ForeignKey('task.id'))
    name = Column(String)
    description= Column(String)
    required_time= Column(String)
    deadline= Column(Date)
    registered= Column(DateTime)
    last_update= Column(DateTime)

class Task(Base):
    __tablename__='task'
    id = Column(Integer,primary_key=True)
    name = Column(String)
    description= Column(String)
    required_time= Column(String)
    deadline= Column(Date)
    registered= Column(DateTime)
    last_update= Column(DateTime)
    activities = relationship(Activity,backref='tasks')
    notes = relationship(Note,backref='tasks')
    
    def __init__(self,
                 name, 
                 description,
                 required_time,
                 deadline,
                 registered= datetime.now(),
                 last_update=datetime.now()):
        self.name = name
        self.description = description
        self.required_time = required_time

        if isinstance(deadline, str):
            self.deadline = datetime.strptime(deadline, '%Y-%m-%d')#.strftime(DATE_FORMAT)
        else:
            self.deadline = deadline
        self.registered= registered #.strftime(DATE_FORMAT)
        self.last_update = last_update
    
    def serialize(self):
        return {'id': self.id,
                'name': self.name,
                'description': self.description,
                'required_time': self.required_time,
                'deadline': self.deadline.strftime('%Y-%m-%d'),
                'registered': self.registered.strftime(DATE_FORMAT),
                'last_update': self.last_update.strftime(DATE_FORMAT)
                }
       
class DB():
    DB_ENGINE = {
        SQLITE: 'sqlite:///{DB}'
    }
    db_engine = None
    session = None
    def __init__(self, dbtype, username='', password='', dbname=''):
        dbtype = dbtype.lower()
        if dbtype in self.DB_ENGINE.keys():
            engine_url = self.DB_ENGINE[dbtype].format(DB=dbname)
            self.db_engine = create_engine(engine_url)
            print(self.db_engine)
        else:
            print("DBType is not found in DB_ENGINE")  
        Session = sessionmaker(bind=self.db_engine)
        self.session = Session()
    def add(self,obj):
        self.session.add(obj)
        self.session.commit()
        
    def get_tasks_by_deadline(self,
                deadline=datetime.now().strftime('%Y-%m-%d')):
        query = self.session.query(Task).filter_by(deadline=deadline)
        tasks = []
        if query.count() > 0:
            for t in query.all():
                tasks.append(t.serialize())
        print(tasks)
        return tasks
    def create_all_tables(self):
        Base.metadata.create_all(self.db_engine)


