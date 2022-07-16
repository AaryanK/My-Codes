from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.metrics import dp
from kivy.uix.scrollview import ScrollView
from kivy.uix.pagelayout import PageLayout
from kivy.properties import StringProperty, BooleanProperty
from sympy import false

class BoxLayoutExample(BoxLayout):
    pass
    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    #     self.orientation = "vertical"
    #     b1 = Button(text="Button 1")
    #     b2 = Button(text="Button 2")
    #     b3 = Button(text="Button 3")
    #     self.add_widget(b1)
    #     self.add_widget(b2)
    #     self.add_widget(b3)

class WidgetsExample(GridLayout):
    my_text = StringProperty("1")
    count = 1
    count_enabled = BooleanProperty(False)  

    def on_click(self):
        # print("Button clicked")
        if self.count_enabled == True:
            self.count += 1
            self.my_text = str(self.count)

        elif self.count_enabled==False:
            print(False)
        # self.my_text = "Wow, you clicked the button"

    def on_toggle(self,  widget):
        # print("State: " + widget.state)
        if widget.state == "down":
            widget.text = "ON"
            self.count_enabled = True
            
        else:
            widget.text = "OFF"
            self.count_enabled = False
    
    def switch_on(self, widget):
        print(f"Switch state: {widget.active}")

# class PageLayoutExample(PageLayout):
#     pass

# class ScrollViewExample(ScrollView):
#     pass

class StackLayoutExample(StackLayout):
    pass
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "lr-tb"
        self.padding = (dp(20), dp(20), dp(20), dp(20))
        self.spacing.left = (dp(20), dp(20))
        for i in range(100):
            # size = dp(100) + i*10
            b = Button(text=str(i+1), size_hint = (None, None), size = (dp(100), dp(100)))
            self.add_widget(b)

# class GridLayoutExample(GridLayout):
#     pass

class AnchorLayoutExample(AnchorLayout):
    pass

class MainWidget(Widget):
    pass

class ThelabApp(App):
    pass
 
ThelabApp().run()
