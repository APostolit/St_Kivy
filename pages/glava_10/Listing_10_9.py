# Листинг 10.9
from kivy.lang import Builder
from kivymd.app import MDApp

KV = '''
MDScreen:
    BoxLayout:
        orientation: "vertical"
        MDTopAppBar:
            title: "Класс MDLabel"
            elevation: 2
        MDLabel:            
            text: "Текст 1"
            halign: "center"
        MDLabel:
            text: "Текст 2"
            theme_text_color: "Custom"
            text_color: 1, 0, 0, 1
            halign: "center"
        MDLabel:
            text: "Текст 3"
            font_size: dp(35)
            halign: "center"    
'''

class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

MainApp().run()