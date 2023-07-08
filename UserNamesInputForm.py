from kivy.uix.widget import Widget
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty
)
from kivy.vector import Vector
from kivy.uix.boxlayout import BoxLayout

class UserNamesInputForm(Widget):
    p1_name = ObjectProperty(None)
    p2_name = ObjectProperty(None)
    cb_names_received = None
    cb_names_not_received = None
    caller = ObjectProperty(None)

    def __init__(self, caller, cb_names_received, cb_names_not_received):
        super().__init__()
        self.caller = caller
        self.cb_names_not_received = cb_names_not_received
        self.cb_names_received = cb_names_received

    def save_names(self):
        print("I am in save names")
        if(self.p1_name != '' and self.p2_name != ''):
            print('Need to see how to hide myself')
            self.cb_names_received(self.caller,(self.p1_name.text, self.p2_name.text))
        return

    def clear_widget(self):
        print("I am in clear widget")
        return
    
    def getPlayer1Name(self):
        return p1_name

    def getPlayer2Name(self):
        return p2_name