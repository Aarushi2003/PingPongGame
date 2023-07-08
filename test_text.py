# import Kivy
import kivy
import random

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class MyApp(App):
# layout
    def build(self):
        layout = BoxLayout(padding=10, orientation='vertical')
        btn1 = Button(text="OK")
        btn1.bind(on_press=self.buttonClicked)
        layout.add_widget(btn1)
        self.lbl1 = Label(text="test")
        layout.add_widget(self.lbl1)
        self.txt1 = TextInput(text='', multiline=False)
        layout.add_widget(self.txt1)
        return layout

# button click function
    def buttonClicked(self,btn):
        self.lbl1.text = "You wrote " + self.txt1.text

# run app
if __name__ == "__main__":
    MyApp().run()
 # join all items in a list into 1 big string