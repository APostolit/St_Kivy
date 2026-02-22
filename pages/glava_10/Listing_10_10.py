# Листинг 10.10
from kivy.lang import Builder
from kivymd.app import MDApp

KV = '''
MDScreen:
    MDBoxLayout:
        orientation: "vertical"
        MDTopAppBar:
            title: "Класс MDIcon"
            elevation: 2
        MDLabel:
            text: "Иконки"
            font_size: dp(35)
            halign: "center"             
        MDIcon:            
            icon: "language-python"            
            pos_hint: {"center_x": .5, "center_y": .4}
        MDIcon:
            icon: "language-python"
            theme_text_color: "Custom"
            text_color: 1, 0, 0, 1
            pos_hint: {"center_x": .5, "center_y": .3}
        MDIcon:
            icon: "language-python"            
            font_size: dp(45)
            pos_hint: {"center_x": .5, "center_y": .2}
'''

class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

MainApp().run()