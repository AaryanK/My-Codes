from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDRectangleFlatButton, MDIconButton, MDFloatingActionButton
from kivymd.app import MDApp
# from kivymd.uix.textfield import Textfield
from kivy.lang import Builder, builder

username_string = """
MDTextField:
    hint_text:'Your name'
    helper_text: "Enter your username to continue"
    helper_text_mode : "on_focus"
    icon_right : "language-python"
    icon_right_color : app.theme_cls.primary_color
    pos_hint: {'center_x':0.5,'center_y':0.3}
    size_hint_x:None
    width : 300
    """

chrome_string= """
MDFloatingActionButton:
    icon: "opera"
    md_bg_color: app.theme_cls.primary_color
    pos_hint: {'center_x':0.3,'center_y':0.7}
"""

vscode_string= """
MDFloatingActionButton:
    icon: "volume-high"
    md_bg_color: app.theme_cls.primary_color
    pos_hint: {'center_x':0.1,'center_y':0.7}
"""

nav_strings = """
#import MDRectangleFlatButton kivymd.uix.button.MDRectangleFlatButton



BoxLayout:
    orientation:'vertical'
    



    MDBottomNavigation:
        panel_color: .2, .2, .2, 1
        

        MDBottomNavigationItem:
            name: 'screen 1'
            text: 'Apps'
            icon: 'application'
            

            MDRectangleFlatButton:
                text:'Power off'
                pos_hint:{'center_x': 0.5, 'center_y': 0.5}
                on_release:app.turn_off()
            MDFloatingActionButton:
                icon: "opera"
                md_bg_color: app.theme_cls.primary_color
                pos_hint: {'center_x':0.3,'center_y':0.7}
            MDFloatingActionButton:
                icon: "language-python"
                pos_hint: {'center_x':0.5,'center_y':0.7}
                on_release:app.turn_on()

        MDBottomNavigationItem:
            name: 'screen 2'
            text: 'Audio Controls'
            icon: 'music'

            MDLabel:
                text: 'I programming of C++'
                halign: 'center'

        MDBottomNavigationItem:
            name: 'screen 3'
            text: 'utilities'
            icon: 'language-javascript'

            MDLabel:
                text: 'JS'
                halign: 'center'

        MDBottomNavigationItem:
            name: 'screen 3'
            text: 'About'
            icon: 'information'

            MDLabel:
                text: 'JS'
                halign: 'center'
"""
from kivymd.uix.dialog import MDDialog
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.core.window import Window
import socket

HEADER = 64
PORT = 1234
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "192.168.1.64"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    # print(client.recv(2048).decode(FORMAT))

class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()

class Aaryans_appApp(MDApp):
    def build(self):
        Window.size = (2220, 1080)
        self.theme_cls.primary_palette = "Cyan"
        self.theme_cls.theme_style = "Dark"

        screen = Screen()
        screen.add_widget(
            Builder.load_string(nav_strings)
        )
        return screen

        
    def turn_on(self):
        self.comp_command_send('Turn on')
    
    def turn_off(self):
        self.comp_command_send('Turn off')

    def comp_command_send(self,msg):
        send(f"###{msg}###")
    

Aaryans_appApp().run()


'''MDRectangleFlatButton(
                text="Hello, World",
                pos_hint={"center_x": 0.5, "center_y": 0.5},
            '''
