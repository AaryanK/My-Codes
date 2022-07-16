
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