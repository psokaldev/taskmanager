# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 20:41:09 2020

@author: DEV
"""
#import time
#import kivy
#import random
from backend.resources.task import Tasks, Task
#import os
from kivymd.app import MDApp
#from kivy.factory import Factory
from kivy.lang import Builder
#from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.list import TwoLineListItem
from kivymd.toast import toast
from kivy.uix.screenmanager import Screen, ScreenManager
#from kivy.properties import StringProperty
#from kivy.properties import ObjectProperty
from frontend.uix.TaskItem import TaskItem, TaskCard
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

class TaskApp(MDApp,Tasks):
    Builder.load_file('frontend/uix/kv/MainWindow.kv')
    Builder.load_file('frontend/uix/kv/TaskList.kv')
    Builder.load_file('frontend/uix/kv/TaskForm.kv')
    def toast(self,text):
        toast(text)
    def __init__(self,**kwargs):
        self.title = "Task application"
        self.theme_cls.primary_palette = "DeepPurple"
        super().__init__(**kwargs)
        
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
        self.load_todays_tasks()
        self.print_task_list()
    def show_task_list(self):
        self.root.current = "task_list"
        self.clear_task_list()
        self.load_by_date('2019-01-31')
        self.print_task_list()
        
    def print_task_list(self):
        for t in self._tasks:
            self.root.current_screen.ids.task_list.add_widget(TaskItem(
                    content=TaskCard(description=t['info']['desc'],required_time =t['info']['req_time']),
                    title = t['name'], 
                    secondary= t['info']['deadline']))
    def add_new_task(self):
        self.root.current = "task_form"
    def clear_task_list(self):
        self.root.current_screen.ids.task_list.clear_widgets()
    def save_task(self,name, desc,required_time, deadline):
        Task().new(name, desc,required_time, deadline,True)
        self.root.current = "task_list"
if __name__ == "__main__":
    #app = HBoxLayoutExample()
    #app.run()
    TaskApp().run()
#def getMe():
    #return TaskApp()
    #task.Task().new("test","descritdgsdgf","2h","2019-01-31",True)
    #time.sleep(2)
    #t = task.Task()
    #t.new("test","descritdgssasasasadgf","2h","2019-01-31",True)
    #time.sleep(2)
    #t.update('desc','dgdfhgdsgsdgfsadgsadgfassfaswfa')
    #t.commit()
    #t = task.Tasks()
    #t.load_by_date('2019-01-31')
    #g = t.get()
    #for g_ in g:
        #print(', '.join([g_['ID'],g_['name'],g_['info']['desc']]))
    #e = task.Event("20200123205728")
    #time.sleep(4)
    #e.stop()
    #t = task.Task()
    #t.load(20200123205730)
    #t.print_()
    #t.crossout()
    
    
    
    