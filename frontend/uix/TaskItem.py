# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 19:36:42 2020

@author: DEV
"""

from kivy.lang import Builder
from kivy.animation import Animation
from kivy.metrics import dp
from kivy.properties import ObjectProperty, NumericProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDIconButton
from kivymd.uix.list import IRightBodyTouch,TwoLineListItem,TwoLineRightIconListItem

Builder.load_string(
    """
<TaskCard>    
    orientation: 'vertical'
    padding: dp(10)
    spacing: dp(10)
    size_hint_y: None
    height: self.minimum_height

    BoxLayout:
        size_hint_y: None
        height: self.minimum_height

        Widget:
        MDRoundFlatButton:
            text: "Work"
            on_press: app.toast(self.text)
        Widget:
        MDRoundFlatButton:
            text: "Pomodoro"
            on_press: app.toast(self.text)
        Widget:
    TwoLineListItem:
        id: t_desc
        text: root.required_time
        secondary_text: root.description
        on_press: app.toast("Edit the desc")
        
<TitlePanel>
    text: root.title
    secondary_text: root.secondary
    _no_ripple_effect: True
    ChevronRight:
        id: chevron
        icon: 'chevron-right'
        disabled: True
        canvas.before:
            PushMatrix
            Rotate:
                angle: self.angle
                axis: (0, 0, 1)
                origin: self.center
        canvas.after:
            PopMatrix
<TaskItem>
    size_hint_y: None
    height: dp(68)
    BoxLayout:
        id: box_item
        size_hint_y: None
        height: root.height
        orientation: 'vertical'
        TitlePanel:
            id: item_anim
            text: root.title
            secondary_text: root.secondary
            on_press: root.expand_content(self)
"""
)
    
    
    
class TaskItem(BoxLayout):
    content = ObjectProperty()
    title = StringProperty()
    secondary=StringProperty() 
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def expand_content(self, instance):
        pressed = False
        #loop through all siblings to close opened one
        for box in self.parent.children: 
            if box.__class__ is TaskItem:
                #if content exists it is #2 child of box_item
                if len(box.ids.box_item.children)==2:  
                    if instance is box.ids.item_anim:
                        pressed = True
                    #delete content
                    box.ids.box_item.remove_widget(box.ids.box_item.children[0])
                    chevron = box.ids.box_item.children[0].ids.chevron
                    self.anim_chevron_up(chevron)
                    self.anim_resize_close(box)
                    break
        if not pressed:
            self.anim_chevron_down()
    
    def anim_chevron_down(self):
        chevron = self.ids.item_anim.ids.chevron
        angle = -90
        Animation(angle=angle, d=0.2).start(chevron)
        self.anim_resize_open_item()

    def anim_chevron_up(self, instance):
        angle = 0
        Animation(angle=angle, d=0.2).start(instance)

    def anim_resize_close(self, box):
        Animation(height=dp(68), d=0.1, t="in_cubic").start(box)

    def anim_resize_open_item(self, *args):
        self.content.name_item = self.title
        anim = Animation(
            height=self.content.height + dp(70), d=0.2, t="in_cubic"
        )
        anim.bind(on_complete=self.add_content)
        anim.start(self)

    def add_content(self, *args):
        if self.content:
            self.ids.box_item.add_widget(self.content)
class ChevronRight(IRightBodyTouch, MDIconButton):
    angle = NumericProperty(0)   

class TitlePanel(TwoLineRightIconListItem):
    title = StringProperty()
    secondary = StringProperty()
class TaskCard(BoxLayout):
    required_time = StringProperty()
    description = StringProperty()