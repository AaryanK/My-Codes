from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
# from KivyOnTop import register_topmost,

Window.size = (320, 600)

class WindowManager(ScreenManager):
    pass

class MessageScreen(Screen):
    pass

class ChatScreen(Screen):
    pass

class MainApp(MDApp):
    def build(self):
        # register_topmost(Window, "Chat")
        self.theme_cls.theme_style='Dark'
        self.theme_cls.primary_palette = 'Brown'
        self.theme_cls.primary_hue='A100'
        self.theme_cls.accent_palette='Teal'
        self.theme_cls.accent_hue='A100'
        self.title="DragonZpyder"

        screens = [
            MessageScreen(name="chat")
        ]

        self.wm = WindowManager(transition=FadeTransition())
        for s in screens:
            self.wm.add_widget(s)

        return self.wm
MainApp().run()