# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 20:41:09 2020

@author: DEV
"""
import time
import kivy
import random
from backend.resources import task
import os
from kivymd.app import MDApp
from kivy.factory import Factory
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.list import TwoLineListItem
from kivy.uix.screenmanager import Screen, ScreenManager

class TaskListElement(TwoLineListItem):
    def __init__(self, **kwargs):
        super(TaskListElement,self).__init__(**kwargs)
class TaskList(Screen):
    pass
class MainWindow(Screen):
    pass
class SManager(ScreenManager):
    pass
class TaskApp(MDApp,task.Tasks):
    Builder.load_file('frontend/uix/MainWindow.kv')
    Builder.load_file('frontend/uix/TaskList.kv')
    Builder.load_file('frontend/uix/TaskListElement.kv')
    def __init__(self,**kwargs):
        self.title = "Task application"
        self.theme_cls.primary_palette = "DeepPurple"
        super().__init__(**kwargs)
        self.load_by_date('2019-01-31')
    def build(self, **kwargs):
        self.root  = ScreenManager()
        self.root.add_widget(MainWindow(name="main"))
        self.root.add_widget(TaskList(name="task_list"))
        self.root.current = "main"
        
        
    def show_task_list(self):
        self.root.current = "task_list"
        for i in range(10):
            for t in self._tasks:
                self.root.current_screen.ids.gs.add_widget(TwoLineListItem(
                    text = t['name'],secondary_text = t['ID']))
if __name__ == "__main__":
    #app = HBoxLayoutExample()
    #app.run()
    TaskApp().run()
    
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
    
    
    
    