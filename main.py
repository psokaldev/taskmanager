# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 20:41:09 2020

@author: DEV
"""
#import time
#import kivy
#import random
#from backend.resources.task import Tasks#, Task
#import os
from kivymd.app import MDApp
#from kivy.factory import Factory
from kivy.lang import Builder
#from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.list import TwoLineListItem
from kivymd.toast import toast
from datetime import datetime
from kivy.uix.screenmanager import Screen, ScreenManager
#from kivy.properties import StringProperty
#from kivy.properties import ObjectProperty
from frontend.uix.TaskItem import TaskItem, TaskCard
from frontend.uix.DatePicker import DatePicker
from backend.resources.db import DB, Task
class TaskListElement(TwoLineListItem):
    pass
class TaskList(Screen):
    pass
class TaskForm(Screen):
    pass
class MainWindow(Screen):
    pass
class SManager(ScreenManager):
    pass
#class TaskCard(BoxLayout):
    #pass

class TaskApp(MDApp):
    Builder.load_file('frontend/uix/kv/MainWindow.kv')
    Builder.load_file('frontend/uix/kv/TaskList.kv')
    Builder.load_file('frontend/uix/kv/TaskForm.kv')
    _tasks=[]
    float_box = None
    def toast(self,text):
        toast(text)
    def __init__(self,**kwargs):
        self.title = "Task application"
        self.theme_cls.primary_palette = "DeepPurple"
        super().__init__(**kwargs)
        self.db = DB(dbtype='sqlite',dbname='database.db')
    def build(self, **kwargs):
        self.root  = ScreenManager()
        self.root.add_widget(MainWindow(name="main"))
        self.root.add_widget(TaskList(name="task_list"))
        self.root.add_widget(TaskForm(name="task_form"))
        self.main_window()
    def back_to_main(self):
        self.main_window()
    def main_window(self):
        self.root.current = "main"
        self.clear_task_list()
        self._tasks=self.db.get_tasks_by_deadline()
        self.print_task_list()
    def search_for_tasks(self):
        self.float_box= DatePicker()
        self.root.current_screen.add_widget(self.float_box)
    def show_task_list(self, date):
        self.root.current_screen.remove_widget(self.float_box)
        self.root.current = "task_list"
        self.clear_task_list()
        self._tasks=self.db.get_tasks_by_deadline(str(date))
        self.print_task_list()
        
    def print_task_list(self):
        for t in self._tasks:
            self.root.current_screen.ids.task_list.add_widget(TaskItem(
                    content=TaskCard(description=t['description'],required_time =t['required_time']),
                    title = t['name'], 
                    secondary= t['deadline']))
    def add_new_task(self):
        self.root.current = "task_form"
    def clear_task_list(self):
        self.root.current_screen.ids.task_list.clear_widgets()
    def save_task(self,name, desc,required_time, deadline):
        self.db.add(Task(name, desc,required_time, deadline))
        self.root.current = "task_list"

if __name__ == "__main__":
    TaskApp().run()



