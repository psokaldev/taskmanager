# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 23:48:31 2020

@author: DEV
"""


from kivy.lang import Builder
from kivymd.uix.picker import MDDatePicker
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from datetime import date
Builder.load_string(
    """
<DatePicker>    
    size_hint_y:0.8
    AnchorLayout:
        anchor_x:'center'
        anchor_y:'center'
        GridLayout:
            cols:2
            width: self.minimum_width
            MDTextField:
                id: date_field
                hint_text: "YYYY-MM-DD"
                
            MDIconButton:
                icon: "calendar"
                on_release: root.show_calendar()
        MDRoundFlatButton:
            text: "Search"
            on_press: app.show_task_list(date_field.text)
"""
)

class DatePicker(FloatLayout):
    date_given = ObjectProperty()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_previous_date (date.today())
    def show_calendar(self):
        MDDatePicker(self.set_previous_date).open()
    def set_previous_date(self, date_obj):
        self.date_given = date_obj
        self.ids.date_field.text = str(date_obj)
    