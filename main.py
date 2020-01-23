# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 20:41:09 2020

@author: DEV
"""
import time
import kivy
import random
from backend.resources import task

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

red = [1,0,0,1]
green = [0,1,0,1]
blue =  [0,0,1,1]
purple = [1,0,1,1]

class HBoxLayoutExample(App):
    def build(self):
        layout = BoxLayout(padding=10)
        colors = [red, green, blue, purple]

        for i in range(5):
            btn = Button(text="Button #%s" % (i+1),
                         background_color=random.choice(colors)
                         )

            layout.add_widget(btn)
        return layout

if __name__ == "__main__":
    #app = HBoxLayoutExample()
    #app.run()
    
    #task.Task().new("test","descritdgsdgf","2h","2019-01-31",True)
    #time.sleep(2)
    #t = task.Task()
    #t.new("test","descritdgssasasasadgf","2h","2019-01-31",True)
    #time.sleep(2)
    #t.update('desc','dgdfhgdsgsdgfsadgsadgfassfaswfa')
    #t.commit()
    t = task.Tasks()
    t.load_by_date('2019-01-31')
    g = t.get()
    for g_ in g:
        print(', '.join([g_['ID'],g_['name'],g_['info']['desc']]))