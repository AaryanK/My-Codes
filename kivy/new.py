import os
os.environ['DISPLAY']=':0'
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MyGrid(GridLayout):
    def __init__(self,**kwargs):
        super(MyGrid,self).__init__(**kwargs)
        self.cols=1

        self.first = GridLayout()
        self.first.cols = 2
        self.first.add_widget(Label(text='Hey whats your First name? : '))
        self.fname = TextInput(multiline=False)
        self.first.add_widget(self.fname)

        self.first.add_widget(Label(text='Hey whats your Last name : '))
        self.lname = TextInput(multiline=False)
        self.first.add_widget(self.lname)

        self.first.add_widget(Label(text='Hey whats your email ? : '))
        self.ename = TextInput(multiline=False)
        self.first.add_widget(self.ename)
        self.add_widget(self.first)

        self.submit = Button(text='submit',font_size=40)
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)

    def pressed(self,instance):
        print(' pressed')
        print(f'Name : {self.fname.text} Last Name : {self.lname.text} email : {self.ename.text}')
        self.fname.text=''
        self.lname.text=''
        self.ename.text=''


class MyApp(App):
    def build(self):
        return MyGrid()

if __name__ == "__main__":
    MyApp().run()